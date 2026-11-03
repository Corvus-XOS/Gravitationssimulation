# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Name_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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

class Ui_NameDialog(object):
    def setupUi(self, NameDialog):
        if not NameDialog.objectName():
            NameDialog.setObjectName(u"NameDialog")
        NameDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        NameDialog.resize(275, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NameDialog.sizePolicy().hasHeightForWidth())
        NameDialog.setSizePolicy(sizePolicy)
        NameDialog.setMinimumSize(QSize(275, 150))
        NameDialog.setMaximumSize(QSize(275, 150))
        self.verticalLayout_2 = QVBoxLayout(NameDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelName = QLabel(NameDialog)
        self.labelName.setObjectName(u"labelName")
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.labelName, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lineName = QLineEdit(NameDialog)
        self.lineName.setObjectName(u"lineName")

        self.verticalLayout.addWidget(self.lineName, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelError = QLabel(NameDialog)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setStyleSheet(u"color: red;")

        self.verticalLayout.addWidget(self.labelError, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushDiscard = QPushButton(NameDialog)
        self.pushDiscard.setObjectName(u"pushDiscard")
        self.pushDiscard.setStyleSheet(u"QPushButton{\n"
"	background-color: red;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(150, 20, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.pushDiscard)

        self.pushAccept = QPushButton(NameDialog)
        self.pushAccept.setObjectName(u"pushAccept")
        self.pushAccept.setStyleSheet(u"QPushButton{\n"
"	background-color: green;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(20, 150, 0);\n"
"}")
        self.pushAccept.setCheckable(False)
        self.pushAccept.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pushAccept)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(NameDialog)

        self.pushAccept.setDefault(True)


        QMetaObject.connectSlotsByName(NameDialog)
    # setupUi

    def retranslateUi(self, NameDialog):
        NameDialog.setWindowTitle(QCoreApplication.translate("NameDialog", u"Bezeichnung Planet", None))
        self.labelName.setText(QCoreApplication.translate("NameDialog", u"Bezeichnung f\u00fcr Planeten festlegen", None))
        self.labelError.setText("")
        self.pushDiscard.setText(QCoreApplication.translate("NameDialog", u"Abbrechen", None))
        self.pushAccept.setText(QCoreApplication.translate("NameDialog", u"\u00dcbernehmen", None))
    # retranslateUi

