import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circle = [0, 0, 0, 0]
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        rad = randint(1, 50)
        self.circle = [randint(0, self.width()), randint(0, self.height()),
                       rad, rad]
        self.repaint()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor("yellow"))
        # Рисуем прямоугольник заданной кистью
        qp.drawEllipse(*self.circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())