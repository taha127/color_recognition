# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'activate_license_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ActivateLicenseDialog(object):
    def setupUi(self, ActivateLicenseDialog):
        if not ActivateLicenseDialog.objectName():
            ActivateLicenseDialog.setObjectName(u"ActivateLicenseDialog")
        ActivateLicenseDialog.resize(480, 180)
        self.verticalLayout = QVBoxLayout(ActivateLicenseDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.InfoLabel = QLabel(ActivateLicenseDialog)
        self.InfoLabel.setObjectName(u"InfoLabel")

        self.verticalLayout.addWidget(self.InfoLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 30)
        self.LicenseKeyLabel = QLabel(ActivateLicenseDialog)
        self.LicenseKeyLabel.setObjectName(u"LicenseKeyLabel")

        self.horizontalLayout.addWidget(self.LicenseKeyLabel)

        self.LicenseKeyLineEdit = QLineEdit(ActivateLicenseDialog)
        self.LicenseKeyLineEdit.setObjectName(u"LicenseKeyLineEdit")

        self.horizontalLayout.addWidget(self.LicenseKeyLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ActivateButton = QPushButton(ActivateLicenseDialog)
        self.ActivateButton.setObjectName(u"ActivateButton")

        self.horizontalLayout_2.addWidget(self.ActivateButton)

        self.ExitButton = QPushButton(ActivateLicenseDialog)
        self.ExitButton.setObjectName(u"ExitButton")

        self.horizontalLayout_2.addWidget(self.ExitButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ActivateLicenseDialog)

        QMetaObject.connectSlotsByName(ActivateLicenseDialog)
    # setupUi

    def retranslateUi(self, ActivateLicenseDialog):
        ActivateLicenseDialog.setWindowTitle(QCoreApplication.translate("ActivateLicenseDialog", u"Activate License", None))
        self.InfoLabel.setText(QCoreApplication.translate("ActivateLicenseDialog", u"Please enter your License key and click activate.", None))
        self.LicenseKeyLabel.setText(QCoreApplication.translate("ActivateLicenseDialog", u"License Key:", None))
        self.ActivateButton.setText(QCoreApplication.translate("ActivateLicenseDialog", u"Activate", None))
        self.ExitButton.setText(QCoreApplication.translate("ActivateLicenseDialog", u"Exit", None))
    # retranslateUi

