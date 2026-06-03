from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget

from widgets.main_window import MainWindow
from widgets.calibration_page import CalibrationPage
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
        self.calibration_page = CalibrationPage(self.camera_widget)

        self.stack.addWidget(self.main_page)
        self.stack.addWidget(self.calibration_page)

        self.stack.setCurrentWidget(self.main_page)

        # Navigation
        self.main_page.go_calibration.connect(self.show_calibration)
        self.calibration_page.profileSelected.connect(self.show_detection)

        self.calibration_page.profileSelected.connect(
            self.main_page.set_profile)

    # go to calibration page
    def show_calibration(self):

        self.stack.setCurrentWidget(self.calibration_page)

    # come back to main page with Profile
    def show_detection(self, profile):

        self.main_page.ui.NameOfProfile.setText(profile["name"])
        self.stack.setCurrentWidget(self.main_page)
