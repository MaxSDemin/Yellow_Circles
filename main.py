import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 430, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Пуск!"))


class Circle(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_new_coord)
        self.yellows_cyrcles = []

    def paintEvent(self, QPaintEvent):
        if self.yellows_cyrcles:
            qp = QPainter()
            qp.begin(self)
            for x_y_r_c in self.yellows_cyrcles:
                x, y, r, c = x_y_r_c
                qp.setPen(c)
                qp.drawEllipse(x, y, r, r)
            qp.end()

    def add_new_coord(self):
        x = randint(100, 500)
        y = randint(100, 300)
        r = randint(10, 100)
        c = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        self.yellows_cyrcles.append((x, y, r, c))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
ex = Circle()
ex.move(600, 400)
ex.show()
sys.exit(app.exec_())
