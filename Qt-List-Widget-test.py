#!/usr/bin/env python3

import sys
from dataclasses import dataclass

from PySide6.QtCore import QFile, Qt
from PySide6.QtLocation import QPlaceUser
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QSpinBox,
)

from ui_List_Widget import Ui_Dialog  #Form ist der Name des Fensters


@dataclass
class Item:
    mass: int = 10
    velo: int = 0
    degree: int = 0
    active: Qt.CheckState = Qt.CheckState.Checked

class Dialog(QDialog):
    def __init__(self):
        super().__init__() #Alternativ: super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.setItem)

        self.ui.pushButton_2.clicked.connect(self.rmItem)

        #wird ersetzt, um Funktion außerhalb von Dialog nutzen zu können. self.ui.pushButton_3.clicked.connect(print_items)

        self.ui.pushButton_4.clicked.connect(self.lwAddItem)

        self.ui.listWidget.currentItemChanged.connect(self.listItem)


    
    def lwAddItem(self):
        item = QListWidgetItem("Placeholder")
        item.setData(Qt.ItemDataRole.UserRole, Item())
        self.ui.listWidget.addItem(item)
        
    
    def rmItem(self):
        curRow = self.ui.listWidget.currentRow()
        if curRow >= 0:
            self.ui.listWidget.takeItem(curRow)

    def listItem(self, item: QListWidgetItem):
        element: Item = item.data(Qt.ItemDataRole.UserRole)
        self.ui.textEdit.setPlainText(item.text())
        self.ui.checkBox.setCheckState(element.active)
        self.ui.spinBox.setValue(element.mass)
        self.ui.spinBox_2.setValue(element.velo)
        self.ui.spinBox_3.setValue(element.degree)
    
    def setItem(self):
        item = self.ui.listWidget.currentItem()
        if item is not None:
            element: Item = item.data(Qt.ItemDataRole.UserRole)
            element.active = self.ui.checkBox.checkState()
            element.mass = self.ui.spinBox.value()
            element.velo = self.ui.spinBox_2.value()
            element.degree = self.ui.spinBox_3.value()
            item.setText(self.ui.textEdit.toPlainText().strip())

def print_items(dialog: Dialog):
    list_widget = dialog.ui.listWidget

    for row in range(list_widget.count()):
        item = list_widget.item(row)
        element: Item = item.data(Qt.ItemDataRole.UserRole)

        print("Items: \n"
            f"{item.text()}: Masse={element.mass}, "
            f"Geschwindigkeit={element.velo}, "
            f"Winkel={element.degree}, "
            f"Aktiv={element.active == Qt.CheckState.Checked}"
        )

    dialog.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Dialog()#Window ist die verwendete Instanz von Dialog, notwendig für Zugriff auf Eigenschaften
    window.ui.pushButton_3.clicked.connect(lambda: print_items(window))#Notwendig, um Dialog in einer externen Funktion zu manipulieren
    window.show()

    sys.exit(app.exec())