from PySide6.QtWidgets import (QDialog, QFileDialog,
                               QTreeWidgetItem,
                               QMessageBox)
from PySide6.QtCore import Qt, Signal
from ui.profile_dialog_ui import Ui_Dialog
import os
from services.profile_manager import ProfileManager
from pathlib import Path

MAX_RECENT_PROFILES = 3


class ProfileDialog(QDialog):

    deleteRequested = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.profile_path = ""
        self.profile_name = ""
        self.save_profile = False
        self.selected_recent = None
        self.pm = ProfileManager()

        self.ui.BrowseButton.clicked.connect(
            self.browse_profile
        )

        self.ui.RecentProfilesTree.itemSelectionChanged.connect(
            self.select_recent
        )

        self.ui.DeleteButton.clicked.connect(
            self.delete_recent
        )

        self.ui.RecentProfilesTree.header().setStretchLastSection(True)
        self.ui.RecentProfilesTree.setRootIsDecorated(False)

        self.ui.RecentProfilesTree.setAlternatingRowColors(True)

        self.ui.RecentProfilesTree.setUniformRowHeights(True)

        self.load_recent_profiles()

    def browse_profile(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select ICC Profile",
            "",
            "ICC Files (*.icc *.icm)"
        )
        if filename:
            self.selected_recent = None
            self.ui.RecentProfilesTree.clearSelection()
            self.ui.AddressProfile.setText(filename)

    def accept(self):

        if self.selected_recent is not None:
            self.profile_name = self.selected_recent["name"]
            self.profile_path = self.selected_recent["path"]
            self.save_profile = False
            super().accept()
            return

        self.profile_path = self.ui.AddressProfile.text()
        self.save_profile = self.ui.SaveCheckBox.isChecked()
        entered = self.ui.NameProfilelineEdit.text().strip()

        if entered:
            self.profile_name = entered

        else:
            self.profile_name = Path(self.profile_path).stem

        if not self.validate_inputs():
            return

        super().accept()

    def load_recent_profiles(self):

        self.ui.RecentProfilesTree.clear()
        profiles = self.pm.last_profiles(MAX_RECENT_PROFILES)

        self.recent_profiles = profiles

        for profile in self.recent_profiles:
            item = QTreeWidgetItem()
            item.setText(0, f"{profile['name']}: ")
            item.setText(1, profile["path"])
            item.setData(0, Qt.ItemDataRole.UserRole, profile)
            self.ui.RecentProfilesTree.addTopLevelItem(item)

        self.update_recent_section()

    def select_recent(self):

        items = self.ui.RecentProfilesTree.selectedItems()

        if not items:

            self.selected_recent = None
            return

        item = items[0]
        self.selected_recent = item.data(0, Qt.ItemDataRole.UserRole)
        if self.selected_recent is None:
            return

        self.ui.AddressProfile.setText(
            self.selected_recent["path"]
        )

        self.ui.NameProfilelineEdit.setText(
            self.selected_recent["name"]
        )

    def delete_recent(self):

        if self.selected_recent is None:

            return

        name = self.selected_recent["name"]
        self.deleteRequested.emit(name)
        self.selected_recent = None
        self.ui.AddressProfile.clear()
        self.ui.NameProfilelineEdit.clear()
        self.load_recent_profiles()

    def validate_inputs(self) -> bool:

        if not self.profile_path:
            QMessageBox.warning(
                self,
                "No Profile Selected",
                "Please select an ICC profile."
            )
            return False

        if not os.path.exists(self.profile_path):
            QMessageBox.warning(
                self,
                "File Not Found",
                "The selected ICC profile does not exist."
            )
            return False

        return True

    def update_recent_section(self):

        count = self.ui.RecentProfilesTree.topLevelItemCount()
        if count == 0:

            self.ui.NoProfilesLabel.show()
            self.ui.RecentProfilesTree.hide()
            self.ui.DeleteButton.hide()
            return

        self.ui.NoProfilesLabel.hide()
        self.ui.RecentProfilesTree.show()
        self.ui.DeleteButton.show()
        row_height = self.ui.RecentProfilesTree.sizeHintForRow(0)
        height = row_height * count + 4
        self.ui.RecentProfilesTree.setFixedHeight(height)
