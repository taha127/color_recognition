# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QFrame,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(996, 660)
        Widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalGroupBox_3 = QGroupBox(Widget)
        self.verticalGroupBox_3.setObjectName(u"verticalGroupBox_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalGroupBox_3.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.verticalGroupBox_3.setFont(font)
        self.verticalGroupBox_3.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.verticalGroupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scancolortab = QTabWidget(self.verticalGroupBox_3)
        self.scancolortab.setObjectName(u"scancolortab")
        self.scancolortab.setStyleSheet(u"")
        self.scancolortab.setDocumentMode(True)
        self.scancolortab.setTabsClosable(False)
        self.scancolortab.setMovable(False)
        self.scancolortab.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formsavecolor = QGroupBox(self.tab)
        self.formsavecolor.setObjectName(u"formsavecolor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.formsavecolor.sizePolicy().hasHeightForWidth())
        self.formsavecolor.setSizePolicy(sizePolicy1)
        self.formsavecolor.setMouseTracking(False)
        self.formsavecolor.setTabletTracking(False)
        self.formsavecolor.setAcceptDrops(False)
        self.formsavecolor.setStyleSheet(u"#formsavecolor{\n"
"padding: 3px;\n"
"\n"
"}")
        self.formLayout = QFormLayout(self.formsavecolor)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.formsavecolor)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.ColorRecognationLabel = QLabel(self.formsavecolor)
        self.ColorRecognationLabel.setObjectName(u"ColorRecognationLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.ColorRecognationLabel)

        self.label_3 = QLabel(self.formsavecolor)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.NameColorIn = QLineEdit(self.formsavecolor)
        self.NameColorIn.setObjectName(u"NameColorIn")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.NameColorIn)

        self.SaveColorBtn = QPushButton(self.formsavecolor)
        self.SaveColorBtn.setObjectName(u"SaveColorBtn")
        self.SaveColorBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SaveColorBtn.setStyleSheet(u"#SaveColorBtn {\n"
"background-color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 4px;\n"
"padding: 3px 3px;\n"
"margin-bottom: 5px;\n"
"}\n"
"#SaveColorBtn:hover {\n"
"background-color: rgb(115, 115, 115);\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.SaveColorBtn)


        self.verticalLayout_2.addWidget(self.formsavecolor)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.scancolortab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.SavedColorTable = QTableWidget(self.tab_2)
        if (self.SavedColorTable.columnCount() < 5):
            self.SavedColorTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.SavedColorTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.SavedColorTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.SavedColorTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.SavedColorTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.SavedColorTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.SavedColorTable.setObjectName(u"SavedColorTable")
        self.SavedColorTable.setFrameShape(QFrame.Shape.Panel)
        self.SavedColorTable.setFrameShadow(QFrame.Shadow.Raised)
        self.SavedColorTable.setShowGrid(True)
        self.SavedColorTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.SavedColorTable.setSortingEnabled(False)
        self.SavedColorTable.setWordWrap(True)
        self.SavedColorTable.setCornerButtonEnabled(True)
        self.SavedColorTable.setRowCount(0)
        self.SavedColorTable.horizontalHeader().setVisible(True)
        self.SavedColorTable.horizontalHeader().setCascadingSectionResizes(False)
        self.SavedColorTable.horizontalHeader().setDefaultSectionSize(98)
        self.SavedColorTable.horizontalHeader().setStretchLastSection(True)
        self.SavedColorTable.verticalHeader().setVisible(False)
        self.SavedColorTable.verticalHeader().setCascadingSectionResizes(False)
        self.SavedColorTable.verticalHeader().setDefaultSectionSize(39)
        self.SavedColorTable.verticalHeader().setProperty(u"showSortIndicator", False)
        self.SavedColorTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_6.addWidget(self.SavedColorTable)

        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.SaveActBtn = QPushButton(self.groupBox)
        self.SaveActBtn.setObjectName(u"SaveActBtn")
        self.SaveActBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SaveActBtn.setStyleSheet(u"#SaveActBtn {\n"
"background-color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 4px;\n"
"padding: 3px 3px;\n"
"margin-bottom: 5px;\n"
"}\n"
"#SaveActBtn:hover {\n"
"background-color: rgb(115, 115, 115);\n"
"}")

        self.horizontalLayout_2.addWidget(self.SaveActBtn)

        self.RstBtn = QPushButton(self.groupBox)
        self.RstBtn.setObjectName(u"RstBtn")
        self.RstBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.RstBtn.setStyleSheet(u"#RstBtn {\n"
"background-color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 4px;\n"
"padding: 3px 3px;\n"
"margin-bottom: 5px;\n"
"}\n"
"#RstBtn:hover {\n"
"background-color: rgb(115, 115, 115);\n"
"}")

        self.horizontalLayout_2.addWidget(self.RstBtn)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.scancolortab.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.scancolortab)


        self.gridLayout.addWidget(self.verticalGroupBox_3, 0, 0, 1, 1)

        self.verticalGroupBox_2 = QGroupBox(Widget)
        self.verticalGroupBox_2.setObjectName(u"verticalGroupBox_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalGroupBox_2.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_2.setSizePolicy(sizePolicy2)
        self.verticalGroupBox_2.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 1)
        self.CameraScan = QGraphicsView(self.verticalGroupBox_2)
        self.CameraScan.setObjectName(u"CameraScan")
        font1 = QFont()
        font1.setBold(False)
        self.CameraScan.setFont(font1)
        self.CameraScan.setStyleSheet(u"")
        self.CameraScan.setFrameShape(QFrame.Shape.Panel)
        self.CameraScan.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CameraScan.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CameraScan.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.CameraScan.setResizeAnchor(QGraphicsView.ViewportAnchor.NoAnchor)

        self.verticalLayout_4.addWidget(self.CameraScan)

        self.TakePhotoBtn = QPushButton(self.verticalGroupBox_2)
        self.TakePhotoBtn.setObjectName(u"TakePhotoBtn")
        self.TakePhotoBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.TakePhotoBtn.setStyleSheet(u"#TakePhotoBtn{\n"
"background-color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 10px 14px;\n"
"}\n"
"\n"
"#TakePhotoBtn:hover {\n"
"background-color: rgb(115, 115, 115);\n"
"}")

        self.verticalLayout_4.addWidget(self.TakePhotoBtn)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.CancelBtn = QPushButton(self.verticalGroupBox_2)
        self.CancelBtn.setObjectName(u"CancelBtn")
        self.CancelBtn.setEnabled(True)
        self.CancelBtn.setFont(font1)
        self.CancelBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CancelBtn.setStyleSheet(u"#CancelBtn{\n"
"background-color: rgb(170, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 10px 14px;\n"
"margin-bottom: 5px;\n"
"}\n"
"#CancelBtn:hover {\n"
"background-color: rgb(140, 0, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.CancelBtn)

        self.ScanBtn = QPushButton(self.verticalGroupBox_2)
        self.ScanBtn.setObjectName(u"ScanBtn")
        self.ScanBtn.setEnabled(True)
        self.ScanBtn.setFont(font1)
        self.ScanBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ScanBtn.setStyleSheet(u"#ScanBtn {\n"
"background-color: rgb(0, 85, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 10px 14px;\n"
"margin-bottom: 5px;\n"
"}\n"
"#ScanBtn:hover {\n"
"background-color: rgb(0, 75, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.ScanBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.verticalGroupBox_2, 0, 1, 1, 1)

        self.verticalGroupBox = QGroupBox(Widget)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.verticalGroupBox.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox.setSizePolicy(sizePolicy3)
        self.verticalGroupBox.setFont(font)
        self.verticalGroupBox.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.verticalGroupBox.setToolTipDuration(-15)
        self.verticalGroupBox.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SettingsBtn = QPushButton(self.verticalGroupBox)
        self.SettingsBtn.setObjectName(u"SettingsBtn")
        self.SettingsBtn.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.SettingsBtn.sizePolicy().hasHeightForWidth())
        self.SettingsBtn.setSizePolicy(sizePolicy4)
        self.SettingsBtn.setFont(font1)
        self.SettingsBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SettingsBtn.setStyleSheet(u"#SettingsBtn{\n"
"background-color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 10px 10px;\n"
"}\n"
"\n"
"#SettingsBtn:hover {\n"
"background-color: rgb(115, 115, 115);\n"
"}")

        self.verticalLayout_3.addWidget(self.SettingsBtn)

        self.CalibrateBtn_2 = QPushButton(self.verticalGroupBox)
        self.CalibrateBtn_2.setObjectName(u"CalibrateBtn_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.CalibrateBtn_2.sizePolicy().hasHeightForWidth())
        self.CalibrateBtn_2.setSizePolicy(sizePolicy5)
        self.CalibrateBtn_2.setFont(font1)
        self.CalibrateBtn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CalibrateBtn_2.setStyleSheet(u"#CalibrateBtn_2{\n"
"background-color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 10px 10px;\n"
"}\n"
"\n"
"#CalibrateBtn_2:hover {\n"
"background-color: rgb(115, 115, 115);\n"
"}")

        self.verticalLayout_3.addWidget(self.CalibrateBtn_2)

        self.SendFeedBackBtn = QPushButton(self.verticalGroupBox)
        self.SendFeedBackBtn.setObjectName(u"SendFeedBackBtn")
        sizePolicy5.setHeightForWidth(self.SendFeedBackBtn.sizePolicy().hasHeightForWidth())
        self.SendFeedBackBtn.setSizePolicy(sizePolicy5)
        self.SendFeedBackBtn.setFont(font1)
        self.SendFeedBackBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SendFeedBackBtn.setStyleSheet(u"#SendFeedBackBtn{\n"
"background-color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 10px 10px;\n"
"}\n"
"\n"
"#SendFeedBackBtn:hover {\n"
"background-color: rgb(115, 115, 115);\n"
"}")

        self.verticalLayout_3.addWidget(self.SendFeedBackBtn)

        self.HelpBtn = QPushButton(self.verticalGroupBox)
        self.HelpBtn.setObjectName(u"HelpBtn")
        sizePolicy5.setHeightForWidth(self.HelpBtn.sizePolicy().hasHeightForWidth())
        self.HelpBtn.setSizePolicy(sizePolicy5)
        self.HelpBtn.setFont(font1)
        self.HelpBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.HelpBtn.setStyleSheet(u"#HelpBtn{\n"
"background-color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 10px 10px;\n"
"}\n"
"\n"
"#HelpBtn:hover {\n"
"background-color: rgb(115, 115, 115);\n"
"}")

        self.verticalLayout_3.addWidget(self.HelpBtn)

        self.AboutSoftBtn = QPushButton(self.verticalGroupBox)
        self.AboutSoftBtn.setObjectName(u"AboutSoftBtn")
        sizePolicy5.setHeightForWidth(self.AboutSoftBtn.sizePolicy().hasHeightForWidth())
        self.AboutSoftBtn.setSizePolicy(sizePolicy5)
        self.AboutSoftBtn.setFont(font1)
        self.AboutSoftBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.AboutSoftBtn.setStyleSheet(u"#AboutSoftBtn{\n"
"background-color: rgb(135, 135, 135);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 10px 10px;\n"
"}\n"
"\n"
"#AboutSoftBtn:hover {\n"
"background-color: rgb(115, 115, 115);\n"
"}")
        self.AboutSoftBtn.setAutoDefault(False)
        self.AboutSoftBtn.setFlat(False)

        self.verticalLayout_3.addWidget(self.AboutSoftBtn)

        self.groupBox_2 = QGroupBox(self.verticalGroupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.NameOfProfile = QLabel(self.groupBox_2)
        self.NameOfProfile.setObjectName(u"NameOfProfile")

        self.verticalLayout.addWidget(self.NameOfProfile)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.verticalGroupBox, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 1)

        self.retranslateUi(Widget)

        self.scancolortab.setCurrentIndex(0)
        self.AboutSoftBtn.setDefault(False)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.verticalGroupBox_3.setTitle(QCoreApplication.translate("Widget", u"Operations", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Color:", None))
        self.ColorRecognationLabel.setText(QCoreApplication.translate("Widget", u"-------------", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Name:", None))
        self.SaveColorBtn.setText(QCoreApplication.translate("Widget", u"\u2705Save", None))
        self.scancolortab.setTabText(self.scancolortab.indexOf(self.tab), QCoreApplication.translate("Widget", u"Scaned Colors", None))
        ___qtablewidgetitem = self.SavedColorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Row", None));
        ___qtablewidgetitem1 = self.SavedColorTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Name", None));
        ___qtablewidgetitem2 = self.SavedColorTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Color", None));
        ___qtablewidgetitem3 = self.SavedColorTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Date", None));
        ___qtablewidgetitem4 = self.SavedColorTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"Delete", None));
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Actions", None))
        self.SaveActBtn.setText(QCoreApplication.translate("Widget", u"Save", None))
        self.RstBtn.setText(QCoreApplication.translate("Widget", u"Reset", None))
        self.scancolortab.setTabText(self.scancolortab.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"Saved colors", None))
        self.verticalGroupBox_2.setTitle(QCoreApplication.translate("Widget", u"Scan Color", None))
        self.TakePhotoBtn.setText(QCoreApplication.translate("Widget", u"Take Photo", None))
        self.CancelBtn.setText(QCoreApplication.translate("Widget", u"Cancel", None))
        self.ScanBtn.setText(QCoreApplication.translate("Widget", u"Start Scan", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("Widget", u"ToolBar", None))
        self.SettingsBtn.setText(QCoreApplication.translate("Widget", u"Settings", None))
        self.CalibrateBtn_2.setText(QCoreApplication.translate("Widget", u"Calibrate", None))
        self.SendFeedBackBtn.setText(QCoreApplication.translate("Widget", u"Send Feedback", None))
        self.HelpBtn.setText(QCoreApplication.translate("Widget", u"Help", None))
        self.AboutSoftBtn.setText(QCoreApplication.translate("Widget", u"About Software", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Calibrated Profile", None))
        self.NameOfProfile.setText(QCoreApplication.translate("Widget", u"---------", None))
    # retranslateUi

