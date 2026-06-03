# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibration.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGraphicsView, QGroupBox,
    QHBoxLayout, QHeaderView, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Calibration_window(object):
    def setupUi(self, Calibration_window):
        if not Calibration_window.objectName():
            Calibration_window.setObjectName(u"Calibration_window")
        Calibration_window.resize(1114, 688)
        self.centralwidget = QWidget(Calibration_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CalibratedColorsTable = QTableWidget(self.groupBox)
        if (self.CalibratedColorsTable.columnCount() < 3):
            self.CalibratedColorsTable.setColumnCount(3)
        font = QFont()
        font.setPointSize(11)
        font.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.CalibratedColorsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.CalibratedColorsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.CalibratedColorsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.CalibratedColorsTable.setObjectName(u"CalibratedColorsTable")
        self.CalibratedColorsTable.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.CalibratedColorsTable.setSortingEnabled(False)
        self.CalibratedColorsTable.setRowCount(0)
        self.CalibratedColorsTable.setColumnCount(3)
        self.CalibratedColorsTable.horizontalHeader().setVisible(True)
        self.CalibratedColorsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.CalibratedColorsTable.horizontalHeader().setMinimumSectionSize(50)
        self.CalibratedColorsTable.horizontalHeader().setDefaultSectionSize(70)
        self.CalibratedColorsTable.horizontalHeader().setHighlightSections(False)
        self.CalibratedColorsTable.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.CalibratedColorsTable.horizontalHeader().setStretchLastSection(True)
        self.CalibratedColorsTable.verticalHeader().setVisible(False)
        self.CalibratedColorsTable.verticalHeader().setCascadingSectionResizes(False)
        self.CalibratedColorsTable.verticalHeader().setProperty(u"showSortIndicator", False)
        self.CalibratedColorsTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.CalibratedColorsTable)

        self.NamePrflineEdit = QLineEdit(self.groupBox)
        self.NamePrflineEdit.setObjectName(u"NamePrflineEdit")

        self.verticalLayout_3.addWidget(self.NamePrflineEdit)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.SaveButton = QPushButton(self.groupBox)
        self.SaveButton.setObjectName(u"SaveButton")

        self.horizontalLayout_7.addWidget(self.SaveButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CameraScan = QGraphicsView(self.groupBox_3)
        self.CameraScan.setObjectName(u"CameraScan")
        self.CameraScan.setStyleSheet(u"")
        self.CameraScan.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CameraScan.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CameraScan.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        self.verticalLayout.addWidget(self.CameraScan)

        self.TakePhotoBtn = QPushButton(self.groupBox_3)
        self.TakePhotoBtn.setObjectName(u"TakePhotoBtn")

        self.verticalLayout.addWidget(self.TakePhotoBtn)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CodeIn = QLineEdit(self.groupBox_3)
        self.CodeIn.setObjectName(u"CodeIn")

        self.horizontalLayout_3.addWidget(self.CodeIn)

        self.PickColorBtn = QPushButton(self.groupBox_3)
        self.PickColorBtn.setObjectName(u"PickColorBtn")

        self.horizontalLayout_3.addWidget(self.PickColorBtn)

        self.horizontalLayout_3.setStretch(0, 99)
        self.horizontalLayout_3.setStretch(1, 100)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.OkBtn = QPushButton(self.groupBox_3)
        self.OkBtn.setObjectName(u"OkBtn")

        self.horizontalLayout_2.addWidget(self.OkBtn)

        self.CancelBtn = QPushButton(self.groupBox_3)
        self.CancelBtn.setObjectName(u"CancelBtn")

        self.horizontalLayout_2.addWidget(self.CancelBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.PrfTable = QTableWidget(self.groupBox_2)
        if (self.PrfTable.columnCount() < 5):
            self.PrfTable.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.PrfTable.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.PrfTable.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.PrfTable.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.PrfTable.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.PrfTable.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        self.PrfTable.setObjectName(u"PrfTable")
        self.PrfTable.horizontalHeader().setCascadingSectionResizes(False)
        self.PrfTable.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.PrfTable.horizontalHeader().setStretchLastSection(True)
        self.PrfTable.verticalHeader().setVisible(False)
        self.PrfTable.verticalHeader().setCascadingSectionResizes(False)
        self.PrfTable.verticalHeader().setHighlightSections(True)
        self.PrfTable.verticalHeader().setProperty(u"showSortIndicator", False)
        self.PrfTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.PrfTable)

        self.CountinueBtn = QPushButton(self.groupBox_2)
        self.CountinueBtn.setObjectName(u"CountinueBtn")

        self.verticalLayout_4.addWidget(self.CountinueBtn)


        self.horizontalLayout_4.addWidget(self.groupBox_2)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 10)
        self.horizontalLayout_4.setStretch(2, 6)
        Calibration_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Calibration_window)

        QMetaObject.connectSlotsByName(Calibration_window)
    # setupUi

    def retranslateUi(self, Calibration_window):
        Calibration_window.setWindowTitle(QCoreApplication.translate("Calibration_window", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("Calibration_window", u"Calibrated colors", None))
        ___qtablewidgetitem = self.CalibratedColorsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Calibration_window", u"Row", None));
        ___qtablewidgetitem1 = self.CalibratedColorsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Calibration_window", u"Color", None));
        ___qtablewidgetitem2 = self.CalibratedColorsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Calibration_window", u"Delete", None));
        self.NamePrflineEdit.setInputMask("")
        self.NamePrflineEdit.setText("")
        self.NamePrflineEdit.setPlaceholderText(QCoreApplication.translate("Calibration_window", u"name:", None))
        self.SaveButton.setText(QCoreApplication.translate("Calibration_window", u"Save", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Calibration_window", u"Calibrated part", None))
        self.TakePhotoBtn.setText(QCoreApplication.translate("Calibration_window", u"Take Photo", None))
        self.CodeIn.setText("")
        self.CodeIn.setPlaceholderText(QCoreApplication.translate("Calibration_window", u"code:", None))
        self.PickColorBtn.setText(QCoreApplication.translate("Calibration_window", u"Pick Color", None))
        self.OkBtn.setText(QCoreApplication.translate("Calibration_window", u"OK", None))
        self.CancelBtn.setText(QCoreApplication.translate("Calibration_window", u"Cancel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Calibration_window", u"Calibrated profiles", None))
        ___qtablewidgetitem3 = self.PrfTable.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Calibration_window", u"Name", None));
        ___qtablewidgetitem4 = self.PrfTable.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Calibration_window", u"Colors", None));
        ___qtablewidgetitem5 = self.PrfTable.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Calibration_window", u"Creation Date", None));
        ___qtablewidgetitem6 = self.PrfTable.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Calibration_window", u"Select", None));
        ___qtablewidgetitem7 = self.PrfTable.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Calibration_window", u"Delete", None));
        self.CountinueBtn.setText(QCoreApplication.translate("Calibration_window", u"Continue", None))
    # retranslateUi

