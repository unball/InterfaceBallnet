import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QPointF, QThread
import os
import logging
from window import *
import sys

logging.basicConfig(level=logging.INFO)

class QDisplayWorker(QObject):
    finished = Signal()
    
    def __init__(self, fileName):
        super().__init__()
        
        self.fileName = fileName
        
    
    
    def run(self):
        from models.BallnetPose.detect import BallnetPose
        
        self.model = BallnetPose()
        
        self.locations = self.model.detect(self.fileName)
        self.finished.emit()

class QDownloadWorker(QObject):
    finished = Signal()
    
    def __init__(self, path):
        super().__init__()
        self.repoPath = path
    
    def run(self):
        os.system("git lfs install")
        os.system(f"git clone {self.repoPath} models/BallnetPose")
        self.finished.emit()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.modelThread = QThread()
        self.downloadThread = QThread()
        
        self.centralize()
            
        
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition()
    
    def mouseMoveEvent(self, event):
        delta = QPointF(event.globalPosition() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        
        self.oldPosition = event.globalPosition()
    
    def centralize(self):
        screen = self.screen()
        screen_geometry = screen.geometry()

        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        self.move(x, y)
    
    def openFile(self):
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Abrir Vídeo",
                ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")

        if self.filePath != '':
            fileName = self.filePath.split("/")[-1]
        
            self.videoDisplay.mediaPlayer.setSource(QUrl.fromLocalFile(self.filePath))
            self.execButton.setEnabled(True)
            
            self.browser.setText(fileName)
            logging.info(f"Fonte: {self.filePath}")
    
    
    def download(self, repoPath):
        if not os.path.exists(os.path.join(os.getcwd(), "/models/BallnetPose")):
            
            self.downloadWorker = QDownloadWorker(repoPath)
            self.downloadWorker.moveToThread(self.downloadThread)
            
            self.downloadThread.started.connect(self.downloadWorker.run)
            self.downloadWorker.finished.connect(self.downloadThread.quit)
            self.downloadWorker.finished.connect(self.downloadWorker.deleteLater)
            self.downloadThread.finished.connect(self.downloadThread.deleteLater)
            
            logging.info("Baixando o modelo....")
            self.downloadThread.start()
            logging.info("Modelo baixado.")
    
    def runModel(self):
        if not self.modelThread.isRunning():
            self.download("https://huggingface.co/ayssag/BallnetPose")
            
            self.modelWorker = QDisplayWorker(self.filePath)
            self.modelWorker.moveToThread(self.modelThread)
            
            self.modelThread.started.connect(self.modelWorker.run)
            self.modelWorker.finished.connect(self.modelThread.quit)
            self.modelWorker.finished.connect(self.modelWorker.deleteLater)
            self.modelThread.finished.connect(self.modelThread.deleteLater)
            
            self.modelThread.start()
            
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    
    window.show()
    
    app.exec()