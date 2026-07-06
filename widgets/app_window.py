from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget

from widgets.main_window import MainWindow
from services.camera_manager import CameraManager, CameraWidget
from widgets.camera_select_dialog import CameraSelectDialog


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # Camera Manager
        self.camera_manager = CameraManager()

        dlg = CameraSelectDialog()
        if dlg.exec():
            device = dlg.selected_camera()
            if device:
                self.camera_manager.start(device)

        # Create ONE shared CameraWidget
        self.camera_widget = CameraWidget(
            self.camera_manager.get_camera()
        )

        # Pages
        self.main_page = MainWindow(self.camera_widget)
        self.stack.addWidget(self.main_page)

        self.stack.setCurrentWidget(self.main_page)
