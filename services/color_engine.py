import os
from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor, LabColor
from PIL import Image
from PIL import ImageCms
from typing import Sequence


class ColorEngine:

    def __init__(self):

        self.profile = None
        self.transform = None
        self.srgb = ImageCms.createProfile("sRGB")

    def load_printer_profile(self, profile_path):

        if not os.path.exists(profile_path):
            raise FileNotFoundError(profile_path)

        self.profile = ImageCms.getOpenProfile(profile_path)
        try:
            self.transform = ImageCms.buildTransformFromOpenProfiles(
                self.srgb,
                self.profile,
                "RGB",
                "RGB",
                renderingIntent=ImageCms.Intent.PERCEPTUAL
            )
        except Exception as e:
            self.transform = None
            self.profile = None
            raise RuntimeError(
                f"Failed to build transform from printer profile: {e}")

    def unload_printer_profile(self):
        self.transform = None
        self.profile = None

        import gc
        gc.collect()

    def camera_rgb_to_printer_rgb(self, rgb):

        if self.transform is None:
            raise RuntimeError("Printer ICC profile is not loaded.")

        img = Image.new(
            "RGB",
            (1, 1),
            tuple(rgb)
        )
        out = ImageCms.applyTransform(
            img,
            self.transform
        )

        return out.getpixel((0, 0))

    def rgb_to_lab(self, rgb: tuple | list):
        """
        Convert RGB (0-255) to Lab.

        Parameters
        ----------
        rgb : tuple | list
            (R, G, B)

        Returns
        -------
        LabColor
        """

        r, g, b = rgb
        rgb_color = sRGBColor(
            r / 255.0,
            g / 255.0,
            b / 255.0
        )
        lab = convert_color(
            rgb_color,
            LabColor
        )
        return lab

    def lab_to_rgb(self, lab: LabColor | tuple):
        """
        Convert LabColor or (L,a,b) tuple to RGB.
        """

        if isinstance(lab, (tuple, list)):
            lab = LabColor(*lab)

        rgb = convert_color(lab, sRGBColor)
        return (
            max(0, min(255, int(round(rgb.clamped_rgb_r * 255)))),
            max(0, min(255, int(round(rgb.clamped_rgb_g * 255)))),
            max(0, min(255, int(round(rgb.clamped_rgb_b * 255))))
        )

    def rgb_to_hex(self, rgb: Sequence[int]):
        """
        Convert RGB (0-255) to HEX string.

        Parameters
        ----------
        rgb : tuple | list | numpy.ndarray
            (R, G, B)

        Returns
        -------
        str
            HEX color string (e.g. "#7A5030")
        """

        r, g, b = map(int, rgb)
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        return "#{:02X}{:02X}{:02X}".format(r, g, b)

    def hex_to_rgb(self, hex_color: str):
        """
        Convert HEX string to RGB tuple.

        Parameters
        ----------
        hex_color : str
            "#RRGGBB" or "RRGGBB"

        Returns
        -------
        tuple
            (R, G, B)
        """

        hex_color = hex_color.lstrip("#")

        if len(hex_color) != 6:
            raise ValueError("HEX color must have 6 digits.")

        return (
            int(hex_color[0:2], 16),
            int(hex_color[2:4], 16),
            int(hex_color[4:6], 16),
        )

    def process(self, rgb: Sequence[int]):
        """
        Full color processing pipeline.

        Parameters
        ----------
        rgb : tuple | list | numpy.ndarray
            Camera RGB (0-255)

        Returns
        -------
        dict
            {
                camera_rgb,
                camera_lab,
                camera_hex,

                printer_rgb,
                printer_lab,
                printer_hex
            }
        """

        # ---------- Camera RGB ----------
        camera_rgb = tuple(map(int, rgb))
        # Camera Lab
        camera_lab = self.rgb_to_lab(camera_rgb)
        # Camera HEX
        camera_hex = self.rgb_to_hex(camera_rgb)
        # ---------- Printer RGB ----------
        printer_rgb = self.camera_rgb_to_printer_rgb(camera_rgb)
        # Printer Lab
        printer_lab = self.rgb_to_lab(printer_rgb)
        # Printer HEX
        printer_hex = self.rgb_to_hex(printer_rgb)

        return {
            "camera_rgb": camera_rgb,
            "camera_lab": camera_lab,
            "camera_hex": camera_hex,

            "printer_rgb": printer_rgb,
            "printer_lab": printer_lab,
            "printer_hex": printer_hex,
        }
