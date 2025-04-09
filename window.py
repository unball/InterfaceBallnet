from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget, QFileDialog, QGraphicsView, QGraphicsScene, QPlainTextEdit)
from PySide6.QtMultimedia import QMediaPlayer, QMediaCaptureSession, QCamera
from PySide6.QtMultimediaWidgets import QVideoWidget
import os, logging
from media_player import *

logger = logging.getLogger(__name__)
logging.basicConfig(filename="box.log",level=logging.INFO)

class QLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)

class QClickableLabel(QLabel):
    clicked = Signal()
    
    def mousePressEvent(self, ev):
        self.clicked.emit()

class QVideoPlayer(QWidget):
        def __init__(self, parent = None):
                super(QVideoPlayer,self).__init__(parent)
                
                self.videoWidget = QVideoWidget(parent)
                
                self.mediaPlayer = QMediaPlayer()
                self.mediaPlayer.setVideoOutput(self.videoWidget)
                
                self.camera = QCamera()
                
                self.cameraSession = QMediaCaptureSession()
                self.cameraSession.setCamera(self.camera)
                self.cameraSession.setVideoOutput(self.videoWidget)
                

        def show(self, source):
                if source == "Webcam":
                        logging.info("Opening camera....")
                        self.mediaPlayer.stop()
                        self.camera.start()
                        
                elif source == "Arquivo de vídeo":
                        self.camera.stop()
                        self.mediaPlayer.play()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
            
        ##### SET FONTS
        fontInter12 = QFont()
        fontInter12.setFamilies([u"Inter"])
        fontInter12.setPointSize(12)
        
        fontInter18 = QFont()
        fontInter18.setFamilies([u"Inter"])
        fontInter18.setPointSize(18)
        
        ##### SET ICONS
        icon = QIcon()
        icon.addFile(u"assets/imgs/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        
        closeIcon = QIcon()
        closeIcon.addFile(u"assets/imgs/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        
        playIcon = QIcon()
        playIcon.addFile(u"assets/imgs/mdi_play-pause.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        
        ##### MAIN WINDOWS SETTINGS
        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 600)
        
        MainWindow.setFont(fontInter12)
        MainWindow.setStyleSheet(u"* {\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"}\n"
"")
        ##### CENTRAL WIDGET SETTINGS
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        
        self.centralwidget.setStyleSheet(u"background-color: #1d1d1d;\n"
"")
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 920, 540))
        
        ##### HEADER SETTINGS
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
        
        self.title.setFont(fontInter18)
        self.title.setAutoFillBackground(False)

        self.name.addWidget(self.title, 0, Qt.AlignmentFlag.AlignTop)

        self.header.addLayout(self.name)

        self.barcolor = QLabel(self.layoutWidget1)
        self.barcolor.setObjectName(u"barcolor")
        self.barcolor.setPixmap(QPixmap(u"../Bars.png"))

        self.header.addWidget(self.barcolor, 0, Qt.AlignmentFlag.AlignTop)
        
        ##### BUTTONS
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(20, 490, 90, 28))
        
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        
        self.saveButton.setFont(fontInter12)
        self.saveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.saveButton.setIcon(icon)
        self.saveButton.setIconSize(QSize(24, 24))
        self.saveButton.setStyleSheet("background-color: #bad266; color: black")
        
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(120, 490, 90, 28))
        
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setFont(fontInter12)
        self.closeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    
        
        self.closeButton.setIcon(closeIcon)
        self.closeButton.setIconSize(QSize(24, 24))
        
          
        self.execButton = QPushButton(self.centralwidget)
        self.execButton.setObjectName(u"execButton")
        self.execButton.setGeometry(QRect(760, 47, 121, 28))
        
        sizePolicy.setHeightForWidth(self.execButton.sizePolicy().hasHeightForWidth())
        self.execButton.setSizePolicy(sizePolicy)
        
        self.execButton.setFont(fontInter12)
        self.execButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.execButton.setIcon(playIcon)
        self.execButton.setIconSize(QSize(24, 24))
        self.execButton.setCheckable(True)
        self.execButton.setStyleSheet("background-color: #bad266; color: black")
        
        ##### MEDIA DISPLAY
        
        self.sourceDropdown = QComboBox(self.centralwidget)
        self.sourceDropdown.setGeometry(QRect(600, 47, 150, 30))
        
        self.sourceDropdown.addItem("")
        self.sourceDropdown.addItem("")
        
        self.sourceDropdown.setObjectName(u"sourceDropdown")
        
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        
        sizePolicy2.setHeightForWidth(self.sourceDropdown.sizePolicy().hasHeightForWidth())
        
        self.sourceDropdown.setSizePolicy(sizePolicy2)
        self.sourceDropdown.setFixedHeight(30)
        self.sourceDropdown.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sourceDropdown.setStyleSheet(u"color: white;\n"
"border: 2px solid #fff; \n"
"padding: 5px;\n"
"background: #1d1d1d;")

        self.videoDisplay = QVideoPlayer(self.centralwidget)
        self.videoDisplay.setObjectName(u"videoDisplay")
        self.videoDisplay.videoWidget.setGeometry(QRect(346, 100, 557, 313))
        
        self.logBox = QLogger(self.centralwidget)
        self.logBox.widget.setGeometry(QRect(346, 450, 557, 120))
        self.logBox.widget.setStyleSheet(u"color: white;\n"
"border: 2px solid #fff; \n"
"padding: 5px;\n"
"background: #1d1d1d;")
        self.logBox.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        logging.getLogger().addHandler(self.logBox)
        logging.getLogger().setLevel(logging.INFO)

        
        ##### SIDE MENU 
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 230, 291, 190))
        
        ### IMAGE OPTIONS
        self.imageOptions = QVBoxLayout(self.widget)
        self.imageOptions.setSpacing(7)
        self.imageOptions.setObjectName(u"imageOptions")
        self.imageOptions.setContentsMargins(0, 0, 0, 0)
        
        self.Opcoesdaimagem = QLabel(self.widget)
        self.Opcoesdaimagem.setObjectName(u"Opcoesdaimagem")
        self.Opcoesdaimagem.setFont(fontInter12)

        self.imageOptions.addWidget(self.Opcoesdaimagem)

        # BRIGHTNESS
        self.brightness = QVBoxLayout()
        self.brightness.setObjectName(u"brightness")
        
        self.brightnessSlider = QSlider(self.widget)
        self.brightnessSlider.setObjectName(u"brightnessSlider")
        self.brightnessSlider.setStyleSheet(u"background: white;\n"
"border: 2px solid white;\n"
)
        self.brightnessSlider.setOrientation(Qt.Orientation.Horizontal)
        self.brightnessSlider.setTickPosition(QSlider.TickPosition.NoTicks)

        self.brightness.addWidget(self.brightnessSlider)

        self.brightnessLabel = QHBoxLayout()
        self.brightnessLabel.setSpacing(0)
        self.brightnessLabel.setObjectName(u"brightnessLabel")
        
        self.brightnessIcon = QLabel(self.widget)
        self.brightnessIcon.setObjectName(u"brightnessIcon")
        
        sizePolicy.setHeightForWidth(self.brightnessIcon.sizePolicy().hasHeightForWidth())
        
        self.brightnessIcon.setSizePolicy(sizePolicy)
        self.brightnessIcon.setMinimumSize(QSize(20, 20))
        self.brightnessIcon.setMaximumSize(QSize(20, 20))
        self.brightnessIcon.setPixmap(QPixmap(u"assets/imgs/brightness.svg"))
        self.brightnessIcon.setScaledContents(True)

        self.brightnessLabel.addWidget(self.brightnessIcon)

        self.Brilho = QLabel(self.widget)
        self.Brilho.setObjectName(u"Brilho")
        
        sizePolicy.setHeightForWidth(self.Brilho.sizePolicy().hasHeightForWidth())
        
        self.Brilho.setSizePolicy(sizePolicy)
        self.Brilho.setFont(fontInter12)
        self.Brilho.setScaledContents(True)
        self.Brilho.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.brightnessLabel.addWidget(self.Brilho)

        self.brightness.addLayout(self.brightnessLabel)

        self.imageOptions.addLayout(self.brightness)

        # CONTRAST 
        self.constrast = QVBoxLayout()
        self.constrast.setObjectName(u"constrast")
        
        self.constrastSlider = QSlider(self.widget)
        self.constrastSlider.setObjectName(u"constrastSlider")
        self.constrastSlider.setStyleSheet(u"background: white;\n"
"border: 2px solid white;")
        self.constrastSlider.setOrientation(Qt.Orientation.Horizontal)

        self.constrast.addWidget(self.constrastSlider)

        self.constrastLabel = QHBoxLayout()
        self.constrastLabel.setSpacing(0)
        self.constrastLabel.setObjectName(u"constrastLabel")
        
        self.contrastIcon = QLabel(self.widget)
        self.contrastIcon.setObjectName(u"contrastIcon")
        
        sizePolicy.setHeightForWidth(self.contrastIcon.sizePolicy().hasHeightForWidth())
        
        self.contrastIcon.setSizePolicy(sizePolicy)
        self.contrastIcon.setMinimumSize(QSize(20, 20))
        self.contrastIcon.setMaximumSize(QSize(20, 20))
        self.contrastIcon.setPixmap(QPixmap(u"assets/imgs/contrast.svg"))
        self.contrastIcon.setScaledContents(True)

        self.constrastLabel.addWidget(self.contrastIcon)

        self.Constraste = QLabel(self.widget)
        self.Constraste.setObjectName(u"Constraste")
        
        sizePolicy.setHeightForWidth(self.Constraste.sizePolicy().hasHeightForWidth())
        
        self.Constraste.setSizePolicy(sizePolicy)
        self.Constraste.setFont(fontInter12)
        self.Constraste.setScaledContents(True)
        self.Constraste.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.constrastLabel.addWidget(self.Constraste)

        self.constrast.addLayout(self.constrastLabel)

        self.imageOptions.addLayout(self.constrast)

        # SATURATION
        self.saturation = QVBoxLayout()
        self.saturation.setObjectName(u"saturation")
        
        self.saturationSlider = QSlider(self.widget)
        self.saturationSlider.setObjectName(u"saturationSlider")
        self.saturationSlider.setStyleSheet(u"background: white;\n"
"border: 2px solid white;")
        self.saturationSlider.setOrientation(Qt.Orientation.Horizontal)

        self.saturation.addWidget(self.saturationSlider)

        self.saturationLabel = QHBoxLayout()
        self.saturationLabel.setSpacing(0)
        self.saturationLabel.setObjectName(u"saturationLabel")
        
        self.saturarionIcon = QLabel(self.widget)
        self.saturarionIcon.setObjectName(u"saturarionIcon")
        
        sizePolicy.setHeightForWidth(self.saturarionIcon.sizePolicy().hasHeightForWidth())
        
        self.saturarionIcon.setSizePolicy(sizePolicy)
        self.saturarionIcon.setMinimumSize(QSize(18, 20))
        self.saturarionIcon.setMaximumSize(QSize(18, 20))
        self.saturarionIcon.setPixmap(QPixmap(u"assets/imgs/saturation.svg"))
        self.saturarionIcon.setScaledContents(True)

        self.saturationLabel.addWidget(self.saturarionIcon)

        self.Saturacao = QLabel(self.widget)
        self.Saturacao.setObjectName(u"Saturacao")
        
        sizePolicy.setHeightForWidth(self.Saturacao.sizePolicy().hasHeightForWidth())
        
        self.Saturacao.setSizePolicy(sizePolicy)
        self.Saturacao.setFont(fontInter12)
        self.Saturacao.setScaledContents(True)
        self.Saturacao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.saturationLabel.addWidget(self.Saturacao)

        self.saturation.addLayout(self.saturationLabel)

        self.imageOptions.addLayout(self.saturation)

        ### MODEL SETTINGS
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 150, 291, 60))
        
        self.netSize = QVBoxLayout(self.widget1)
        self.netSize.setSpacing(7)
        self.netSize.setObjectName(u"netSize")
        self.netSize.setContentsMargins(0, 0, 0, 0)
        
        self.Modelo = QLabel(self.widget1)
        self.Modelo.setObjectName(u"Modelo")
        
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHeightForWidth(self.Modelo.sizePolicy().hasHeightForWidth())
        
        self.Modelo.setSizePolicy(sizePolicy1)
        self.Modelo.setMaximumSize(QSize(16777215, 28))
        self.Modelo.setFont(fontInter12)

        self.netSize.addWidget(self.Modelo)

        self.netSizeDropdown = QComboBox(self.widget1)
        
        self.netSizeDropdown.addItem("")
        
        self.netSizeDropdown.setObjectName(u"netSizeDropdown")
        
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        
        sizePolicy2.setHeightForWidth(self.netSizeDropdown.sizePolicy().hasHeightForWidth())
        
        self.netSizeDropdown.setSizePolicy(sizePolicy2)
        self.netSizeDropdown.setFixedHeight(30)
        self.netSizeDropdown.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.netSizeDropdown.setStyleSheet(u"color: white;\n"
"border: 2px solid #fff; \n"
"padding: 5px;\n"
"background: #1d1d1d;")

        self.netSize.addWidget(self.netSizeDropdown, 0, Qt.AlignmentFlag.AlignTop)
        
        ### FILE BROWSER
        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(32, 52, 291, 82))
        
        self.fileBrowser = QVBoxLayout(self.widget2)
        self.fileBrowser.setObjectName(u"fileBrowser")
        self.fileBrowser.setContentsMargins(0, 0, 0, 0)
        
        self.Pesquisar = QLabel(self.widget2)
        self.Pesquisar.setObjectName(u"Pesquisar")
        
        sizePolicy1.setHeightForWidth(self.Pesquisar.sizePolicy().hasHeightForWidth())
        
        self.Pesquisar.setSizePolicy(sizePolicy1)
        self.Pesquisar.setFont(fontInter12)

        self.fileBrowser.addWidget(self.Pesquisar)

        self.browser = QClickableLabel(self.widget2)
        self.browser.setObjectName(u"browser")
        
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHeightForWidth(self.browser.sizePolicy().hasHeightForWidth())
        
        self.browser.setSizePolicy(sizePolicy3)

        self.browser.setMaximumHeight(30)
        self.browser.setStyleSheet(u""
"border: 2px solid #fff; \n"
"padding: 5px;\n")
        self.browser.setWordWrap(True)
        
        self.dialog = QFileDialog(self)
        self.dialog.setFileMode(QFileDialog.FileMode.Directory)

        self.fileBrowser.addWidget(self.browser)
    
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        
        ##### SIGNALS AND SLOTS
        self.closeButton.clicked.connect(MainWindow.close)
        self.browser.clicked.connect(MainWindow.openFile)
        self.execButton.pressed.connect(MainWindow.runModel)
        #self.execButton.clicked[bool].connect(self.videoDisplay.play)
        self.sourceDropdown.textActivated[str].connect(self.videoDisplay.show)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Pose", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.execButton.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.execButton.setEnabled(True)
        self.Opcoesdaimagem.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es da imagem", None))
        self.Brilho.setText(QCoreApplication.translate("MainWindow", u"Brilho", None))
        self.Constraste.setText(QCoreApplication.translate("MainWindow", u"Contraste", None))
        self.Saturacao.setText(QCoreApplication.translate("MainWindow", u"Satura\u00e7\u00e3o", None))
        self.Modelo.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.netSizeDropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Ballnet Pose v1", None))
        self.videoDisplay.videoWidget.show()
        self.sourceDropdown.setCurrentText(QCoreApplication.translate("MainWindow", u"Webcam", None))
        self.sourceDropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Webcam", None))
        self.sourceDropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Arquivo de vídeo", None))
        self.netSizeDropdown.setCurrentText(QCoreApplication.translate("MainWindow", u"Large - YOLOv8l", None))
        self.Pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
