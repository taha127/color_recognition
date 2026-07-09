import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog
import resources.resources_rc
from widgets.app_window import AppWindow
from widgets.activate_license_dialog import ActivateLicenseDialog
from services.license_manager import LicenseManager


def main():
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(":icons/favicon256.ico"))
    app.setApplicationName("Color Recognition App")
    license_manager = LicenseManager()
    if not license_manager.can_run():

        dlg = ActivateLicenseDialog()
        if dlg.exec() != QDialog.DialogCode.Accepted:
            sys.exit(0)

        if not license_manager.can_run():
            sys.exit(0)

    window = AppWindow()
    window.showMaximized()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
