# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget, QFileDialog)

class QClickableLabel(QLabel):
    clicked = Signal()
    
    def mousePressEvent(self, ev):
        self.clicked.emit()
        

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
        
        ##### MAIN WINDOWS SETTINGS
        
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 540)
        
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
        self.saveButton.setStyleSheet(u"background-color: #BAD266; \n"
"color: #000;\n"
"border-radius: 12px;")
        self.saveButton.setIcon(icon)
        self.saveButton.setIconSize(QSize(24, 24))
        
        self.closeButton = QPushButton(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(120, 490, 90, 28))
        
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setFont(fontInter12)
        self.closeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeButton.setStyleSheet(u"background-color: #3f3f3f; \n"
"color: #fff;\n"
"border-radius: 12px;")
        
        self.closeButton.setIcon(closeIcon)
        self.closeButton.setIconSize(QSize(24, 24))
        
        ##### IMAGE DISPLAY
        self.imageDisplay = QLabel(self.centralwidget)
        self.imageDisplay.setObjectName(u"imageDisplay")
        self.imageDisplay.setGeometry(QRect(360, 60, 528, 297))
        
        sizePolicy.setHeightForWidth(self.imageDisplay.sizePolicy().hasHeightForWidth())
        
        self.imageDisplay.setSizePolicy(sizePolicy)
        self.imageDisplay.setStyleSheet(u"background: #3d3d3d;\n"
"border: 2px solid white;\n"
"border-radius: 12px;")
        self.imageDisplay.setPixmap(QPixmap(u"assets/imgs/image.png"))
        self.imageDisplay.setScaledContents(False)
        self.imageDisplay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.logBox = QLabel(self.centralwidget)
        self.logBox.setObjectName(u"logBox")
        self.logBox.setGeometry(QRect(360, 390, 528, 120))
        
        sizePolicy.setHeightForWidth(self.logBox.sizePolicy().hasHeightForWidth())
        
        self.logBox.setSizePolicy(sizePolicy)
        self.logBox.setStyleSheet(u"background: #3d3d3d;\n"
"border: 2px solid white;\n"
"border-radius: 12px;")
        
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
        self.brightnessSlider.setStyleSheet(u"background: #BAD266;\n"
"border: 2px solid white;")
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
        self.constrastSlider.setStyleSheet(u"background: #BAD266;\n"
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
        self.saturationSlider.setStyleSheet(u"background: #BAD266;\n"
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
        self.widget1.setGeometry(QRect(30, 150, 291, 57))
        
        self.netSize = QVBoxLayout(self.widget1)
        self.netSize.setSpacing(7)
        self.netSize.setObjectName(u"netSize")
        self.netSize.setContentsMargins(0, 0, 0, 0)
        
        self.Tamanhodarede = QLabel(self.widget1)
        self.Tamanhodarede.setObjectName(u"Tamanhodarede")
        
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHeightForWidth(self.Tamanhodarede.sizePolicy().hasHeightForWidth())
        
        self.Tamanhodarede.setSizePolicy(sizePolicy1)
        self.Tamanhodarede.setMaximumSize(QSize(16777215, 28))
        self.Tamanhodarede.setFont(fontInter12)

        self.netSize.addWidget(self.Tamanhodarede)

        self.netSizeDropdown = QComboBox(self.widget1)
        
        self.netSizeDropdown.addItem("")
        self.netSizeDropdown.addItem("")
        self.netSizeDropdown.addItem("")
        self.netSizeDropdown.addItem("")
        self.netSizeDropdown.addItem("")
        
        self.netSizeDropdown.setObjectName(u"netSizeDropdown")
        
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        
        sizePolicy2.setHeightForWidth(self.netSizeDropdown.sizePolicy().hasHeightForWidth())
        
        self.netSizeDropdown.setSizePolicy(sizePolicy2)
        self.netSizeDropdown.setFixedHeight(30)
        self.netSizeDropdown.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.netSizeDropdown.setStyleSheet(u"color: #000;\n"
"border: 2px solid #fff; \n"
"padding: 5px;\n"
"border-radius: 12px;\n"
"background: #bad266;")

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

        self.browser.setMinimumHeight(28)
        self.browser.setStyleSheet(u"color: #000;\n"
"border: 2px solid #fff; \n"
"padding: 5px;\n"
"border-radius: 12px;\n"
"background: #bad266;")
        self.browser.setWordWrap(True)
        
        self.dialog = QFileDialog(self)
        self.dialog.setFileMode(QFileDialog.AnyFile)
        self.dialog.setNameFilter(u"Images (*.png *.jpg)")

        self.fileBrowser.addWidget(self.browser)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        
        ##### SIGNALS AND SLOTS
        self.closeButton.clicked.connect(MainWindow.close)
        self.browser.clicked.connect(MainWindow.openFile)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Pose", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.closeButton.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.logBox.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<ul style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"<li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>\n"
"<li>Integer rutrum nisi vestibulum, feugiat magna vel, gravida sem.</li>\n"
"<li>Vivamus ac velit placerat, dapibus nunc ut, ornare libero.</li>\n"
"<li>Pellentesque mattis purus eget enim lacinia, ut dapibus tellus faucibus.</li>\n"
"<li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>\n"
"<li>Integer rutrum "
                        "nisi vestibulum, feugiat magna vel, gravida sem.</li>\n"
"</ul></body></html>", None))
        self.Opcoesdaimagem.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es da imagem", None))
        self.Brilho.setText(QCoreApplication.translate("MainWindow", u"Brilho", None))
        self.Constraste.setText(QCoreApplication.translate("MainWindow", u"Contraste", None))
        self.Saturacao.setText(QCoreApplication.translate("MainWindow", u"Satura\u00e7\u00e3o", None))
        self.Tamanhodarede.setText(QCoreApplication.translate("MainWindow", u"Tamanho da rede", None))
        self.netSizeDropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Nano - YOLOv8n", None))
        self.netSizeDropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Small - YOLOv8s", None))
        self.netSizeDropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Medium - YOLOv8m", None))
        self.netSizeDropdown.setItemText(3, QCoreApplication.translate("MainWindow", u"Large - YOLOv8l", None))
        self.netSizeDropdown.setItemText(4, QCoreApplication.translate("MainWindow", u"Extra Large - YOLOv8xl", None))

        self.netSizeDropdown.setCurrentText(QCoreApplication.translate("MainWindow", u"Large - YOLOv8l", None))
        self.Pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))