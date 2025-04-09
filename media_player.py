import sys
from PySide6.QtCore import Qt, QSize, QUrl, QRect
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (
    QPushButton, 
    QApplication,
    QHBoxLayout, 
    QStyle,
    QSlider,
    QStatusBar,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QLabel,
    QSizePolicy
)

class VideoPlayer(QWidget):

    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)

        self.mediaPlayer = QMediaPlayer()

        btnSize = QSize(16, 16)
        videoWidget = QVideoWidget()

        openButton = QPushButton("Open Video")   
        openButton.setToolTip("Open Video File")
        openButton.setStatusTip("Open Video File")
        openButton.setFixedHeight(24)
        openButton.setIconSize(btnSize)
        openButton.setFont(QFont("Noto Sans", 8))
        openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
        openButton.clicked.connect(self.abrir)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setFixedHeight(24)
        self.playButton.setIconSize(btnSize)
        self.playButton.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Orientation.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.statusBar = QStatusBar()
        self.statusBar.setFont(QFont("Noto Sans", 7))
        self.statusBar.setFixedHeight(14)
        
        ##### HEADER SETTINGS
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        self.layoutWidget1 = QWidget()
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 920, 540))
        
        sizePolicy.setHeightForWidth(self.layoutWidget1.sizePolicy().hasHeightForWidth())
        self.layoutWidget1.setSizePolicy(sizePolicy)
        
        self.header = QHBoxLayout(self.layoutWidget1)
        self.header.setSpacing(0)
        self.header.setObjectName(u"header")
        self.header.setContentsMargins(0, 0, 0, 0)
        
        self.name = QHBoxLayout()
        self.name.setSpacing(5)
        self.name.setObjectName(u"name")
        self.name.setContentsMargins(5, 5, 5, 5)
        
        self.logo = QLabel(self.layoutWidget1)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"assets/imgs/ballnet-logo.svg"))

        self.name.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignTop)

        self.title = QLabel(self.layoutWidget1)
        self.title.setObjectName(u"title")
        
        fontInter18 = QFont()
        fontInter18.setFamilies([u"Inter"])
        fontInter18.setPointSize(18)
        
        self.title.setFont(fontInter18)
        self.title.setText("Pose")

        self.name.addWidget(self.title, 0, Qt.AlignmentFlag.AlignTop)

        self.header.addLayout(self.name)
        
        
        
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)
        

        layout = QVBoxLayout()
        layout.addWidget(self.layoutWidget1)
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.statusBar)

        self.setLayout(layout)
        
        

        #help(self.mediaPlayer)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.playbackStateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.errorChanged.connect(self.handleError)
        self.statusBar.showMessage("Ready")
        
        

    def abrir(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select Media",
                ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi)")

        if fileName != '':
            self.mediaPlayer.setSource(QUrl.fromLocalFile(fileName))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(fileName)
            self.play()

    def play(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
        
        
if __name__ == '__main__' :        
    app = QApplication(sys.argv)
    window = VideoPlayer()
    window.showMaximized()
    app.exec()

# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QRadioButton, QLabel
# from PySide6.QtMultimedia import QMediaPlayer, QMediaCaptureSession, QCamera
# from PySide6.QtMultimediaWidgets import QVideoWidget
# from PySide6.QtCore import QUrl


# class VideoPlayerApp(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Configuração da janela principal
#         self.setWindowTitle("Reprodutor de Vídeo com QVideoWidget")
#         self.setGeometry(100, 100, 800, 600)

#         # Layout principal
#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)
#         self.layout = QVBoxLayout(self.central_widget)

#         # Radio buttons para escolher a fonte de vídeo
#         self.radio_webcam = QRadioButton("Webcam")
#         self.radio_file = QRadioButton("Arquivo de Vídeo")
#         self.radio_file.setChecked(True)  # Arquivo selecionado por padrão
#         self.layout.addWidget(self.radio_webcam)
#         self.layout.addWidget(self.radio_file)

#         # Widget de vídeo
#         self.video_widget = QVideoWidget()
#         self.layout.addWidget(self.video_widget)

#         # Inicializar o player de mídia
#         self.media_player = QMediaPlayer(self)
#         self.media_player.setVideoOutput(self.video_widget)

#         # Inicializar a câmera (webcam)
#         self.camera = QCamera(self)
#         self.capture_session = QMediaCaptureSession()
#         self.capture_session.setCamera(self.camera)
#         self.capture_session.setVideoOutput(self.video_widget)

#         # Conectar sinais dos radio buttons
#         self.radio_webcam.toggled.connect(self.toggle_video_source)
#         self.radio_file.toggled.connect(self.toggle_video_source)

#         # Iniciar a reprodução de vídeo
#         self.toggle_video_source()

#     def toggle_video_source(self):
#         """Alterna entre webcam e arquivo de vídeo."""
#         if self.radio_webcam.isChecked():
#             # Parar o player de mídia e iniciar a webcam
#             self.media_player.stop()
#             self.camera.start()
#         else:
#             # Parar a webcam e iniciar o player de mídia
#             self.camera.stop()
#             self.media_player.setSource(QUrl.fromLocalFile("caminho/para/seu/video.mp4"))  # Substitua pelo caminho do vídeo
#             self.media_player.play()

#     def closeEvent(self, event):
#         """Liberar recursos ao fechar a janela."""
#         self.camera.stop()
#         self.media_player.stop()
#         event.accept()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = VideoPlayerApp()
#     window.show()
#     sys.exit(app.exec())