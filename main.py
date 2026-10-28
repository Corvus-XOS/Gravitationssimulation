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
    QStatusBar,  #showMessage(text, timeout=x) for new status
    QWidgetAction,
)

from aux import MassObject
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

        self.ui.comboElement.currentIndexChanged.connect(self.idxChange)

        self.ui.pushCreate.clicked.connect(self.addElem)

    
    def addElem(self):
        planet = MassObject("WIP-Name")
        self.planetList.append(planet)
        self.ui.comboElement.addItem(planet.getName())
        #CHANGE: Name needs to be unique, Pop-up required
        self.ui.statusBar.showMessage("Element hinzugefügt", 5000)
        

    def delElem(self):
        element : MassObject = self.ui.comboElement.currentData()
        if element is not None:
            idx = element.getName()
            for obj in self.planetList:
                if obj.getName() == idx:
                    self.planetList.remove(obj) #obj is unique, so no break needed
    
    def idxChange(self):
        curData = self.ui.comboElement.currentData()
        if curData is None:
            return

        planet = next((p for p in self.planetList if p.getName() == curData), None)
        if planet is not None:
            if(planet.active):
                self.ui.checkAktiv.setCheckState(Qt.CheckState.Checked)
            else:
                self.ui.checkAktiv.setCheckState(Qt.CheckState.Unchecked)
            self.ui.spinMass.setValue(planet.getMass())
            self.ui.spinVelo.setValue(planet.getInVelo())
            #finish displaying data







if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(planetList)
    window.show()

    sys.exit(app.exec())