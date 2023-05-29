import sys, os

from qtpy.QtGui import QIcon, QGuiApplication, QFont
from qtpy.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QFrame, QWidget, QSplitter
from qtpy.QtCore import Qt, Signal, QCoreApplication

from leftSideBar import LeftSideBar
from rightSideBar import RightSideBar
from viewWidget import ViewWidget
from svgButton import SvgButton

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support
# qt version should be above 5.14
if os.environ['QT_API'] == 'pyqt5' or os.environ['QT_API'] != 'pyside6':
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

QApplication.setFont(QFont('Arial', 12))


class ImageGeneratingToolWidget(QWidget):
    notifierWidgetActivated = Signal()

    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('PyQt DreamStudio (Desktop)')
        self.setWindowIcon(QIcon('logo.png'))

        self.__leftSideBarWidget = LeftSideBar()
        self.__leftSideBarWidget.setVisible(False)
        self.__leftSideBarWidget.added.connect(self.__addImageGroup)
        self.__leftSideBarWidget.deleted.connect(self.__deleteImageGroup)
        # changed
        # imageUpdated
        self.__leftSideBarWidget.export.connect(self.__exportImageGroup)

        self.__viewWidget = ViewWidget()
        self.__rightSideBarWidget = RightSideBar()
        self.__rightSideBarWidget.notifierWidgetActivated.connect(self.notifierWidgetActivated)
        self.__rightSideBarWidget.submitDallE.connect(self.__setResult)
        self.__rightSideBarWidget.submitSd.connect(self.__setResult)

        self.__sideBarBtn = SvgButton()
        self.__sideBarBtn.setIcon('ico/sidebar.svg')
        self.__sideBarBtn.setCheckable(True)
        self.__sideBarBtn.setToolTip('Chat List')
        self.__sideBarBtn.setChecked(True)
        self.__sideBarBtn.toggled.connect(self.__leftSideBarWidget.setVisible)

        self.__historyBtn = SvgButton()
        self.__historyBtn.setIcon('ico/history.svg')
        self.__historyBtn.setCheckable(True)
        self.__historyBtn.setToolTip('History')
        self.__historyBtn.setChecked(True)
        self.__historyBtn.toggled.connect(self.__viewWidget.getExplorerWidget().setVisible)

        self.__settingBtn = SvgButton()
        self.__settingBtn.setIcon('ico/setting.svg')
        self.__settingBtn.setCheckable(True)
        self.__settingBtn.setToolTip('Settings')
        self.__settingBtn.setChecked(True)
        self.__settingBtn.toggled.connect(self.__rightSideBarWidget.setVisible)

        lay = QHBoxLayout()
        # lay.addWidget(self.__sideBarBtn)
        lay.addWidget(self.__settingBtn)
        lay.addWidget(self.__historyBtn)
        lay.setContentsMargins(2, 2, 2, 2)
        lay.setAlignment(Qt.AlignLeft)

        self.__menuWidget = QWidget()
        self.__menuWidget.setLayout(lay)
        self.__menuWidget.setMaximumHeight(self.__menuWidget.sizeHint().height())

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setFrameShadow(QFrame.Sunken)

        mainWidget = QSplitter()
        mainWidget.addWidget(self.__leftSideBarWidget)
        mainWidget.addWidget(self.__viewWidget)
        mainWidget.addWidget(self.__rightSideBarWidget)
        mainWidget.setSizes([100, 700, 200])
        mainWidget.setChildrenCollapsible(False)
        mainWidget.setHandleWidth(2)
        mainWidget.setStyleSheet(
        '''
        QSplitter::handle:horizontal
        {
            background: #CCC;
            height: 1px;
        }
        ''')

        lay = QVBoxLayout()
        lay.addWidget(self.__menuWidget)
        lay.addWidget(sep)
        lay.addWidget(mainWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        self.setLayout(lay)

    def showAiToolBar(self, f):
        self.__menuWidget.setVisible(f)

    def setAIEnabled(self, f):
        self.__rightSideBarWidget.setEnabled(f)

    def __addImageGroup(self):
        self.__db.insertConv('New Chat')
        cur_id = self.__db.getCursor().lastrowid
        self.__browser.resetChatWidget(cur_id)
        self.__leftSideBarWidget.addImageGroup(cur_id)
        self.__lineEdit.setFocus()
        print('addImageGroup')

    def __deleteImageGroup(self):
        print('deleteImageGroup')

    def __exportImageGroup(self):
        print('exportImageGroup')

    def __setResult(self, arg):
        self.__viewWidget.showSdResult(arg)
        # self.__leftSideBarWidget.addImageGroup('Stable Diffusion', 'New Image Group', 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ImageGeneratingToolWidget()
    w.show()
    sys.exit(app.exec_())
