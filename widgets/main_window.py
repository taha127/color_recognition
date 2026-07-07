# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QWidget,
                               QVBoxLayout,
                               QMessageBox,
                               QTableWidgetItem,
                               QAbstractItemView,
                               QHBoxLayout,
                               QCheckBox,
                               QHeaderView,)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFontMetrics
from services.camera_manager import CameraWidget
from widgets.roi_graphics_view import ROIGraphicsView

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui.main_window_ui import Ui_Widget
from widgets.profile_dialog import ProfileDialog
from services.color_processor import ColorProcessor
from services.profile_manager import ProfileManager
from services.color_history_srv import ColorHistoryService
from services.color_engine import ColorEngine


class MainWindow(QWidget):

    def __init__(self, camera_widget: CameraWidget):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Color Recognition")
        self.processor = ColorProcessor(median_kernel=41)
        self.color_history_service = ColorHistoryService()
        self.pm = ProfileManager()
        self.engine = ColorEngine()

        self.setup_saved_colors_table()
        self.load_saved_colors()
        self.ui.SaveActBtn.setEnabled(False)
        self.ui.RstBtn.setEnabled(False)
        self.model = None
        if self.ui.CameraScan.layout() is None:
            self.ui.CameraScan.setLayout(QVBoxLayout())

        self.camera_widget = camera_widget

        self.roi_view = ROIGraphicsView()
        self.roi_view.setScene(self.camera_widget.scene)
        self.ui.CameraScan.layout().addWidget(self.roi_view)
        self.ui.ProfileSelectorBtn.clicked.connect(self.open_profile_dialog)
        self.ui.TakePhotoBtn.clicked.connect(self.take_photo)
        self.ui.ScanBtn.clicked.connect(self.scan)
        self.ui.CancelBtn.clicked.connect(self.handle_cancel)
        self.ui.SaveColorBtn.clicked.connect(self.save_detected_color)
        table = self.ui.SavedColorTable
        table.itemChanged.connect(self.on_table_item_changed)
        self.ui.SaveActBtn.clicked.connect(
            self.apply_table_saved_colors_changes)
        self.ui.RstBtn.clicked.connect(self.reset_table_changes)

        # Load Saved Profile
        self.update_profile_name_and_load_profile()

    def take_photo(self):
        pix = self.camera_widget.take_photo()
        if not self.engine.has_profile:
            QMessageBox.warning(
                self, "Error", "No ICC profile selected.")
            return
        if pix is None:
            QMessageBox.warning(self, "Error", "Failed to capture photo")

    def scan(self):

        pix = self.camera_widget.captured_pixmap
        if pix is None:
            QMessageBox.warning(
                self, "Error", "Failed to capture image from camera.")
            return

        if self.camera_widget.captured_pixmap is None:
            return

        rect = self.roi_view.get_roi_rect()

        if rect is None:
            QMessageBox.warning(self, "Error", "Select ROI")
            return

        frame = self.camera_widget.last_frame
        rect_int = rect.toAlignedRect()
        rect_int = rect_int.intersected(frame.rect())

        roi_img = frame.copy(rect_int)

        # -------- Process ROI --------
        result = self.processor.process_roi(roi_img)

        mean_rgb = result["mean_rgb"]
        color = self.engine.process(mean_rgb)
        #########################################################
        # print("mean_rgb:", self.engine.rgb_to_hex(mean_rgb))
        # print("printer_rgb:", color["printer_rgb"])
        # print("printer_lab:", color["printer_lab"])
        # print("camera_rgb:", color["camera_rgb"])
        # print("camera_hex:", color["camera_hex"])
        # print("camera_lab:", color["camera_lab"])
        ############################################################
        printer_hex = color["printer_hex"]
        r, g, b = color["printer_rgb"]
        txt_color = "#000000" if (
            r*0.299 + g*0.587 + b*0.114) > 140 else "#FFFFFF"

        # -------- Show in UI --------
        self.ui.ColorRecognationLabel.setText(printer_hex)
        self.ui.ColorRecognationLabel.setStyleSheet(
            f"background-color: {printer_hex}; color: {txt_color};"
        )

        self.camera_widget.resume_live()

    # ------------------ Cancel captured photo and return to live mode ---------------- #
    def handle_cancel(self):
        if self.camera_widget.captured_pixmap is None:
            return

        msg = QMessageBox(self)
        msg.setWindowTitle("Confirmation")
        msg.setText(
            "Do you want to discard the captured photo scaning?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        result = msg.exec()

        if result == QMessageBox.Yes:
            self.camera_widget.resume_live()

    def save_detected_color(self):

        color_code = self.ui.ColorRecognationLabel.text().strip()
        color_name = self.ui.NameColorIn.text().strip()

        if not color_code:
            QMessageBox.warning(self, "Error", "No detected color code.")
            return

        if not color_name:
            QMessageBox.warning(
                self, "Error", "Please enter a name for the color.")
            return

        self.color_history_service.save_color(color_name, color_code)
        QMessageBox.information(
            self, "Saved", f"Color '{color_name}' saved successfully.")
        self.ui.NameColorIn.clear()

    def setup_saved_colors_table(self):

        table = self.ui.SavedColorTable
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)

        table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

    def load_saved_colors(self):

        table = self.ui.SavedColorTable
        table.setRowCount(0)

        colors = self.color_history_service.load_saved_colors()
        for index, color in enumerate(colors):
            self.add_color_to_table(index, color)

        table.blockSignals(False)
        self.ui.SaveActBtn.setEnabled(False)
        self.ui.RstBtn.setEnabled(False)

    def add_color_to_table(self, index, color):

        table = self.ui.SavedColorTable
        row = table.rowCount()
        table.insertRow(row)

        # Row number
        row_item = QTableWidgetItem(str(row + 1))
        row_item.setTextAlignment(Qt.AlignCenter)
        table.setItem(row, 0, row_item)
        row_item.setFlags(row_item.flags() & ~Qt.ItemIsEditable)

        # Name
        name_item = QTableWidgetItem(color["name"])
        name_item.setTextAlignment(Qt.AlignCenter)
        table.setItem(row, 1, name_item)

        # Color code
        color_item = QTableWidgetItem(color["hex"])
        color_item.setTextAlignment(Qt.AlignCenter)
        rgb = self.processor.hex_to_rgb(color["hex"])
        color_item.setBackground(QColor(color["hex"]))
        txt_color = "#000000" if (
            rgb[0]*0.299 + rgb[1]*0.587 + rgb[2]*0.114) > 186 else "#FFFFFF"
        color_item.setForeground(QColor(txt_color))
        color_item.setFlags(color_item.flags() & ~Qt.ItemIsEditable)
        table.setItem(row, 2, color_item)

        # Date
        date_item = QTableWidgetItem(color["saved_at"])
        date_item.setTextAlignment(Qt.AlignCenter)
        date_item.setFlags(date_item.flags() & ~Qt.ItemIsEditable)
        table.setItem(row, 3, date_item)

        # Delete CheckBox
        checkbox = QCheckBox()

        layout = QHBoxLayout()
        layout.addWidget(checkbox)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        container = QWidget()
        container.setLayout(layout)

        table.setCellWidget(row, 4, container)
        checkbox.stateChanged.connect(self.on_checkbox_changed)

        self.ui.SaveActBtn.setEnabled(False)
        self.ui.RstBtn.setEnabled(False)

    def save_detected_color(self):

        color_code = self.ui.ColorRecognationLabel.text().strip('-')
        color_name = self.ui.NameColorIn.text().strip()

        if not color_code:
            QMessageBox.warning(self, "Error", "No detected color code")
            return

        if not color_name:
            QMessageBox.warning(self, "Error", "Enter color name")
            return

        new_entry = self.color_history_service.save_color(
            color_name, color_code)

        self.add_color_to_table(0, new_entry)

        self.ui.NameColorIn.clear()
        self.ui.ColorRecognationLabel.clear()

    def apply_table_saved_colors_changes(self):

        table = self.ui.SavedColorTable
        colors = self.color_history_service.load_saved_colors()

        rows_to_delete = []
        rename_operations = []

        for row in range(table.rowCount()):

            cell_widget = table.cellWidget(row, 4)
            checkbox = cell_widget.layout().itemAt(0).widget()

            current_name = table.item(row, 1).text()
            original_name = colors[row]["name"]

            if checkbox.isChecked():
                rows_to_delete.append(original_name)

            else:
                if current_name != original_name:
                    rename_operations.append((original_name, current_name))

        if rows_to_delete:
            for name in rows_to_delete:
                self.color_history_service.delete_color_by_name(name)
        if rename_operations:
            for old_name, new_name in rename_operations:
                self.color_history_service.rename_color(old_name, new_name)

        self.load_saved_colors()
        QMessageBox.information(self, "Saved", "Changes saved successfully.")

    def reset_table_changes(self):

        reply = QMessageBox.question(
            self,
            "Reset Changes",
            "All unsaved changes will be lost. Continue?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        # Reload fresh data from JSON
        self.load_saved_colors()

        QMessageBox.information(
            self, "Reset", "Changes reverted successfully.")

    def enable_action_buttons(self):
        self.ui.SaveActBtn.setEnabled(True)
        self.ui.RstBtn.setEnabled(True)

    def on_table_item_changed(self, item: QTableWidgetItem):

        if item.column() == 1:  # Name column
            self.enable_action_buttons()

    def on_checkbox_changed(self):

        self.enable_action_buttons()

    def open_profile_dialog(self):

        dialog = ProfileDialog(self)

        dialog.deleteRequested.connect(self.handle_delete_profile)

        if dialog.exec():
            try:
                self.ui.NameOfProfile.setText(dialog.profile_name)

                if dialog.save_profile:
                    self.pm.add_profile(dialog.profile_path, dialog.profile_name)

                self.engine.load_printer_profile(dialog.profile_path)

            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load ICC profile: {e}")
                self.ui.NameOfProfile.clear()
                self.engine.unload_printer_profile()

    def update_profile_name_and_load_profile(self):

        saved = self.pm.current_profile()

        if saved is None:
            return

        metrics = QFontMetrics(self.ui.NameOfProfile.font())
        text = metrics.elidedText(
            saved["name"],
            Qt.TextElideMode.ElideRight,
            self.ui.NameOfProfile.contentsRect().width()
        )
        self.ui.NameOfProfile.setText(text)
        self.engine.load_printer_profile(saved["path"])

    def handle_delete_profile(self, name):

        current = self.pm.current_profile()

        if current and current["name"] == name:

            self.engine.unload_printer_profile()
            self.ui.NameOfProfile.clear()

        self.pm.remove_profile(name)
