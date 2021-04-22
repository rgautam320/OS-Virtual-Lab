from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from ProcessScheduler.ProcessScheduler import UI_ProcessScheduler
from PageReplacement.PageReplacements import UI_PageReplacement
from DiskScheduler.DiskScheduling import UI_DiskScheduling
from ConcurrencyDeadlock.ConcurrencyDeadlock import UI_Concurrency


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('UI/main.ui', self)

        self.show()

        self.btn_process.clicked.connect(self.processScheduler)
        self.btn_page.clicked.connect(self.pageReplacement)
        self.btn_disk.clicked.connect(self.diskScheduling)
        self.btn_concurrency.clicked.connect(self.concurrencyDeadlock)

    def processScheduler(self):
        self.process = QtWidgets.QMainWindow()
        self.ui = UI_ProcessScheduler()
        self.ui.setupUi(self.process)
        self.process.show()

    def pageReplacement(self):
        self.page = QtWidgets.QMainWindow()
        self.ui = UI_PageReplacement()
        self.ui.setupUi(self.page)
        self.page.show()

    def diskScheduling(self):
        self.disk = QtWidgets.QMainWindow()
        self.ui = UI_DiskScheduling()
        self.ui.setupUi(self.disk)
        self.disk.show()

    def concurrencyDeadlock(self):
        self.concurrency = QtWidgets.QMainWindow()
        self.ui = UI_Concurrency()
        self.ui.setupUi(self.concurrency)
        self.concurrency.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    mainUI = Main()

    sys.exit(app.exec_())
