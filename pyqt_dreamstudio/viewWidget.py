import requests

from qtpy.QtGui import QFont, QPixmap
from qtpy.QtWidgets import QWidget, QLabel, QGridLayout, QStackedWidget, QSplitter
from qtpy.QtCore import Qt

from pyqt_dreamstudio.explorerWidget import ExplorerWidget
from pyqt_dreamstudio.thumbnailView import ThumbnailView


class ViewWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.__currentImageView = ThumbnailView()
        self.__explorerWidget = ExplorerWidget()
        self.__explorerWidget.clicked.connect(self.__currentImageView.setPixmap)

        imageWidget = QSplitter()
        imageWidget.setOrientation(Qt.Vertical)
        imageWidget.addWidget(self.__currentImageView)
        imageWidget.addWidget(self.__explorerWidget)
        imageWidget.setSizes([700, 300])
        imageWidget.setChildrenCollapsible(False)
        imageWidget.setHandleWidth(2)
        imageWidget.setStyleSheet(
            '''
            QSplitter::handle:vertical
            {
                background: #CCC;
                height: 1px;
            }
            ''')

        homeWidget = QLabel('Home')
        homeWidget.setAlignment(Qt.AlignCenter)
        homeWidget.setFont(QFont('Arial', 32))

        self.__mainWidget = QStackedWidget()
        # self.__mainWidget.addWidget(homeWidget)
        self.__mainWidget.addWidget(imageWidget)

        lay = QGridLayout()
        lay.addWidget(self.__mainWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

    def showSdResult(self, image_bin):
        self.__mainWidget.setCurrentIndex(1)
        self.showImage(image_bin)

    def showImage(self, arg):
        self.__currentImageView.setContent(arg)
        self.__explorerWidget.addContent(arg)

    def getExplorerWidget(self):
        return self.__explorerWidget