import numpy as np
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

# =====================================================
# Color space utilities
# =====================================================

RGB_TO_XYZ = np.array([
    [0.4124564, 0.3575761, 0.1804375],
    [0.2126729, 0.7151522, 0.0721750],
    [0.0193339, 0.1191920, 0.9503041],
])


def srgb_to_linear(rgb):
    rgb = rgb / 255.0
    return np.where(
        rgb <= 0.04045,
        rgb / 12.92,
        ((rgb + 0.055) / 1.055) ** 2.4
    )


def linear_to_xyz(lin_rgb):
    return lin_rgb @ RGB_TO_XYZ.T


def mean_rgb_from_image(image):
    w = image.width()
    h = image.height()
    bpl = image.bytesPerLine()

    ptr = image.bits()

    arr = np.frombuffer(ptr, np.uint8).reshape((h, bpl))
    # Delete padding bytes
    arr = arr[:, :w * 3].reshape((h, w, 3))
    mean_rgb = arr.mean(axis=(0, 1))

    return mean_rgb


def convert_Qcolor_to_lab(qcolor):
    r, g, b = qcolor.red(), qcolor.green(), qcolor.blue()
    srgb = sRGBColor(r/255, g/255, b/255)
    lab = convert_color(srgb, LabColor)
    return lab
