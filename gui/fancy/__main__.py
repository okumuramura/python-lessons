from PySide6 import QtWidgets, QtGui, QtCore

class FancyButton(QtWidgets.QPushButton):
    def __init__(self, parent, text: str):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setText(text)

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.resize(800, 600)

        self.btn = FancyButton(self, "Нажми меня :)")


app = QtWidgets.QApplication()

window = MainWindow()
window.show()

app.exec()