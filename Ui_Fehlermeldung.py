# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Fehlermeldung.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Fehlermeldung(object):
    def setupUi(self, Fehlermeldung):
        if not Fehlermeldung.objectName():
            Fehlermeldung.setObjectName(u"Fehlermeldung")
        Fehlermeldung.setWindowModality(Qt.WindowModality.ApplicationModal)
        Fehlermeldung.resize(200, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Fehlermeldung.sizePolicy().hasHeightForWidth())
        Fehlermeldung.setSizePolicy(sizePolicy)
        Fehlermeldung.setMinimumSize(QSize(200, 100))
        Fehlermeldung.setMaximumSize(QSize(200, 100))
        self.verticalLayout_2 = QVBoxLayout(Fehlermeldung)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelDelete = QLabel(Fehlermeldung)
        self.labelDelete.setObjectName(u"labelDelete")
        self.labelDelete.setStyleSheet(u"color: red;")

        self.verticalLayout.addWidget(self.labelDelete, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushDiscard = QPushButton(Fehlermeldung)
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


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Fehlermeldung)

        QMetaObject.connectSlotsByName(Fehlermeldung)
    # setupUi

    def retranslateUi(self, Fehlermeldung):
        Fehlermeldung.setWindowTitle(QCoreApplication.translate("Fehlermeldung", u"Fehlermeldung", None))
        self.labelDelete.setText(QCoreApplication.translate("Fehlermeldung", u"Fehlermeldung", None))
        self.pushDiscard.setText(QCoreApplication.translate("Fehlermeldung", u"Ok", None))
    # retranslateUi

