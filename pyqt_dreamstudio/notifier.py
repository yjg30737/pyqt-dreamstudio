from qtpy.QtGui import QFont, QIcon
from qtpy.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QDesktopWidget, QSizePolicy, qApp, QPushButton, \
    QApplication
from qtpy.QtCore import Qt, QPoint, Signal, QTimer, QPropertyAnimation


class NotifierWidget(QWidget):
    doubleClicked = Signal()

    def __init__(self, informative_text='', detailed_text=''):
        super().__init__()
        self.__timerVal = 5000
        self.__initUi(informative_text, detailed_text)

    def __initUi(self, informative_text='', detailed_text=''):
        self.setFixedSize(250, 150)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)

        self.__informativeTextLabel = QLabel(informative_text) if informative_text else QLabel('Informative')
        self.__informativeTextLabel.setFont(QFont('Arial', 15, QFont.Bold))
        self.__detailedTextLabel = QLabel(detailed_text) if detailed_text else QLabel('Detailed')

        closeBtn = QPushButton()
        closeBtn.clicked.connect(self.close)
        closeBtn.setIcon(QIcon('ico/close.svg'))

        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)

        self.__btnWidget = QWidget()
        self.__btnWidget.setLayout(lay)

        lay = QHBoxLayout()
        lay.setAlignment(Qt.AlignTop | Qt.AlignRight)
        lay.addWidget(closeBtn)
        lay.setContentsMargins(0, 0, 0, 0)

        customMenuBar = QWidget()
        customMenuBar.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(customMenuBar)
        lay.addWidget(self.__informativeTextLabel)
        lay.addWidget(self.__detailedTextLabel)
        lay.addWidget(self.__btnWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        ag = QDesktopWidget().availableGeometry()

        geo = self.geometry()
        geo.moveBottomRight(QPoint(ag.width(), ag.height()))
        self.setGeometry(geo)

        lay.setContentsMargins(8, 8, 8, 8)
        self.setLayout(lay)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

        return super().keyPressEvent(e)

    def addWidgets(self, widgets: list):
        for widget in widgets:
            widget.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
            self.__btnWidget.layout().addWidget(widget)

    def show(self) -> None:
        super().show()
        QApplication.beep()
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.__checkTimer)
        self.__timer.start(1000)

    def __checkTimer(self):
        self.__timerVal -= 1000
        if self.__timerVal == 1000:
            self.__showAnimation()
        elif self.__timerVal <= 0:
            self.close()

    def __showAnimation(self):
        self.__animation = QPropertyAnimation(self, b"windowOpacity")
        self.__animation.finished.connect(self.close)
        self.__animation.setDuration(1000)
        self.__animation.setStartValue(1.0)
        self.__animation.setEndValue(0.0)
        self.__animation.start()

    def mouseDoubleClickEvent(self, e):
        self.doubleClicked.emit()
        self.close()
        return super().mouseDoubleClickEvent(e)