from PySide6.QtWidgets import QDialog, QMessageBox

from ui.activate_license_dialog_ui import Ui_ActivateLicenseDialog
from services.license_manager import LicenseManager


class ActivateLicenseDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_ActivateLicenseDialog()
        self.ui.setupUi(self)
        self.license_manager = LicenseManager()
        self._connect_signals()

    def _connect_signals(self):
        self.ui.ActivateButton.clicked.connect(self.activate_license)
        self.ui.ExitButton.clicked.connect(self.reject)

    def activate_license(self):

        license_key = self.ui.LicenseKeyLineEdit.text().strip()

        if not license_key:

            QMessageBox.warning(
                self,
                "License",
                "Please enter your license key."
            )

            return

        success = self.license_manager.activate(
            license_key
        )

        if success:

            QMessageBox.information(
                self,
                "License",
                "License activated successfully."
            )
            self.accept()

        else:

            QMessageBox.critical(
                self,
                "License",
                "Invalid license key."
            )
            self.ui.LicenseKeyLineEdit.selectAll()
            self.ui.LicenseKeyLineEdit.setFocus()
