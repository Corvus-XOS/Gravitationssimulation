# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Name_Screenshot.ui'
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

class Ui_NameScreenshot(object):
    def setupUi(self, NameScreenshot):
        if not NameScreenshot.objectName():
            NameScreenshot.setObjectName(u"NameScreenshot")
        NameScreenshot.setWindowModality(Qt.WindowModality.ApplicationModal)
        NameScreenshot.resize(275, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NameScreenshot.sizePolicy().hasHeightForWidth())
        NameScreenshot.setSizePolicy(sizePolicy)
        NameScreenshot.setMinimumSize(QSize(275, 150))
        NameScreenshot.setMaximumSize(QSize(275, 150))
        self.verticalLayout_2 = QVBoxLayout(NameScreenshot)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelName = QLabel(NameScreenshot)
        self.labelName.setObjectName(u"labelName")
        sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
        self.labelName.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.labelName, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.lineName = QLineEdit(NameScreenshot)
        self.lineName.setObjectName(u"lineName")
        self.lineName.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout.addWidget(self.lineName, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelError = QLabel(NameScreenshot)
        self.labelError.setObjectName(u"labelError")
        self.labelError.setStyleSheet(u"color: red;")

        self.verticalLayout.addWidget(self.labelError, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushDiscard = QPushButton(NameScreenshot)
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

        self.pushAccept = QPushButton(NameScreenshot)
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


        self.retranslateUi(NameScreenshot)

        self.pushAccept.setDefault(True)


        QMetaObject.connectSlotsByName(NameScreenshot)
    # setupUi

    def retranslateUi(self, NameScreenshot):
        NameScreenshot.setWindowTitle(QCoreApplication.translate("NameScreenshot", u"Name Screenshot", None))
        self.labelName.setText(QCoreApplication.translate("NameScreenshot", u"Name f\u00fcr Screenshot festlegen", None))
        self.labelError.setText("")
        self.pushDiscard.setText(QCoreApplication.translate("NameScreenshot", u"Abbrechen", None))
        self.pushAccept.setText(QCoreApplication.translate("NameScreenshot", u"\u00dcbernehmen", None))
    # retranslateUi

