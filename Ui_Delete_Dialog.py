# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Delete_Dialog.ui'
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

class Ui_DeleteDialog(object):
    def setupUi(self, DeleteDialog):
        if not DeleteDialog.objectName():
            DeleteDialog.setObjectName(u"DeleteDialog")
        DeleteDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        DeleteDialog.resize(275, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeleteDialog.sizePolicy().hasHeightForWidth())
        DeleteDialog.setSizePolicy(sizePolicy)
        DeleteDialog.setMinimumSize(QSize(275, 100))
        DeleteDialog.setMaximumSize(QSize(275, 100))
        self.verticalLayout_2 = QVBoxLayout(DeleteDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelDelete = QLabel(DeleteDialog)
        self.labelDelete.setObjectName(u"labelDelete")
        self.labelDelete.setStyleSheet(u"color: red;")

        self.verticalLayout.addWidget(self.labelDelete, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushDiscard = QPushButton(DeleteDialog)
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

        self.pushAccept = QPushButton(DeleteDialog)
        self.pushAccept.setObjectName(u"pushAccept")
        self.pushAccept.setStyleSheet(u"QPushButton{\n"
"	background-color: green;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(20, 150, 0);\n"
"}")
        self.pushAccept.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pushAccept)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(DeleteDialog)

        self.pushAccept.setDefault(True)


        QMetaObject.connectSlotsByName(DeleteDialog)
    # setupUi

    def retranslateUi(self, DeleteDialog):
        DeleteDialog.setWindowTitle(QCoreApplication.translate("DeleteDialog", u"Planet l\u00f6schen?", None))
        self.labelDelete.setText(QCoreApplication.translate("DeleteDialog", u"Element l\u00f6schen?", None))
        self.pushDiscard.setText(QCoreApplication.translate("DeleteDialog", u"Abbrechen", None))
        self.pushAccept.setText(QCoreApplication.translate("DeleteDialog", u"L\u00f6schen", None))
    # retranslateUi

