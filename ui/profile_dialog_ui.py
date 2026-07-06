# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QDialog, QDialogButtonBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.NoProfilesLabel = QLabel(Dialog)
        self.NoProfilesLabel.setObjectName(u"NoProfilesLabel")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.NoProfilesLabel.setFont(font)
        self.NoProfilesLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.NoProfilesLabel.setAutoFillBackground(False)
        self.NoProfilesLabel.setStyleSheet(u"")
        self.NoProfilesLabel.setScaledContents(False)
        self.NoProfilesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.NoProfilesLabel)

        self.RecentProfilesTree = QTreeWidget(Dialog)
        self.RecentProfilesTree.setObjectName(u"RecentProfilesTree")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RecentProfilesTree.sizePolicy().hasHeightForWidth())
        self.RecentProfilesTree.setSizePolicy(sizePolicy)
        self.RecentProfilesTree.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.RecentProfilesTree.setStyleSheet(u"#RecentProfilesTree{\n"
"background-color: rgba(68, 55, 255, 0);\n"
"border: 0px;\n"
"}\n"
"#RecentProfilesTree::item{\n"
"padding-top: 6px;\n"
"padding-bottom: 6px; \n"
"}\n"
"")
        self.RecentProfilesTree.setLineWidth(1)
        self.RecentProfilesTree.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.RecentProfilesTree.setAlternatingRowColors(False)
        self.RecentProfilesTree.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.RecentProfilesTree.setUniformRowHeights(False)
        self.RecentProfilesTree.setSortingEnabled(False)
        self.RecentProfilesTree.setAnimated(False)
        self.RecentProfilesTree.setAllColumnsShowFocus(False)
        self.RecentProfilesTree.setWordWrap(False)
        self.RecentProfilesTree.setColumnCount(2)
        self.RecentProfilesTree.header().setVisible(False)
        self.RecentProfilesTree.header().setCascadingSectionResizes(False)
        self.RecentProfilesTree.header().setMinimumSectionSize(36)
        self.RecentProfilesTree.header().setDefaultSectionSize(120)
        self.RecentProfilesTree.header().setHighlightSections(False)
        self.RecentProfilesTree.header().setProperty(u"showSortIndicator", False)
        self.RecentProfilesTree.header().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.RecentProfilesTree)

        self.DeleteButton = QPushButton(Dialog)
        self.DeleteButton.setObjectName(u"DeleteButton")

        self.verticalLayout.addWidget(self.DeleteButton)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 3, 0, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.ProfileAddressLabel = QLabel(Dialog)
        self.ProfileAddressLabel.setObjectName(u"ProfileAddressLabel")

        self.horizontalLayout_8.addWidget(self.ProfileAddressLabel)

        self.AddressProfile = QLineEdit(Dialog)
        self.AddressProfile.setObjectName(u"AddressProfile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AddressProfile.sizePolicy().hasHeightForWidth())
        self.AddressProfile.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.AddressProfile)

        self.BrowseButton = QPushButton(Dialog)
        self.BrowseButton.setObjectName(u"BrowseButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.BrowseButton.sizePolicy().hasHeightForWidth())
        self.BrowseButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.BrowseButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ProfileNamelabel = QLabel(Dialog)
        self.ProfileNamelabel.setObjectName(u"ProfileNamelabel")

        self.horizontalLayout_7.addWidget(self.ProfileNamelabel)

        self.NameProfilelineEdit = QLineEdit(Dialog)
        self.NameProfilelineEdit.setObjectName(u"NameProfilelineEdit")

        self.horizontalLayout_7.addWidget(self.NameProfilelineEdit)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.SaveCheckBox = QCheckBox(Dialog)
        self.SaveCheckBox.setObjectName(u"SaveCheckBox")

        self.verticalLayout_2.addWidget(self.SaveCheckBox)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Select Profile", None))
        self.NoProfilesLabel.setText(QCoreApplication.translate("Dialog", u"No saved profiles", None))
        ___qtreewidgetitem = self.RecentProfilesTree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Dialog", u"2", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dialog", u"1", None));
        self.DeleteButton.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.ProfileAddressLabel.setText(QCoreApplication.translate("Dialog", u"Profile Address:", None))
        self.BrowseButton.setText(QCoreApplication.translate("Dialog", u"Browse", None))
        self.ProfileNamelabel.setText(QCoreApplication.translate("Dialog", u"Profile Name:", None))
        self.SaveCheckBox.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

