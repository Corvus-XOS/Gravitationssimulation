# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDockWidget, QDoubleSpinBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 850)
        MainWindow.setMinimumSize(QSize(850, 850))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.actionStart_Stop = QAction(MainWindow)
        self.actionStart_Stop.setObjectName(u"actionStart_Stop")
        icon = QIcon(QIcon.fromTheme(u"media-playback-start"))
        self.actionStart_Stop.setIcon(icon)
        self.actionGithub_Repo = QAction(MainWindow)
        self.actionGithub_Repo.setObjectName(u"actionGithub_Repo")
        icon1 = QIcon(QIcon.fromTheme(u"applications-development"))
        self.actionGithub_Repo.setIcon(icon1)
        self.actionWas_macht_dieser_Link = QAction(MainWindow)
        self.actionWas_macht_dieser_Link.setObjectName(u"actionWas_macht_dieser_Link")
        icon2 = QIcon(QIcon.fromTheme(u"dialog-question"))
        self.actionWas_macht_dieser_Link.setIcon(icon2)
        self.actionDock = QAction(MainWindow)
        self.actionDock.setObjectName(u"actionDock")
        icon3 = QIcon(QIcon.fromTheme(u"applications-system"))
        self.actionDock.setIcon(icon3)
        self.actionAddElement = QAction(MainWindow)
        self.actionAddElement.setObjectName(u"actionAddElement")
        icon4 = QIcon(QIcon.fromTheme(u"list-add"))
        self.actionAddElement.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setEnabled(True)
        self.dockWidget.setMinimumSize(QSize(175, 802))
        self.dockWidget.setMaximumSize(QSize(175, 524287))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelElemSet = QLabel(self.dockWidgetContents)
        self.labelElemSet.setObjectName(u"labelElemSet")
        font = QFont()
        font.setBold(True)
        self.labelElemSet.setFont(font)

        self.verticalLayout.addWidget(self.labelElemSet, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_d1 = QHBoxLayout()
        self.horizontalLayout_d1.setObjectName(u"horizontalLayout_d1")
        self.pushCreate = QPushButton(self.dockWidgetContents)
        self.pushCreate.setObjectName(u"pushCreate")
        self.pushCreate.setStyleSheet(u"QPushButton{\n"
"	background-color: green;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(20, 150, 0);\n"
"}")

        self.horizontalLayout_d1.addWidget(self.pushCreate)

        self.pushDelete = QPushButton(self.dockWidgetContents)
        self.pushDelete.setObjectName(u"pushDelete")
        self.pushDelete.setStyleSheet(u"QPushButton{\n"
"	background-color: red;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(150, 20, 0);\n"
"}")

        self.horizontalLayout_d1.addWidget(self.pushDelete)


        self.verticalLayout.addLayout(self.horizontalLayout_d1)

        self.comboElement = QComboBox(self.dockWidgetContents)
        self.comboElement.setObjectName(u"comboElement")

        self.verticalLayout.addWidget(self.comboElement)

        self.checkAktiv = QCheckBox(self.dockWidgetContents)
        self.checkAktiv.setObjectName(u"checkAktiv")
        self.checkAktiv.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkAktiv.setChecked(True)

        self.verticalLayout.addWidget(self.checkAktiv, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelMass = QLabel(self.dockWidgetContents)
        self.labelMass.setObjectName(u"labelMass")
        self.labelMass.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelMass)

        self.lineEditMasse = QLineEdit(self.dockWidgetContents)
        self.lineEditMasse.setObjectName(u"lineEditMasse")
        self.lineEditMasse.setMinimumSize(QSize(100, 0))
        self.lineEditMasse.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout.addWidget(self.lineEditMasse, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelVelo = QLabel(self.dockWidgetContents)
        self.labelVelo.setObjectName(u"labelVelo")
        self.labelVelo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelVelo)

        self.spinVelo = QDoubleSpinBox(self.dockWidgetContents)
        self.spinVelo.setObjectName(u"spinVelo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinVelo.sizePolicy().hasHeightForWidth())
        self.spinVelo.setSizePolicy(sizePolicy)
        self.spinVelo.setMinimumSize(QSize(100, 0))
        self.spinVelo.setMaximumSize(QSize(100, 16777215))
        self.spinVelo.setAcceptDrops(False)
        self.spinVelo.setAutoFillBackground(False)
        self.spinVelo.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinVelo.setDecimals(6)
        self.spinVelo.setMinimum(-1000000000000.000000000000000)
        self.spinVelo.setMaximum(1000000000000.000000000000000)

        self.verticalLayout.addWidget(self.spinVelo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelDegree = QLabel(self.dockWidgetContents)
        self.labelDegree.setObjectName(u"labelDegree")
        self.labelDegree.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelDegree)

        self.spinDegree = QDoubleSpinBox(self.dockWidgetContents)
        self.spinDegree.setObjectName(u"spinDegree")
        self.spinDegree.setMinimumSize(QSize(100, 0))
        self.spinDegree.setMaximumSize(QSize(100, 16777215))
        self.spinDegree.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinDegree.setDecimals(6)
        self.spinDegree.setMinimum(-1000000000000.000000000000000)
        self.spinDegree.setMaximum(1000000000000.000000000000000)

        self.verticalLayout.addWidget(self.spinDegree, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelPos = QLabel(self.dockWidgetContents)
        self.labelPos.setObjectName(u"labelPos")

        self.verticalLayout.addWidget(self.labelPos, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_d2 = QHBoxLayout()
        self.horizontalLayout_d2.setObjectName(u"horizontalLayout_d2")
        self.labelX = QLabel(self.dockWidgetContents)
        self.labelX.setObjectName(u"labelX")
        self.labelX.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_d2.addWidget(self.labelX)

        self.spinXPos = QDoubleSpinBox(self.dockWidgetContents)
        self.spinXPos.setObjectName(u"spinXPos")
        self.spinXPos.setMinimumSize(QSize(100, 0))
        self.spinXPos.setMaximumSize(QSize(100, 16777215))
        self.spinXPos.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinXPos.setDecimals(6)
        self.spinXPos.setMinimum(-1000000000000.000000000000000)
        self.spinXPos.setMaximum(1000000000000.000000000000000)

        self.horizontalLayout_d2.addWidget(self.spinXPos)


        self.verticalLayout.addLayout(self.horizontalLayout_d2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelY = QLabel(self.dockWidgetContents)
        self.labelY.setObjectName(u"labelY")
        self.labelY.setMaximumSize(QSize(10, 16777215))

        self.horizontalLayout_3.addWidget(self.labelY)

        self.spinYPos = QDoubleSpinBox(self.dockWidgetContents)
        self.spinYPos.setObjectName(u"spinYPos")
        self.spinYPos.setMinimumSize(QSize(100, 0))
        self.spinYPos.setMaximumSize(QSize(100, 16777215))
        self.spinYPos.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinYPos.setDecimals(6)
        self.spinYPos.setMinimum(-1000000000000.000000000000000)
        self.spinYPos.setMaximum(1000000000000.000000000000000)

        self.horizontalLayout_3.addWidget(self.spinYPos)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.labelColor = QLabel(self.dockWidgetContents)
        self.labelColor.setObjectName(u"labelColor")

        self.verticalLayout.addWidget(self.labelColor, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboColor = QComboBox(self.dockWidgetContents)
        self.comboColor.setObjectName(u"comboColor")

        self.verticalLayout.addWidget(self.comboColor)

        self.pushSetElem = QPushButton(self.dockWidgetContents)
        self.pushSetElem.setObjectName(u"pushSetElem")
        self.pushSetElem.setStyleSheet(u"QPushButton{\n"
"	background-color: green;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(20, 150, 0);\n"
"}")

        self.verticalLayout.addWidget(self.pushSetElem)

        self.pushDiscElem = QPushButton(self.dockWidgetContents)
        self.pushDiscElem.setObjectName(u"pushDiscElem")
        self.pushDiscElem.setStyleSheet(u"QPushButton{\n"
"	background-color: red;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(150, 20, 0);\n"
"}")

        self.verticalLayout.addWidget(self.pushDiscElem)

        self.lineSepDock = QFrame(self.dockWidgetContents)
        self.lineSepDock.setObjectName(u"lineSepDock")
        self.lineSepDock.setFrameShape(QFrame.Shape.HLine)
        self.lineSepDock.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.lineSepDock)

        self.labelSimSet = QLabel(self.dockWidgetContents)
        self.labelSimSet.setObjectName(u"labelSimSet")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.labelSimSet.setFont(font1)

        self.verticalLayout.addWidget(self.labelSimSet, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelSteps = QLabel(self.dockWidgetContents)
        self.labelSteps.setObjectName(u"labelSteps")

        self.verticalLayout.addWidget(self.labelSteps, 0, Qt.AlignmentFlag.AlignHCenter)

        self.spinSteps = QSpinBox(self.dockWidgetContents)
        self.spinSteps.setObjectName(u"spinSteps")
        self.spinSteps.setMinimumSize(QSize(100, 0))
        self.spinSteps.setMaximumSize(QSize(100, 16777215))
        self.spinSteps.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinSteps.setMaximum(1000000000)

        self.verticalLayout.addWidget(self.spinSteps, 0, Qt.AlignmentFlag.AlignHCenter)

        self.labelAccuracy = QLabel(self.dockWidgetContents)
        self.labelAccuracy.setObjectName(u"labelAccuracy")

        self.verticalLayout.addWidget(self.labelAccuracy, 0, Qt.AlignmentFlag.AlignHCenter)

        self.doubleAccuracy = QDoubleSpinBox(self.dockWidgetContents)
        self.doubleAccuracy.setObjectName(u"doubleAccuracy")
        self.doubleAccuracy.setMinimumSize(QSize(100, 0))
        self.doubleAccuracy.setMaximumSize(QSize(100, 16777215))
        self.doubleAccuracy.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.doubleAccuracy.setDecimals(6)
        self.doubleAccuracy.setMaximum(1000000000000.000000000000000)

        self.verticalLayout.addWidget(self.doubleAccuracy, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkTrace = QCheckBox(self.dockWidgetContents)
        self.checkTrace.setObjectName(u"checkTrace")

        self.verticalLayout.addWidget(self.checkTrace, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushReset = QPushButton(self.dockWidgetContents)
        self.pushReset.setObjectName(u"pushReset")
        self.pushReset.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(100, 100, 100);\n"
"}")

        self.verticalLayout.addWidget(self.pushReset)

        self.pushStartSim = QPushButton(self.dockWidgetContents)
        self.pushStartSim.setObjectName(u"pushStartSim")
        self.pushStartSim.setStyleSheet(u"QPushButton{\n"
"	background-color: green;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(20, 150, 0);\n"
"}")

        self.verticalLayout.addWidget(self.pushStartSim)

        self.pushStopSim = QPushButton(self.dockWidgetContents)
        self.pushStopSim.setObjectName(u"pushStopSim")
        self.pushStopSim.setStyleSheet(u"QPushButton{\n"
"	background-color: red;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(150, 20, 0);\n"
"}")

        self.verticalLayout.addWidget(self.pushStopSim)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 850, 38))
        self.menuSimulation = QMenu(self.menuBar)
        self.menuSimulation.setObjectName(u"menuSimulation")
        self.menuHilfe = QMenu(self.menuBar)
        self.menuHilfe.setObjectName(u"menuHilfe")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
#if QT_CONFIG(shortcut)
        self.labelMass.setBuddy(self.labelMass)
#endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menuSimulation.menuAction())
        self.menuBar.addAction(self.menuHilfe.menuAction())
        self.menuSimulation.addAction(self.actionStart_Stop)
        self.menuSimulation.addSeparator()
        self.menuSimulation.addAction(self.actionDock)
        self.menuSimulation.addAction(self.actionAddElement)
        self.menuHilfe.addAction(self.actionWas_macht_dieser_Link)
        self.menuHilfe.addSeparator()
        self.menuHilfe.addAction(self.actionGithub_Repo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Schwerkraft Simulation", None))
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.actionStart_Stop.setText(QCoreApplication.translate("MainWindow", u"Start/ Stop", None))
#if QT_CONFIG(shortcut)
        self.actionStart_Stop.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionGithub_Repo.setText(QCoreApplication.translate("MainWindow", u"Github-Repo", None))
        self.actionWas_macht_dieser_Link.setText(QCoreApplication.translate("MainWindow", u"Was macht dieser Link?", None))
        self.actionDock.setText(QCoreApplication.translate("MainWindow", u"Dock", None))
#if QT_CONFIG(shortcut)
        self.actionDock.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionAddElement.setText(QCoreApplication.translate("MainWindow", u"Element hinzuf\u00fcgen", None))
#if QT_CONFIG(shortcut)
        self.actionAddElement.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.labelElemSet.setText(QCoreApplication.translate("MainWindow", u"Element", None))
        self.pushCreate.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushDelete.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.checkAktiv.setText(QCoreApplication.translate("MainWindow", u"Aktiv", None))
        self.labelMass.setText(QCoreApplication.translate("MainWindow", u"Masse", None))
        self.labelVelo.setText(QCoreApplication.translate("MainWindow", u"Geschwindigkeit", None))
        self.labelDegree.setText(QCoreApplication.translate("MainWindow", u"Winkel", None))
        self.labelPos.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.labelX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.labelY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.labelColor.setText(QCoreApplication.translate("MainWindow", u"Farbe", None))
        self.pushSetElem.setText(QCoreApplication.translate("MainWindow", u"\u00dcbernehmen", None))
        self.pushDiscElem.setText(QCoreApplication.translate("MainWindow", u"Verwerfen", None))
        self.labelSimSet.setText(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.labelSteps.setText(QCoreApplication.translate("MainWindow", u"Schritte pro Frame", None))
        self.labelAccuracy.setText(QCoreApplication.translate("MainWindow", u"Genauigkeit", None))
        self.checkTrace.setText(QCoreApplication.translate("MainWindow", u"Trace", None))
        self.pushReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushStartSim.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushStopSim.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.menuSimulation.setTitle(QCoreApplication.translate("MainWindow", u"Simulation", None))
        self.menuHilfe.setTitle(QCoreApplication.translate("MainWindow", u"Hilfe", None))
    # retranslateUi

