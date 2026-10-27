import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PySide6.QtCore import QFile, Qt, QTimer
from PySide6.QtGui import QBrush, QPen, QColor, QPainter
from ui_qtview import Ui_MainWindow
import physics_core as pc

STEPS_PER_FRAME = 100
RADIUS = 3
COLORS = ["red", "green", "blue"]

planet1 = pc.Planet(x_pos=50, y_pos=0, masse=1e15, speed=30, degree=150)
planet2 = pc.Planet(x_pos=-25, y_pos=43.3, masse=1e15, speed=30, degree=270)
planet3 = pc.Planet(x_pos=-25, y_pos=-43.3, masse=1e15, speed=30, degree=30)

planet_arr = [planet1, planet2, planet3]

class MainWindow(QMainWindow):
    def __init__(self, planets):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.planets = planets

        self.scene = QGraphicsScene(-300, -300, 600, 600)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.ui.graphicsView.scale(1, -1)                 # y-Achse nach oben wie bei Turtle
        # self.setCentralWidget(self.view)

        self.items, self.last_pos = [], []
        for p, c in zip(planets, COLORS):
            item = self.scene.addEllipse(-RADIUS, -RADIUS, 2*RADIUS, 2*RADIUS,
                                         QPen(Qt.NoPen), QBrush(QColor(c)))
            item.setPos(p.x_pos, p.y_pos)
            item.setZValue(1)
            self.items.append(item)
            self.last_pos.append((p.x_pos, p.y_pos))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.step)
        self.timer.start(16)

    def step(self):
        for _ in range(STEPS_PER_FRAME):
            pc.update(arr=self.planets, n=len(self.planets))

        for i, p in enumerate(self.planets):
            x0, y0 = self.last_pos[i]
            self.scene.addLine(x0, y0, p.x_pos, p.y_pos, QPen(QColor(COLORS[i])))
            self.items[i].setPos(p.x_pos, p.y_pos)
            self.last_pos[i] = (p.x_pos, p.y_pos)





    #     self.scene = QGraphicsScene(0, 0, 1000, 1000)

    #     self.kreis = self.scene.addEllipse(100, 100, 100, 100, QPen(Qt.white), QBrush(QColor("yellow"))) 
        
    #     self.ui.graphicsView.setScene(self.scene)

    #     self.text = self.scene.addText("hallo")
    #     self.text.setPos(500, 500)

    #     self.ui.graphicsView.update()

    #     # self.ui.start.clicked.connect(self.start)
    #     self.ui.start.setAutoRepeat(True)
    #     self.ui.start.pressed.connect(self.start)


    # def start(self):
    #     # for i in range(0, 1000):
    #     while self.ui.start.isChecked():
    #         pc.update(arr=planet_arr, n=len(planet_arr))
    #         self.kreis.setPos(planet_arr[1].x_pos + 200, planet_arr[1].y_pos + 200)
    #         self.ui.graphicsView.update()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(planet_arr)
    window.show()

    sys.exit(app.exec())