#!/usr/bin/env python3

import sys
import webbrowser
from webbrowser import open

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QBrush, QPen, QColor, QPainter
import physics_core as pc

STEPS_PER_FRAME = 100
RADIUS = 3
COLORS = ["red", "green", "blue"]

#from PySide6.QtLocation import QPlaceUser
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QMenu,
    QPushButton,
    QSpinBox,
    QStatusBar,
    QWidgetAction,
    QGraphicsScene,
)

from auxFile import DeleteDialog, Fehlermeldung, MassObject, SetNameDialog
from ui_Main_Window import Ui_MainWindow

planetList : list[MassObject] = []

workingPlanetList : list[MassObject] = []

# planet1 = MassObject(name="p1", x_pos=50, y_pos=0, mass=1e15, speed=30, degree=150)
# planet2 = MassObject(name="p2", x_pos=-25, y_pos=43.3, mass=1e15, speed=30, degree=270)
# planet3 = MassObject(name="p3", x_pos=-25, y_pos=-43.3, mass=1e15, speed=30, degree=30)

# planet_arr = [planet1, planet2, planet3]

class MainWindow(QMainWindow):
    def __init__(self, planetList : list[MassObject], workingPlanetList : list[MassObject]):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.planetList = planetList
        self.workingPlanetList = workingPlanetList
        self.planetName = []

        #Simulation params
        self.simSpeed : int = 1
        self.simAcc : float = 1.0

        self.index = 0
        self.startStop = False #Notwendig für QAction Start/Stop, True für Sim läuft

        self.ui.comboElement.currentTextChanged.connect(self.textChange)
        self.ui.comboColor.addItems(["black", "blue", "green", "red", "yellow", "purple"] )

        self.ui.pushCreate.clicked.connect(self.addElem)
        self.ui.pushSetElem.clicked.connect(self.acceptChange)
        self.ui.pushDiscElem.clicked.connect(self.discardChange)
        self.ui.pushDelete.clicked.connect(self.delElem)
        self.ui.pushStartSim.clicked.connect(self.startSim)
        self.ui.pushStopSim.clicked.connect(self.stopSim)

        self.ui.comboElement.currentIndexChanged.connect(self.textChange)

        self.ui.actionStart_Stop.triggered.connect(self.toggleSim)
        self.ui.actionDock.triggered.connect(self.toggleDock)
        self.ui.actionGithub_Repo.triggered.connect(self.openRepo)
        self.ui.actionWas_macht_dieser_Link.triggered.connect(self.openRandomLink)
        self.ui.actionAddElement.triggered.connect(self.addElem)

        #Elemente für die Parameter der Simulation:
        #Schritte p. sek.: self.ui.spinSteps (SpinBox)
        #Genauigkeit: self.ui.doubleAccuracy (DoubleSpinBox)
        self.scene = QGraphicsScene(-300, -300, 600, 600)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.ui.graphicsView.scale(1, -1)

        self.items, self.last_pos = [], []
        for p, c in zip(workingPlanetList, COLORS):
            item = self.scene.addEllipse(-RADIUS, -RADIUS, 2*RADIUS, 2*RADIUS, QPen(Qt.NoPen), QBrush(QColor(c)))
            item.setPos(p.x_pos, p.y_pos)
            item.setZValue(1)
            self.items.append(item)
            self.last_pos.append((p.x_pos, p.y_pos))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.step)

    
    def addElem(self):
        nameDialog = SetNameDialog(self.planetList)
        if nameDialog.exec() == QDialog.DialogCode.Accepted:
            elemName = planetList[-1].getName()
            self.ui.comboElement.addItem(elemName)

            self.count = self.ui.comboElement.count()
            self.ui.comboElement.setCurrentIndex(self.count - 1)

            self.ui.statusBar.showMessage("Element hinzugefügt", 5000)
        

    def delElem(self):
        curText = self.ui.comboElement.currentText()
        idx : int = -1

        for obj in planetList:
            if obj.getName() == curText:
                idx = planetList.index(obj)
                break

        if idx != -1:
            deleteDialog = DeleteDialog(planetList[idx].getName())
            if deleteDialog.exec() == QDialog.DialogCode.Accepted:
                self.ui.comboElement.removeItem(self.ui.comboElement.currentIndex())
                planetList.pop(idx)
                self.ui.statusBar.showMessage("Element gelöscht", 5000)
                return
            else:
                return
    
    def textChange(self):
        curText = self.ui.comboElement.currentText()
        idx : int = 0

        for obj in planetList:
            if obj.getName() == curText:
                idx = planetList.index(obj)

        planet = planetList[idx]
        if planet is not None:
            if(planet.active):
                self.ui.checkAktiv.setCheckState(Qt.CheckState.Checked)
            else:
                self.ui.checkAktiv.setCheckState(Qt.CheckState.Unchecked)
            self.ui.lineEditMasse.setText(str(planet.getMass()))
            self.ui.spinVelo.setValue(planet.getInVelo())
            self.ui.spinDegree.setValue(planet.getDegree())
            self.ui.spinXPos.setValue(planet.x_pos)
            self.ui.spinYPos.setValue(planet.y_pos)
            idx = self.ui.comboColor.findText(planet.getColor())
            if idx != -1:
                self.ui.comboColor.setCurrentIndex(idx)

    
    def acceptChange(self):
        curText = self.ui.comboElement.currentText()
        if curText == "":
            return
        
        idx : int = 0

        for obj in planetList:
            if obj.getName() == curText:
                idx = planetList.index(obj)
        try:
            planetList[idx].setMass(float(self.ui.lineEditMasse.text()))
        except ValueError:
            fehlermeldung = Fehlermeldung()
            fehlermeldung.exec()
            return
        planetList[idx].active = self.ui.checkAktiv.isChecked()
        planetList[idx].setMass(float(self.ui.lineEditMasse.text()))
        planetList[idx].setInVelo(self.ui.spinVelo.value())
        planetList[idx].setDegree(self.ui.spinDegree.value())
        planetList[idx].x_pos = self.ui.spinXPos.value()
        planetList[idx].y_pos = self.ui.spinYPos.value()
        planetList[idx].setColor(self.ui.comboColor.currentText())
        workingPlanetList = []
        for i in range(0, len(planetList)):
            if planetList[i].active:
                workingPlanetList.append(planetList[i])
        print(workingPlanetList)
        self.ui.statusBar.showMessage("Daten übernommen", 50000)

    def discardChange(self):
        self.textChange()
        self.ui.statusBar.showMessage("Änderungen verworfen", 5000)
    
    def startSim(self):
        #Hier den Code zum starten der Sim einsetzten und "pass" entfernen
        # pass
        self.timer.start(16)
        print("start")
        #------------------------

    def stopSim(self):
        #Hier den Code zum stopen der Sim einsetzen und "pass" entfernen
        # pass
        self.timer.stop()
        print("stop")
        #------------------------
    
    def toggleSim(self):
        if self.startStop == True:
            self.stopSim()
        else:
            self.startSim()
    
    def toggleDock(self):
        if self.ui.dockWidget.isVisible():
            self.ui.dockWidget.setVisible(False)
        else:
            self.ui.dockWidget.setVisible(True)

    def openRepo(self):
        webbrowser.open("https://github.com/Corvus-XOS/Zimbos-Python")

    def openRandomLink(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def step(self):
            for _ in range(STEPS_PER_FRAME):
                pc.update(arr=workingPlanetList, n=len(workingPlanetList))
    
            for i, p in enumerate(workingPlanetList):
                x0, y0 = self.last_pos[i]
                self.scene.addLine(x0, y0, p.x_pos, p.y_pos, QPen(QColor(COLORS[i])))
                self.items[i].setPos(p.x_pos, p.y_pos)
                self.last_pos[i] = (p.x_pos, p.y_pos)







if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(planetList, workingPlanetList=workingPlanetList)
    window.showMaximized()
    window.show()

    sys.exit(app.exec())