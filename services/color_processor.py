import numpy as np
import cv2
from PySide6.QtGui import QImage, QColor
from colormath.color_objects import LabColor
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
        Extract the representative RGB color from ROI.
        """
    
        arr = self._qimage_to_numpy(roi_qimage)
    
        blurred = cv2.medianBlur(arr, self.median_kernel)
    
        mean_rgb = blurred.mean(axis=(0, 1))
    
        return {
            "mean_rgb": mean_rgb
        }

    def compute_delta_e(self, lab1: LabColor, lab2: LabColor) -> float:
        return delta_e_cie2000(lab1, lab2)

    # -------------------------------------------------
    # Core Color Conversions
    # -------------------------------------------------

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
