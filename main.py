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
        self.planetName = {} #dict, to cantain name and uid together

        #Simulation params
        self.simSpeed : int = 1
        self.simAcc : float = 1.0

        self.planetIdSeed = 0 #Contains seed for uid

        self.ui.comboElement.currentIndexChanged.connect(self.idxChange)

    
    def addElem(self):
        planet = MassObject(self.planetIdSeed)
        self.planetList.append(planet)
        self.planetName[self.planetIdSeed] = planet.name
        self.ui.comboElement.addItem(planet.name, self.planetIdSeed)
        self.planetIdSeed += 1 #changes uid, to stay unique
        

    def delElem(self):
        element : MassObject = self.ui.comboElement.currentData()
        if element is not None:
            idx = element.getUid()
            for obj in self.planetList:
                if obj.getUid() == idx:
                    self.planetList.remove(obj) #obj is unique, so no break needed
    
    def idxChange(self):
        uid = self.ui.comboElement.currentData()
        if uid is None:
            return

        planet = next((p for p in self.planetList if p.getUid() == uid), None)
        if planet is not None:
            self.ui.lineEdit.setText(planet.name)
            if(planet.active):
                self.ui.checkAktiv.setCheckState(Qt.CheckState.Checked)
            else:
                self.ui.checkAktiv.setCheckState(Qt.CheckState.Unchecked)
            self.ui.spinMass.setValue(planet.getMass())
            self.ui.spinVelo.setValue(planet.getVelo())
            #finish displaying data







if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(planetList)
    window.show()

    sys.exit(app.exec())