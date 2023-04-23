import random

from PySide6 import QtWidgets, QtGui, QtCore

class FancyButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget, text: str):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText(text)
    
    def enterEvent(self, event: QtGui.QEnterEvent) -> None:
        p_box = self.parentWidget().rect()

        new_x = random.randint(0, p_box.width() - self.rect().width())
        new_y = random.randint(0, p_box.height() - self.rect().height())

        self.move(new_x, new_y)
        return super().enterEvent(event)

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.resize(800, 600)

        self.btn = FancyButton(self, "Нажми меня :)")
        self.btn.resize(200, 50)
        bbox = self.btn.rect()
        self.btn.move(400 - bbox.width() // 2, 300 - bbox.height() // 2)
        self.btn.clicked.connect(self.win)

    def win(self):
        self.setWindowTitle("You won!")

app = QtWidgets.QApplication()

window = MainWindow()
window.show()

app.exec()