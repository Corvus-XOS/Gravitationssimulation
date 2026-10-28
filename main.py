#!/usr/bin/env python3

import sys

from PySide6.QtCore import Qt

#from PySide6.QtLocation import QPlaceUser
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDockWidget,
    QDoubleSpinBox,
    QGraphicsView,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QPushButton,
    QSpinBox,
    QStatusBar,
    QWidgetAction,
)

from auxFile import MassObject, SetNameDialog, DeleteDialog
from ui_Main_Window import Ui_MainWindow

planetList : list[MassObject] = []

class MainWindow(QMainWindow):
    def __init__(self, planetList : list[MassObject]):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.planetList = planetList
        self.planetName = []

        #Simulation params
        self.simSpeed : int = 1
        self.simAcc : float = 1.0

        self.index = 0

        self.ui.comboElement.currentTextChanged.connect(self.textChange)
        self.ui.comboColor.addItems(["schwarz", "blau", "grün", "rot", "blau", "gelb", "lila"])

        self.ui.pushCreate.clicked.connect(self.addElem)
        self.ui.pushSetElem.clicked.connect(self.acceptChange)
        self.ui.pushDiscElem.clicked.connect(self.discardChange)
        self.ui.pushDelete.clicked.connect(self.delElem)
        self.ui.pushStartSim.clicked.connect(self.startSim)
        self.ui.pushStopSim.clicked.connect(self.stopSim)

        self.ui.comboElement.currentIndexChanged.connect(self.textChange)

        #Elemente für die Parameter der Simulation:
        #Schritte p. sek.: self.ui.spinSteps (SpinBox)
        #Genauigkeit: self.ui.doubleAccuracy (DoubleSpinBox)

    
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
            self.ui.spinMass.setValue(planet.getMass())
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
        if self.ui.checkAktiv.checkState == Qt.CheckState.Checked:
            planetList[idx].active = True
        else:
            planetList[idx].active = False
        planetList[idx].setMass(self.ui.spinMass.value())
        planetList[idx].setInVelo(self.ui.spinVelo.value())
        planetList[idx].setDegree(self.ui.spinDegree.value())
        planetList[idx].x_pos = self.ui.spinXPos.value()
        planetList[idx].y_pos = self.ui.spinYPos.value()
        planetList[idx].setColor(self.ui.comboColor.currentText())
        self.ui.statusBar.showMessage("Daten übernommen", 50000)

    def discardChange(self):
        self.textChange()
        self.ui.statusBar.showMessage("Änderungen verworfen", 5000)
    
    def startSim(self):
        #Hier den Code zum starten der Sim einsetzten und "pass" entfernen
        pass
        #------------------------

    def stopSim(self):
        #Hier den Code zum stopen der Sim einsetzen und "pass" entfernen
        pass
        #------------------------








if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(planetList)
    window.show()

    sys.exit(app.exec())