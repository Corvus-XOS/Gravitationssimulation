#!/usr/bin/env python3

import math
import sys
import webbrowser
from copy import copy

from PySide6.QtCore import QEvent, Qt, QTimer
from PySide6.QtGui import QBrush, QColor, QPainter, QPen, QTransform

import physics_core as pc

RADIUS = 6

#from PySide6.QtLocation import QPlaceUser
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QGraphicsScene,
    QMainWindow,
)

from auxFile import (
    DeleteDialog,
    Fehlermeldung,
    MassObject,
    ScreenShotName,
    SetNameDialog,
)
from Ui_Main_Window import Ui_MainWindow

planetList : list[MassObject] = [] #Liste mit allen Elementen
workingPlanetList : list[MassObject] = [] #Enthälte alle aktiven Planeten

#Klasse für das Hauptfenster
class MainWindow(QMainWindow):
    def __init__(self, planetList : list[MassObject], workingPlanetList : list[MassObject]):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.planetList = planetList
        self.workingPlanetList = workingPlanetList
        self.planetName = []

        #Simulations Parameter
        self.simSpeed : int = 1
        self.simAcc : float = 1.0

        self.index = 0
        self.startStop = False

        #Verknüpfen der Ui Elemente des Hautpfensters mit Funktionen
        #Einrichten der Auswahlbox für die Auswahl der Planeten
        self.ui.comboElement.currentTextChanged.connect(self.textChange)
        self.ui.comboColor.addItems(["white", "blue", "green", "red", "yellow", "purple"] )

        #Verknüpfen der Knöpfe
        self.ui.pushCreate.clicked.connect(self.addElem)
        self.ui.pushSetElem.clicked.connect(self.acceptChange)
        self.ui.pushDiscElem.clicked.connect(self.discardChange)
        self.ui.pushDelete.clicked.connect(self.delElem)
        self.ui.pushReset.clicked.connect(self.resetSim)
        self.ui.pushStartSim.clicked.connect(self.startSim)
        self.ui.pushStopSim.clicked.connect(self.stopSim)
        self.ui.pushSave.clicked.connect(self.saveView)

        #Vernküpfen der Tastenkürzeln
        self.ui.actionStart_Stop.triggered.connect(self.toggleSim)
        self.ui.actionDock.triggered.connect(self.toggleDock)
        self.ui.actionGithub_Repo.triggered.connect(self.openRepo)
        self.ui.actionWas_macht_dieser_Link.triggered.connect(self.openRandomLink)
        self.ui.actionAddElement.triggered.connect(self.addElem)
        self.ui.actionReset.triggered.connect(self.resetSim)
        self.ui.actionBild_Speichern.triggered.connect(self.saveView)
        self.ui.actionElement_bernehmen.triggered.connect(self.acceptChange)
        

        self.ui.doubleAccuracy.setValue(1e-3)
        self.ui.spinSteps.setValue(100)

        #-------------------------------------------------------------------------
        #Slider: self.ui.horSliderZoom
        #Wert wird NICHT extra angezeigt, dafür kann jedoch dass darüber liegende Label verwendte werden: self.ui.labelZoom, evtl Wert anhängen
        self.ui.horSliderZoom.valueChanged.connect(self.updateZoom)
        self.ui.horSliderZoom.setMaximum(100)
        self.ui.horSliderZoom.setMinimum(1)
        self.ui.horSliderZoom.setValue(100)

        self.ui.graphicsView.setBackgroundBrush(QBrush(QColor(0x0)))
        self.ui.graphicsView.installEventFilter(self)    # für Resize des GraphicsView
        # Initialisierung von GraphicsView
        self.updateView()
        self.updateZoom()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.step)

    #Fügt Element zur Liste der Planeten hinzu
    def addElem(self):
        nameDialog = SetNameDialog(self.planetList)
        if nameDialog.exec() == QDialog.DialogCode.Accepted: #Ruft Dialog für Namenswahl auf
            elemName = planetList[-1].getName() #Wird ausgeführt, wenn im Dialog bestätigt wurde
            self.ui.comboElement.addItem(elemName)

            self.count = self.ui.comboElement.count()
            self.ui.comboElement.setCurrentIndex(self.count - 1)

            self.ui.statusBar.showMessage("Element hinzugefügt", 5000)
        
    #Entfernt Planet aus Liste
    def delElem(self):
        curText = self.ui.comboElement.currentText()
        idx : int = -1

        for obj in planetList: #Sucht nach dem Index des derzeit in der Auswahlbox aktiven Planeten
            if obj.getName() == curText:
                idx = planetList.index(obj)
                break

        if idx != -1: #Wenn die Auswahlbox nicht leer ist
            deleteDialog = DeleteDialog(planetList[idx].getName())
            if deleteDialog.exec() == QDialog.DialogCode.Accepted: #Führt Dialog zum Löschen aus
                self.ui.comboElement.removeItem(self.ui.comboElement.currentIndex()) #Wird asugewählt, wenn der Dialog bestätigt wurde
                planetList.pop(idx)
                self.ui.statusBar.showMessage("Element gelöscht", 5000)
                self.resetSim()

    #Aktualisiert die Daten über die Plaeten, wenn in der Auswahlbox ein anderer Planet ausgewählt wurde
    def textChange(self):
        curText = self.ui.comboElement.currentText()
        idx : int = 0

        for obj in planetList: #Sucht nach dem Index des ausgewählten Planeten
            if obj.getName() == curText:
                idx = planetList.index(obj)

        planet = planetList[idx]
        if planet is not None: #Aktualisiert alle Ui Elemente für die Daten der Planeten
            if(planet.active):
                self.ui.checkAktiv.setCheckState(Qt.CheckState.Checked)
            else:
                self.ui.checkAktiv.setCheckState(Qt.CheckState.Unchecked)
            self.ui.lineEditMasse.setText(f"{planet.getMass():.2e}")
            self.ui.spinVelo.setValue(int(planet.getInVelo()))
            self.ui.spinDegree.setValue(int(planet.getDegree()))
            self.ui.spinXPos.setValue(planet.x_pos)
            self.ui.spinYPos.setValue(planet.y_pos)
            idx = self.ui.comboColor.findText(planet.getColor())
            if idx != -1:
                self.ui.comboColor.setCurrentIndex(idx)

    #Bestätigt Änderungen an den Daten von Planeten
    def acceptChange(self):
        curText = self.ui.comboElement.currentText()
        if curText == "":
            return
        
        idx : int = 0

        for obj in planetList:
            if obj.getName() == curText:
                idx = planetList.index(obj)
        try: #Überprüft, ob bei der Masse eine Zahl übergeben wurde
            planetList[idx].setMass(float(self.ui.lineEditMasse.text()))
        except ValueError:
            fehlermeldung = Fehlermeldung()
            fehlermeldung.exec()
            return
        planetList[idx].active = self.ui.checkAktiv.isChecked() #Übernimmt alle Daten, welche für den Planten im Dock ausgewählt wurden
        planetList[idx].setMass(float(self.ui.lineEditMasse.text()))
        planetList[idx].setInVelo(self.ui.spinVelo.value())
        planetList[idx].setDegree(self.ui.spinDegree.value())
        rad = math.radians(planetList[idx].getDegree())
        planetList[idx].x_spd = planetList[idx].getInVelo() * math.cos(rad)
        planetList[idx].y_spd = planetList[idx].getInVelo() * math.sin(rad)
        planetList[idx].x_pos = self.ui.spinXPos.value()
        planetList[idx].y_pos = self.ui.spinYPos.value()
        planetList[idx].setColor(self.ui.comboColor.currentText())

        workingPlanetList.clear() #Aktualisiert die Liste der aktiven Planeten
        for i in range(0, len(planetList)):
            if planetList[i].active:
                workingPlanetList.append(copy(planetList[i]))
        self.ui.statusBar.showMessage("Daten übernommen", 5000)

        self.updateView() #Aktualisert die Ansicht, da sich auch die Postion von Planeten verändern kann
        self.items, self.last_pos = [], []
        for i, p in enumerate(workingPlanetList):
            item = self.scene.addEllipse(-RADIUS, -RADIUS, 2*RADIUS, 2*RADIUS, QPen(), QBrush(QColor(p.getColor())))
            item.setPos(p.x_pos, p.y_pos)
            item.setZValue(1)
            self.items.append(item)
            self.last_pos.append((p.x_pos, p.y_pos))

    #verwirft Änderungen an den Daten von Planeten, in dem textChange() aufgerufen wird
    def discardChange(self):
        self.textChange()
        self.ui.statusBar.showMessage("Änderungen verworfen", 5000)
    
    #Setz die Siumlation zurück
    def resetSim(self):
        self.ui.pushSetElem.setEnabled(True)
        self.ui.pushDiscElem.setEnabled(True)
        self.ui.pushDelete.setEnabled(True)
        workingPlanetList.clear()
        for i in range(0, len(planetList)):
            if planetList[i].active:
                workingPlanetList.append(copy(planetList[i]))
        self.updateView()           #Aktualisiert die Ansicht
        self.stopSim()              # Stoppt Simulation bei Reset
        self.items, self.last_pos = [], []
        for i, p in enumerate(workingPlanetList):
            item = self.scene.addEllipse(-RADIUS, -RADIUS, 2*RADIUS, 2*RADIUS, QPen(), QBrush(QColor(p.getColor()))) #Pen: Qt.NoPen
            item.setPos(p.x_pos, p.y_pos)
            item.setZValue(1)
            self.items.append(item)
            self.last_pos.append((p.x_pos, p.y_pos))
        self.ui.statusBar.showMessage("Simulation zurückgesetzt", 5000)
    
    #Startet die Simulation
    def startSim(self):
        self.startStop = True
        self.timer.start(self.ui.spinSPF.value())
        self.ui.pushSetElem.setEnabled(False)
        self.ui.pushDiscElem.setEnabled(False)
        self.ui.pushDelete.setEnabled(False)

    #Stoppt die Simulation
    def stopSim(self):
        self.startStop = False
        self.timer.stop()
    
    #Wählt einen der darüberliegenden Funktionen aus, notwendig für Kurzbefehl
    def toggleSim(self):
        if self.startStop == True:
            self.stopSim()
        else:
            self.startSim()
    
    #Wechselt die Ansicht des Docks
    def toggleDock(self):
        if self.ui.dockWidget.isVisible():
            self.ui.dockWidget.setVisible(False)
        else:
            self.ui.dockWidget.setVisible(True)

    #Öffnet den "zufälligen" Link, für Kurzbefehl
    def openRepo(self):
        webbrowser.open("https://github.com/Corvus-XOS/Zimbos-Python")

    #Öffnet Github Repository, für Kurzbefehl
    def openRandomLink(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def step(self):
            for _ in range(self.ui.spinSteps.value()):
                pc.update(arr=workingPlanetList, n=len(workingPlanetList), dt=self.ui.doubleAccuracy.value())
    
            for i, p in enumerate(workingPlanetList):
                x0, y0 = self.last_pos[i]
                self.items[i].setPos(p.x_pos, p.y_pos)
                if self.ui.checkTrace.isChecked():
                    self.scene.addLine(x0, y0, p.x_pos, p.y_pos, QPen(QColor(p.getColor())))
                self.last_pos[i] = (p.x_pos, p.y_pos)

    # Fenstergröße anpassen
    def updateView(self):
        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.updateSceneRect()

    # Szene an die aktuelle Größe des Viewports anpassen (Ursprung bleibt in der Mitte)
    def updateSceneRect(self):
        vp = self.ui.graphicsView.viewport()
        w, h = vp.width(), vp.height()
        self.scene.setSceneRect(-w / 2, -h / 2, w, h)

    def eventFilter(self, obj, event):
        if obj is self.ui.graphicsView and event.type() == QEvent.Type.Resize:
            self.updateSceneRect()
        return super().eventFilter(obj, event)

    # Zoom anpassen
    def updateZoom(self):
        zoom = self.ui.horSliderZoom.value() / 100
        self.ui.graphicsView.setTransform(QTransform().scale(zoom, -zoom))

    #Speichert die aktuelle Ansicht
    def saveView(self):
        name = ""
        screenShotDialog = ScreenShotName()
        if screenShotDialog.exec() == QDialog.DialogCode.Accepted: #Ruft Dialog zur Namenswahl des Bils aus
            name = screenShotDialog.getName() + ".png"
            pixmap = self.ui.graphicsView.viewport().grab()
            pixmap.save(name)






if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(planetList, workingPlanetList=workingPlanetList) #Legt Instanz des Hauptfensters an
    # window.showMaximized()
    window.show() #Zeigt Hauptfenster an

    sys.exit(app.exec()) #Startet Anwendung