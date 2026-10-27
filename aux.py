#Contains auxillary functions and classes for main.py
from math import sqrt


class MassObject:
    def __init__(self, uid):
        self.__mass : int = 0
        self.x_pos : int = 0
        self.y_pos : int = 0
        self.__degree : float = 0.0
        self.x_spd : float = 0.0
        self.y_spd : float = 0.0
        self.dx_spd : float = 0.0
        self.dy_spd : float = 0.0
        self.__color = "black"
        self.active = True
        self.name = "Element"
        self.__uid = uid #Contains unique, non changable id to distinguish elements

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
        validColors = ["black", "green", "red", "blue", "yellow", "purple"]
        if newColor.lower() in validColors:
            self.__color = newColor
    
    def getUid(self):
        return self.__uid

    def getVelo(self):
        return sqrt(self.dx_spd * self.dx_spd + self.dy_spd * self.dy_spd)