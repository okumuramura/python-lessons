from PySide6 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.resize(800, 600)
        
        self.select_color_btn = QtWidgets.QPushButton(self)
        bbox = self.select_color_btn.rect()
        self.select_color_btn.move(400 - bbox.width() // 2, 300 - bbox.height())
        self.select_color_btn.clicked.connect(self.color_pick)

    def color_pick(self):
        color_picker = QtWidgets.QColorDialog(self)
        color = color_picker.getColor()
        self.setStyleSheet(f"background: {color.name()}")
        self.setWindowTitle(color.name())

app = QtWidgets.QApplication()

window = MainWindow()
window.show()

app.exec()