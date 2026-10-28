#Contains auxillary functions and classes for main.py

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
    