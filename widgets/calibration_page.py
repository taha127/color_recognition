from PySide6.QtWidgets import (
    QWidget, QMainWindow,
    QWidget,
    QCheckBox,
    QRadioButton,
    QButtonGroup,
    QHBoxLayout,
    QMessageBox,
    QColorDialog,
    QTableWidgetItem,
    QPushButton,
    QStyle,
    QButtonGroup,
    QVBoxLayout,
    QHeaderView,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor
from widgets.roi_graphics_view import ROIGraphicsView

from ui.calibration_ui import Ui_Calibration_window

from services.recognation_model import create_recognition_model, save_profile, load_profiles, delete_profile_by_name
from services.camera_manager import CameraWidget
from services.color_processor import ColorProcessor


class CalibrationPage(QMainWindow):
    profileSelected = Signal(dict)

    def __init__(self, camera_widget: CameraWidget):
        super().__init__()
        # Calibration dataset
        self.samples_xyz = []
        self.samples_lab = []
        self.sample_count = 0
        self.profiles = {}
        self.proccessor = ColorProcessor()
        self.ui = Ui_Calibration_window()
        self.ui.setupUi(self)
        self.setWindowTitle("Calibration Page")
        # Button groups
        self.profile_group = QButtonGroup(self)
        self.profile_group.setExclusive(True)
        # Inject widgets into table
        self.setup_profile_table_widgets()
        # Load profiles to table
        self.load_profiles_to_table()

        if self.ui.CameraScan.layout() is None:
            self.ui.CameraScan.setLayout(QVBoxLayout())

        self.camera_widget = camera_widget

        self.roi_view = ROIGraphicsView()
        self.roi_view.setScene(self.camera_widget.scene)
        self.ui.CameraScan.layout().addWidget(self.roi_view)
        # Connect Take Photo button
        self.ui.TakePhotoBtn.clicked.connect(self.take_photo)
        # Connect Cancel button
        self.ui.CancelBtn.clicked.connect(self.handle_cancel)
        # Connect Color Picker
        self.ui.PickColorBtn.clicked.connect(self.pick_color)
        # Connect Ok color calibration button
        self.ui.OkBtn.clicked.connect(self.add_calibration_sample)
        # Connect save model calibration button
        self.ui.SaveButton.clicked.connect(self.build_and_save_model)
        # Connect continue button
        self.ui.CountinueBtn.clicked.connect(self.on_continue_clicked)

        # Table UI
        calibrated_header = self.ui.CalibratedColorsTable.horizontalHeader()
        calibrated_header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        calibrated_header.setSectionResizeMode(1, QHeaderView.Stretch)
        calibrated_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        prf_header = self.ui.PrfTable.horizontalHeader()
        prf_header.setSectionResizeMode(0, QHeaderView.Stretch)
        prf_header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        prf_header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        prf_header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        prf_header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

    # ------------------- setup profile ------------------- #
    def setup_profile_table_widgets(self):

        table = self.ui.PrfTable
        rows = table.rowCount()

        # group radios -> only one selectable
        self.delete_group = QButtonGroup(self)
        self.delete_group.setExclusive(True)

        SELECT_COL = 3
        DELETE_COL = 4

        for row in range(rows):

            # ---------- Checkbox ----------
            checkbox = QCheckBox()
            self.profile_group.addButton(checkbox, row)
            self.ui.PrfTable.setCellWidget(row, SELECT_COL, checkbox)
            layout = QHBoxLayout()
            layout.addWidget(checkbox)
            layout.setAlignment(checkbox, Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)

            container = QWidget()
            container.setLayout(layout)

            table.setCellWidget(row, SELECT_COL, container)

            # ---------- Radio ----------
            radio = QRadioButton()

            layout2 = QHBoxLayout()
            layout2.addWidget(radio)
            layout2.setAlignment(radio, Qt.AlignCenter)
            layout2.setContentsMargins(0, 0, 0, 0)

            container2 = QWidget()
            container2.setLayout(layout2)

            table.setCellWidget(row, DELETE_COL, container2)

            self.delete_group.addButton(radio)

    def take_photo(self):
        pix = self.camera_widget.take_photo()
        if pix is None:
            QMessageBox.warning(self, "Error", "Failed to capture photo")

    # ------------------ Cancel captured photo and return to live mode ---------------- #
    def handle_cancel(self):
        if self.camera_widget.captured_pixmap is None:
            return

        msg = QMessageBox(self)
        msg.setWindowTitle("Confirmation")
        msg.setText(
            "Do you want to discard the captured photo and take another?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        result = msg.exec()

        if result == QMessageBox.Yes:
            self.camera_widget.resume_live()

    # ------------------- Color Picker ------------------- #
    def pick_color(self):
        color = QColorDialog.getColor(
            parent=self,
            options=QColorDialog.DontUseNativeDialog
        )

        if color.isValid():
            self.ui.CodeIn.setText(color.name())

    # ------------------- Get XYZ from ROI ------------------ #
    def get_xyz_from_roi(self):

        if self.camera_widget.captured_pixmap is None:
            QMessageBox.warning(self, "Error", "Capture photo first")
            return None

        rect = self.roi_view.get_roi_rect()

        if rect is None:
            QMessageBox.warning(self, "Error", "Select ROI")
            return None

        frame = self.camera_widget.last_frame
        rect_int = rect.toAlignedRect()
        rect_int = rect_int.intersected(frame.rect())
        roi_img = frame.copy(rect_int)
        result = self.proccessor.process_roi(roi_img)
        xyz_obj = result["xyz"]

        return [xyz_obj.xyz_x, xyz_obj.xyz_y, xyz_obj.xyz_z]

    # ------------------ Convert HEX to LAB ---------------- #
    def hex_to_lab(self):

        hex_code = self.ui.CodeIn.text()

        try:
            lab = self.proccessor.hex_to_lab(hex_code)
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid HEX color")
            return None
        return [lab.lab_l, lab.lab_a, lab.lab_b]

    # ----------------- Add calibration sample ---------------- #
    def add_calibration_sample(self):

        xyz = self.get_xyz_from_roi()
        if xyz is None:
            return

        lab = self.hex_to_lab()
        if lab is None:
            return

        self.samples_xyz.append(xyz)
        self.samples_lab.append(lab)

        self.sample_count += 1

        self.update_calibrated_table(lab)

        QMessageBox.information(self, "Added",
                                f"Sample {self.sample_count} stored")

        self.camera_widget.resume_live()

    # ----------------- Update Calibrated Table ---------------- #
    def update_calibrated_table(self, lab):

        table = self.ui.CalibratedColorsTable
        row = table.rowCount()
        table.insertRow(row)

        # Row
        row_item = QTableWidgetItem(str(self.sample_count))
        row_item.setFlags(row_item.flags() & ~Qt.ItemIsEditable)
        table.setItem(row, 0, row_item)

        # Color HEX
        hex_code = self.ui.CodeIn.text()
        hex_item = QTableWidgetItem(hex_code)
        rgb = self.proccessor.hex_to_rgb(hex_code)
        hex_item.setBackground(QColor(*rgb))
        txt_color = "#000000" if (
            rgb[0]*0.299 + rgb[1]*0.587 + rgb[2]*0.114) > 186 else "#FFFFFF"
        hex_item.setForeground(QColor(txt_color))
        hex_item.setFlags(hex_item.flags() & ~Qt.ItemIsEditable)
        table.setItem(row, 1, hex_item)

        # Delete Button
        btn = QPushButton()
        btn.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxCritical))
        btn.clicked.connect(lambda _, r=row: self.delete_sample(r))

        table.setCellWidget(row, 2, btn)

    # ----------------- Build and Save Model ---------------- #
    def build_and_save_model(self):

        name = self.ui.NamePrflineEdit.text().strip()

        if not name:
            QMessageBox.warning(self, "Error", "Enter profile name")
            return

        if len(self.samples_xyz) < 4:
            QMessageBox.warning(self, "Error", "Need more samples")
            return

        # -------- Train ----------
        model = create_recognition_model(
            self.samples_xyz,
            self.samples_lab
        )

        # -------- Save ----------
        save_profile(
            name,
            self.samples_xyz,
            self.samples_lab,
            model
        )

        QMessageBox.information(self, "Done", "Model saved")

        self.load_profiles_to_table()

        self.samples_xyz.clear()
        self.samples_lab.clear()
        self.sample_count = 0

    # ---------------- Profile Table Functions ---------------- #
    def load_profiles_to_table(self):

        for b in self.profile_group.buttons():
            self.profile_group.removeButton(b)

        self.profiles = load_profiles()
        table = self.ui.PrfTable

        table.setRowCount(0)

        for p in self.profiles:

            row = table.rowCount()
            table.insertRow(row)

            table.setItem(row, 0, QTableWidgetItem(p["name"]))
            table.setItem(row, 1, QTableWidgetItem(str(len(p["samples_xyz"]))))
            table.setItem(row, 2, QTableWidgetItem(p["created"]))

            # checkbox select
            chk = QCheckBox()
            self.profile_group.addButton(chk, row)
            layout = QHBoxLayout()
            layout.addWidget(chk)
            layout.setAlignment(chk, Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            container = QWidget()
            container.setLayout(layout)
            table.setCellWidget(row, 3, container)

            # Delete Button
            btn = QPushButton()
            btn.setIcon(self.style().standardIcon(
                QStyle.SP_MessageBoxCritical))
            btn.clicked.connect(lambda _, r=row: self.delete_profile(r))
            table.setCellWidget(row, 4, btn)

    # ----------------- Delete Sample from Calibrated Table ---------------- #
    def delete_sample(self, row):

        table = self.ui.CalibratedColorsTable

        if row >= len(self.samples_lab):
            return

        # -------- confirm dialog ----------
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            "Delete this sample?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        # --------- remove from dataset ----------
        del self.samples_lab[row]
        del self.samples_xyz[row]

        # --------- remove from table ----------
        table.removeRow(row)

        self.sample_count -= 1

        self.rebind_delete_buttons()

    # ----------------- Continue with selected profile ---------------- #
    def rebind_delete_buttons(self):

        table = self.ui.CalibratedColorsTable

        for row in range(table.rowCount()):

            btn = table.cellWidget(row, 2)
            if btn:
                try:
                    btn.clicked.disconnect()
                except:
                    pass

                btn.clicked.connect(lambda _, r=row: self.delete_sample(r))

    # ----------------- Delete profile from profile table ---------------- #
    def delete_profile(self, row):

        if row >= len(self.profiles):
            return

        profile = self.profiles[row]

        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Delete profile '{profile['name']} and its model'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        delete_profile_by_name(profile["name"])
        QMessageBox.information(
            self, "Deleted", f"Profile '{profile['name']}' removed successfully.")
        self.load_profiles_to_table()

    # ----------------- Continue with selected profile ---------------- #
    def on_continue_clicked(self):

        button = self.profile_group.checkedButton()

        if button is None:
            QMessageBox.warning(self, "Error", "Select a profile")
            return

        row = self.profile_group.id(button)

        selected_profile = self.profiles[row]
        self.profileSelected.emit(selected_profile)
