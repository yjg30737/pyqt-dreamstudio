from qtpy.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from qtpy.QtCore import Signal

from pyqt_dreamstudio.imageStableDiffusionPage import ImageStableDiffusionPage


class RightSideBar(QWidget):
    submitDallE = Signal(str)
    submitSd = Signal(bytes)
    notifierWidgetActivated = Signal()

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        w = ImageStableDiffusionPage()
        w.notifierWidgetActivated.connect(self.notifierWidgetActivated)
        w.submitSd.connect(self.submitSd)
        lay = QVBoxLayout()
        lay.addWidget(w)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)