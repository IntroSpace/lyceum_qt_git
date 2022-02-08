import sys
from random import randint

from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circle = [0, 0, 0, 0]
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
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        # Рисуем прямоугольник заданной кистью
        qp.drawEllipse(*self.circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())