import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from random import randint


class Cyrcle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add_new_coord)
        self.yellows_cyrcles = []

    def paintEvent(self, QPaintEvent):
        if self.yellows_cyrcles:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(Qt.yellow)
            for x_y_r in self.yellows_cyrcles:
                x, y, r = x_y_r
                qp.drawEllipse(x, y, r, r)
            qp.end()


    def add_new_coord(self):
        x = randint(100, 500)
        y = randint(100, 300)
        r = randint(10, 100)
        self.yellows_cyrcles.append((x, y, r))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = Cyrcle()
ex.move(600, 400)
ex.show()
sys.exit(app.exec_())
