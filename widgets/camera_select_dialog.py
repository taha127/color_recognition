from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QListWidget,
    QPushButton
)

from PySide6.QtMultimedia import QMediaDevices


class CameraSelectDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Select Camera")

        layout = QVBoxLayout(self)

        self.list = QListWidget()
        layout.addWidget(self.list)

        self.ok_btn = QPushButton("OK")
        layout.addWidget(self.ok_btn)

        self.devices = QMediaDevices.videoInputs()

        for dev in self.devices:
            self.list.addItem(dev.description())

        self.ok_btn.clicked.connect(self.accept)

    def selected_camera(self):
        row = self.list.currentRow()
        if row >= 0:
            return self.devices[row]
        return None
