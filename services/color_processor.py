import numpy as np
import cv2
from colormath.color_conversions import convert_color
from PySide6.QtGui import QImage, QColor
from colormath.color_objects import LabColor, XYZColor, sRGBColor
from colormath.color_diff import delta_e_cie2000


class ColorProcessor:
    def __init__(self, median_kernel: int = 41):
        if median_kernel % 2 == 0:
            raise ValueError("Median kernel must be odd.")
        self.median_kernel = median_kernel

    # -------------------------------------------------
    # Public API
    # -------------------------------------------------

    def process_roi(self, roi_qimage: QImage):
        """
        Full pipeline:
        QImage -> median -> mean RGB -> XYZ -> Lab
        Returns dict with all stages.
        """

        arr = self._qimage_to_numpy(roi_qimage)

        blurred = cv2.medianBlur(arr, self.median_kernel)

        mean_rgb = blurred.mean(axis=(0, 1))

        xyz = self.rgb_to_xyz(mean_rgb)
        lab = self.xyz_to_lab(xyz)

        return {
            "mean_rgb": mean_rgb,
            "xyz": xyz,
            "lab": lab
        }

    def compute_delta_e(self, lab1: LabColor, lab2: LabColor) -> float:
        return delta_e_cie2000(lab1, lab2)

    # -------------------------------------------------
    # Core Color Conversions
    # -------------------------------------------------

    def rgb_to_xyz(self, rgb):
        """
        rgb: array-like [R,G,B] in 0-255
        """

        rgb = np.array(rgb) / 255.0

        # sRGB gamma correction
        rgb_linear = np.where(
            rgb <= 0.04045,
            rgb / 12.92,
            ((rgb + 0.055) / 1.055) ** 2.4
        )

        # sRGB D65 matrix
        M = np.array([
            [0.4124564, 0.3575761, 0.1804375],
            [0.2126729, 0.7151522, 0.0721750],
            [0.0193339, 0.1191920, 0.9503041],
        ])

        xyz = np.dot(M, rgb_linear)

        return XYZColor(*xyz)

    def xyz_to_lab(self, xyz: XYZColor):
        return convert_color(xyz, LabColor)

    def qcolor_to_lab(self, color: QColor):

        if not color.isValid():
            raise ValueError("Invalid QColor")

        r = color.red()
        g = color.green()
        b = color.blue()

        # Convert to sRGBColor (0-1 range)
        rgb = sRGBColor(r / 255.0, g / 255.0, b / 255.0)

        lab = convert_color(rgb, LabColor)

        return lab

    def hex_to_lab(self, hex_str: str):

        color = QColor(hex_str)

        if not color.isValid():
            raise ValueError("Invalid HEX color")

        return self.qcolor_to_lab(color)

    def hex_to_rgb(self, hex_str: str):
        color = QColor(hex_str)

        if not color.isValid():
            raise ValueError("Invalid HEX color")

        return [color.red(), color.green(), color.blue()]

    # -------------------------------------------------
    # Internal Helpers
    # -------------------------------------------------

    def _qimage_to_numpy(self, qimage: QImage):

        qimage = qimage.convertToFormat(QImage.Format_RGB888)

        width = qimage.width()
        height = qimage.height()
        bytes_per_line = qimage.bytesPerLine()

        ptr = qimage.bits()
        arr = np.frombuffer(ptr, dtype=np.uint8)

        arr = arr.reshape((height, bytes_per_line))

        # Remove padding
        arr = arr[:, :width * 3]

        arr = arr.reshape((height, width, 3))

        return arr.copy()
