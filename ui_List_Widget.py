# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_List_Widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(700, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(700, 500))
        Dialog.setMaximumSize(QSize(700, 500))
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(100, 20))

        self.verticalLayout.addWidget(self.textEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(50, 0))
        self.spinBox.setMaximumSize(QSize(50, 16777215))
        self.spinBox.setMaximum(999)

        self.verticalLayout.addWidget(self.spinBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_2 = QSpinBox(Dialog)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(50, 0))
        self.spinBox_2.setMaximumSize(QSize(50, 16777215))
        self.spinBox_2.setSingleStep(1)

        self.verticalLayout.addWidget(self.spinBox_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinBox_3 = QSpinBox(Dialog)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimumSize(QSize(50, 0))
        self.spinBox_3.setMaximumSize(QSize(100, 16777215))
        self.spinBox_3.setMinimum(0)
        self.spinBox_3.setMaximum(359)

        self.verticalLayout.addWidget(self.spinBox_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(1000, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(34, 204, 31);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(89, 255, 0);\n"
"}")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(197, 2, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 53, 0)\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(197, 2, 0);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 53, 0)\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_3)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Element Auswahl", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Neues Element", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Kennzeichnung", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Aktiv", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Masse in kg", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"v in M/s", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Winkel in Grad", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u00dcbernehmen", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"L\u00f6schen", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Abbrechen", None))
    # retranslateUi

