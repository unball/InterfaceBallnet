import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QPointF
import os
import logging
from window import Ui_MainWindow

logging.basicConfig(level=logging.INFO)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
    
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event):
        delta = QPointF(event.globalPosition() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        
        self.oldPosition = event.globalPosition()
    
    def openFile(self):
        self.frames = self.dialog.getOpenFileName(self, "Open Image", os.getcwd())
        self.browser.setText(self.frames[0])

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    app.exec()