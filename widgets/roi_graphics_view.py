from PySide6.QtWidgets import QGraphicsView, QGraphicsRectItem
from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QPen


class ROIGraphicsView(QGraphicsView):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.origin = QPointF()
        self.rect_item = None
        self.drawing = False

    # -------------------
    # Mouse Press
    # -------------------

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.origin = self.mapToScene(event.pos())
            self.drawing = True

            if self.rect_item:
                self.scene().removeItem(self.rect_item)

            self.rect_item = QGraphicsRectItem()
            self.rect_item.setPen(QPen(Qt.red, 2))
            self.scene().addItem(self.rect_item)

        super().mousePressEvent(event)

    # -------------------
    # Mouse Move
    # -------------------

    def mouseMoveEvent(self, event):

        if self.drawing and self.rect_item:

            current = self.mapToScene(event.pos())

            rect = QRectF(self.origin, current).normalized()

            size = min(rect.width(), rect.height())
            rect.setWidth(size)
            rect.setHeight(size)

            self.rect_item.setRect(rect)

        super().mouseMoveEvent(event)

    # -------------------
    # Mouse Release
    # -------------------

    def mouseReleaseEvent(self, event):

        self.drawing = False
        super().mouseReleaseEvent(event)

    # To get the ROI rectangle in scene coordinates
    def get_roi_rect(self):
        if self.rect_item:
            return self.rect_item.rect()
        return None
