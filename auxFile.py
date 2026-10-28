#Contains auxillary functions and classes for main.py
from PySide6.QtWidgets import QDialog

from ui_Name_Dialog import Ui_NameDialog
from Ui_Delete_Dialog import Ui_DeleteDialog


class MassObject:
    def __init__(self, name):
        self.__mass : int = 0
        self.x_pos : int = 0
        self.y_pos : int = 0
        self.__degree : float = 0.0
        self.x_spd : float = 0.0
        self.y_spd : float = 0.0
        self.dx_spd : float = 0.0
        self.dy_spd : float = 0.0
        self.__inVelo : float = 0.0
        self.__color = "schwarz"
        self.active = True
        self.__name = name

    def getMass(self):
        return self.__mass
    
    def setMass(self, newMass):
        self.__mass = int(newMass)
    
    def getDegree(self):
        return self.__degree
    
    def setDegree(self, newDegree):
        if float(newDegree) >= 0.0 and float(newDegree) < 360.0:
            self.__degree = float(newDegree)
    
    def getColor(self):
        return self.__color
    
    def setColor(self, newColor):
        validColors = ["schwarz", "blau", "grün", "rot", "blau", "gelb", "lila"]
        if newColor.lower() in validColors:
            self.__color = newColor
    
    def getName(self):
        return self.__name
    
    def getInVelo(self):
        return self.__inVelo

    def setInVelo(self, newInVelo):
        if newInVelo >= 0.0 :
            self.__inVelo = newInVelo

class SetNameDialog(QDialog):
    def __init__(self, planetList : list[MassObject]):
        super().__init__()
        self.ui = Ui_NameDialog()
        self.ui.setupUi(self)
        self.planetList = planetList
        self.success = False
        self.ui.labelError.setText("")

        self.ui.pushAccept.clicked.connect(self.setName)
        self.ui.pushDiscard.clicked.connect(self.abort)

    def abort(self):
        self.close()
    
    def setName(self):
        name = self.ui.lineName.text()
        for obj in self.planetList:
            if obj.getName() == name:
                self.ui.labelError.setText("Die Bezeichnung ist bereits vergeben")
                return
        self.planetList.append(MassObject(name))
        self.ui.labelError.setVisible(False)
        self.success = True
        self.accept()
    
    def getResFlag(self):
        return self.success

class DeleteDialog(QDialog):
    def __init__(self, name):
        super().__init__()
        self.ui = Ui_DeleteDialog()
        self.ui.setupUi(self)
        self.name = name
        self.text = "Möchten Sie Element " + self.name + " löschen?"
        self.ui.labelDelete.setText(self.text)

        self.ui.pushAccept.clicked.connect(self.delete)
        self.ui.pushDiscard.clicked.connect(self.abort)
    
    def delete(self):
        self.accept()
    
    def abort(self):
        self.close()