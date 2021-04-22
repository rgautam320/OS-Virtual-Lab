import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import qtmodern.styles
import numpy as np
import qtmodern.windows
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvasAgg
from PyQt5.QtWidgets import QMainWindow
from DiskScheduler.About import *
from DiskScheduler.aboutsstf import *
from DiskScheduler.warning import *
from DiskScheduler.aboutlook import *
from DiskScheduler.aboutclook import *
from DiskScheduler.aboutcscan import *
from DiskScheduler.aboutscan import *

# fig = plt.figure(figsize=[9, 7], dpi=120, facecolor=[0.9, 0.9, 0.9])

colorHexCode = ["#ff8181", "#a381ff", "#6ffd6f", "#6dd4fd", "#faff51", "#ffa5f1", "#a5ffc9", "#a5a5ff", "#01fa97",
                "#ffe350", "#d47ec6", "#9d7ed4", "#7ed4a3", "#d47e7e", "#c0a0bf", "#73d564", "#f5b850", "#dcbbdb",
                "#bbbbdc", "#e7ffbd", "#e1c122", "#c64859", "#7fb3ab", "#bcfab5",
                "#f1c5f6", "#1088ff", "#10ffa0", "#c8ff10", "#ffd810", "#ff4810", "#8010ff", "#60e6b1", "#fff600",
                "#00ddff", "#ffbb00", "#ff2a00", "#00ff08", "#bdbd4f", "#6f6d9b", "#e604df", "#04e68c", "#2ae604",
                "#04aae6", "#ff324d", "#69ff32", "#ffc932", "#a8bcbd", "#e5d934", "#16ce3b", "#7216ce"]
# fig = plt.figure(figsize=[15, 10], dpi=120, facecolor=[0.9, 0.9, 0.9])


class AboutDialogFCFS(QMainWindow):
    def __init__(self):
        super(AboutDialogFCFS, self).__init__()

        self.aboutfcfs = Ui_Dialog()
        self.aboutfcfs.setupUi(self)


class AboutDialogSSTF(QMainWindow):
    def __init__(self):
        super(AboutDialogSSTF, self).__init__()
        # self.aboutfcfs = Ui_Dialog()
        # self.aboutfcfs.setupUi(self)
        self.aboutsstf = Ui_DialogSSFT()
        self.aboutsstf.setupUi(self)


class AboutLook(QMainWindow):
    def __init__(self):
        super(AboutLook, self).__init__()
        self.aboutlook = Ui_MainWindowLook()
        self.aboutlook.setupUi(self)


class AboutcLook(QMainWindow):
    def __init__(self):
        super(AboutcLook, self).__init__()
        self.aboutclook = Ui_MainWindowCLook()
        self.aboutclook.setupUi(self)


class AboutScan(QMainWindow):
    def __init__(self):
        super(AboutScan, self).__init__()
        self.aboutscan = Ui_MainWindowScan()
        self.aboutscan.setupUi(self)


class WarningDialog(QMainWindow):
    def __init__(self):
        super(WarningDialog, self).__init__()
        self.warning = Ui_DialogWarning()
        self.warning.setupUi(self)


class AboutcScan(QMainWindow):
    def __init__(self):
        super(AboutcScan, self).__init__()
        self.aboutcscan = Ui_MainWindowCscan()
        self.aboutcscan.setupUi(self)


class UI_DiskScheduling(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 690)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 690))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 690))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(800, 0, 20, 811))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.AboutAlgo = QtWidgets.QPushButton(self.centralwidget)
        self.AboutAlgo.setGeometry(QtCore.QRect(590, 10, 211, 31))
        self.AboutAlgo.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                     "font-weight:400;")
        self.AboutAlgo.setObjectName("AboutAlgo")
        self.AboutAlgo.clicked.connect(self.about)
        self.AlgoSelect = QtWidgets.QComboBox(self.centralwidget)
        self.AlgoSelect.setGeometry(QtCore.QRect(20, 10, 231, 31))
        self.AlgoSelect.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                      "font-weight:400;\n"
                                      "text-align:center;")
        self.AlgoSelect.setObjectName("AlgoSelect")
        self.AlgoSelect.addItem("")
        self.AlgoSelect.addItem("")
        self.AlgoSelect.addItem("")
        self.AlgoSelect.addItem("")
        self.AlgoSelect.addItem("")
        self.AlgoSelect.addItem("")
        self.AlgoSelect.addItem("")
        self.AlgoSelect.addItem("")
        self.GenerateGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateGraphButton.setGeometry(QtCore.QRect(630, 510, 171, 41))
        self.GenerateGraphButton.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                               "font-weight:400;")
        self.GenerateGraphButton.setObjectName("GenerateGraphButton")
        self.GenerateGraphButton.clicked.connect(self.generateGraph)
        self.No_of_tracksLbl = QtWidgets.QLabel(self.centralwidget)
        self.No_of_tracksLbl.setGeometry(QtCore.QRect(20, 70, 181, 31))
        self.No_of_tracksLbl.setStyleSheet("font: 9pt \"Comic Sans MS\";\n"
                                           "font-weight:200;")
        self.No_of_tracksLbl.setObjectName("No_of_tracksLbl")
        self.No_of_tracks = QtWidgets.QSpinBox(self.centralwidget)
        self.No_of_tracks.setGeometry(QtCore.QRect(210, 70, 51, 31))
        self.No_of_tracks.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                        "font-weight:400;")
        self.No_of_tracks.setObjectName("No_of_tracks")
        self.Gobtn = QtWidgets.QPushButton(self.centralwidget)
        self.Gobtn.setGeometry(QtCore.QRect(320, 70, 61, 31))
        self.Gobtn.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                 "font-weight:400;")
        self.Gobtn.setObjectName("Gobtn")
        self.Gobtn.clicked.connect(self.make_row)
        self.RW_HeadLbl = QtWidgets.QLabel(self.centralwidget)
        self.RW_HeadLbl.setGeometry(QtCore.QRect(470, 70, 191, 31))
        self.RW_HeadLbl.setStyleSheet("font: 9pt \"Comic Sans MS\";\n"
                                      "font-weight:200;")
        self.RW_HeadLbl.setObjectName("RW_HeadLbl")
        self.Initial_RW_Head = QtWidgets.QLineEdit(self.centralwidget)
        self.Initial_RW_Head.setGeometry(QtCore.QRect(690, 70, 51, 31))
        self.Initial_RW_Head.setObjectName("Initial_RW_Head")
        self.ChangeTheme = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeTheme.setGeometry(QtCore.QRect(380, 10, 121, 31))
        self.ChangeTheme.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                       "font-weight:400;")
        self.ChangeTheme.setObjectName("ChangeTheme")
        self.clicked = 0
        self.ChangeTheme.clicked.connect(self.Dark_mode)
        self.RangeLabl = QtWidgets.QLabel(self.centralwidget)
        self.RangeLabl.setGeometry(QtCore.QRect(20, 130, 121, 31))
        self.RangeLabl.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                     "font-weight:400;")
        self.RangeLabl.setObjectName("RangeLabl")
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(540, 130, 121, 31))
        self.Reset.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                 "font-weight:300;")
        self.Reset.setObjectName("Reset")
        self.Reset.clicked.connect(self.reset)
        self.Solve = QtWidgets.QPushButton(self.centralwidget)
        self.Solve.setGeometry(QtCore.QRect(670, 130, 131, 31))
        self.Solve.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                 "font-weight:400;")
        self.Solve.setObjectName("Solve")
        self.Solve.clicked.connect(self.solve)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 180, 125, 480))
        self.table.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                 "font-weight:500;")
        self.table.setObjectName("table")
        self.table.setColumnCount(1)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(180, 220, 621, 41))
        self.output.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                  "font-weight:500;")
        self.output.setObjectName("output")
        self.track = QtWidgets.QLabel(self.centralwidget)
        self.track.setGeometry(QtCore.QRect(180, 340, 541, 41))
        self.track.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                 "font-weight:500;")
        self.track.setObjectName("track")
        self.Direction = QtWidgets.QComboBox(self.centralwidget)
        self.Direction.setGeometry(QtCore.QRect(360, 130, 92, 31))
        self.Direction.setObjectName("Direction")
        self.Direction.addItem("")
        self.Direction.addItem("")
        self.Direction.addItem("")
        self.EntrDirectionLbl = QtWidgets.QLabel(self.centralwidget)
        self.EntrDirectionLbl.setGeometry(QtCore.QRect(200, 130, 161, 31))
        self.EntrDirectionLbl.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                            "font-weight:400;\n"
                                            "")
        self.EntrDirectionLbl.setObjectName("EntrDirectionLbl")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(150, 130, 20, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.ExplainationLbl = QtWidgets.QLabel(self.centralwidget)
        self.ExplainationLbl.setGeometry(QtCore.QRect(820, 10, 331, 31))
        self.ExplainationLbl.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
                                           "font-weight:400;\n"
                                           "text-align:center;")
        self.ExplainationLbl.setObjectName("ExplainationLbl")
        self.Explaination = QtWidgets.QTableWidget(self.centralwidget)
        self.Explaination.setGeometry(QtCore.QRect(820, 50, 430, 610))
        self.Explaination.setObjectName("Explaination")
        self.Explaination.setColumnCount(0)
        self.Explaination.setRowCount(0)
        self.Explaination.setStyleSheet("font: 9pt \"Comic Sans MS\";\n"
                                        "font-weight:400;\n"
                                        "text-align:center;")
        self.outputS = QtWidgets.QLabel(self.centralwidget)
        self.outputS.setGeometry(QtCore.QRect(180, 270, 611, 61))
        self.outputS.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                   "font-weight:500;")
        self.outputS.setText("")
        self.outputS.setObjectName("outputS")
        self.trackm = QtWidgets.QLabel(self.centralwidget)
        self.trackm.setGeometry(QtCore.QRect(180, 400, 611, 51))
        self.trackm.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                  "font-weight:500;")
        self.trackm.setText("")
        self.trackm.setObjectName("trackm")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 510, 181, 41))
        self.pushButton.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
                                      "font-weight:400;")
        self.pushButton.clicked.connect(self.SingleGraph)
        self.pushButton.setObjectName("pushButton")
        self.seekcompare = QtWidgets.QPushButton(self.centralwidget)
        self.seekcompare.setObjectName(u"seekcompare")
        self.seekcompare.setGeometry(QtCore.QRect(360, 510, 261, 41))
        self.seekcompare.clicked.connect(self.seekGraph)
        self.seekcompare.setStyleSheet(u"font: 10pt \"Comic Sans MS\";\n"
                                       "font-weight:400;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1246, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Disk Scheduling Algorithms"))
        self.AboutAlgo.setText(_translate("MainWindow", "About Algorithm"))
        self.AlgoSelect.setItemText(0, _translate(
            "MainWindow", "-Select Algorithm-"))
        self.AlgoSelect.setItemText(1, _translate("MainWindow", "FCFS"))
        self.AlgoSelect.setItemText(2, _translate("MainWindow", "SSTF"))
        self.AlgoSelect.setItemText(3, _translate("MainWindow", "LOOK"))
        self.AlgoSelect.setItemText(4, _translate("MainWindow", "C-LOOK"))
        self.AlgoSelect.setItemText(5, _translate("MainWindow", "SCAN"))
        self.AlgoSelect.setItemText(6, _translate("MainWindow", "C-SCAN"))
        self.AlgoSelect.setItemText(7, _translate("MainWindow", "LIFO"))
        self.GenerateGraphButton.setText(
            _translate("MainWindow", "Compare Algo"))
        self.No_of_tracksLbl.setText(_translate(
            "MainWindow", "Enter Number of Tracks : "))
        self.Gobtn.setText(_translate("MainWindow", "GO"))
        self.RW_HeadLbl.setText(_translate(
            "MainWindow", "Intial R/W Head Position : "))
        self.ChangeTheme.setText(_translate("MainWindow", "Change Theme"))
        self.RangeLabl.setText(_translate("MainWindow", "Range : 0 - 199"))
        self.Reset.setText(_translate("MainWindow", "Reset"))
        self.Solve.setText(_translate("MainWindow", "Solve"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Track No."))
        self.output.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; \">Output Sequence :</span></p></body></html>"))
        self.track.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Total track movements : </span></p></body></html>"))
        self.Direction.setItemText(0, _translate("MainWindow", "       -"))
        self.Direction.setItemText(1, _translate("MainWindow", "left"))
        self.Direction.setItemText(2, _translate("MainWindow", "right"))
        self.EntrDirectionLbl.setText(
            _translate("MainWindow", "Enter Direction : "))
        self.ExplainationLbl.setText(_translate("MainWindow", "Explaination"))
        self.pushButton.setText(_translate("MainWindow", "Generate Graph"))
        self.seekcompare.setText(_translate(
            "MainWindow", "Seek Time Comparison"))

    def make_row(self):
        r = int(self.No_of_tracks.text())
        self.table.setRowCount(r)
        self.table.setColumnCount(1)
        self.table.setGeometry(QtCore.QRect(20, 180, 140, 461))
        self.table.setHorizontalHeaderItem(
            0, QtWidgets.QTableWidgetItem("Track No."))

    def solve(self):
        l = self.AlgoSelect.currentText()
        if l == "FCFS":
            r = int(self.No_of_tracks.text())
            lis = []
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            u = int(self.Initial_RW_Head.text())
            p = 0
            y = []
            for i in range(r):
                if i > 0:
                    p += abs(lis[i] - lis[i - 1])
                else:
                    p += abs(lis[0] - u)
            lis.insert(0, u)
            z = np.array(lis)
            self.printInfo(lis, p)
            self.explain(lis, l)
            return lis

        elif l == "SSTF":
            r = int(self.No_of_tracks.text())
            lis = []
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            u = int(self.Initial_RW_Head.text())
            p = 0
            q = [u]
            while(len(lis) != 0):
                dif = 200
                z = -1
                for i in lis:
                    if(abs(i-u) < dif):
                        dif = abs(i-u)
                        z = i
                u = z
                q.append(u)
                lis.remove(u)
                if(len(lis) == 1):
                    q.append(lis[0])
                    p += dif
                    break
                p += dif
            y = np.array(q)
            self.printInfo(q, p)
            self.explain(q, l)
            return q

        elif l == "LIFO":
            r = int(self.No_of_tracks.text())
            lis = []
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            lis.reverse()
            u = int(self.Initial_RW_Head.text())
            z = u
            p = 0
            for i in lis:
                p += abs(i-u)
                u = i
            lis.insert(0, z)
            self.printInfo(lis, p)
            self.explain(lis, l)
            y = np.array(lis)
            return lis

        elif l == "SCAN":
            r = int(self.No_of_tracks.text())
            lis = []
            u = int(self.Initial_RW_Head.text())
            di = self.Direction.currentText()
            if(di == 'left'):
                o = 'l'
            else:
                o = 'r'
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            p = []
            first = []
            second = []
            if u in lis:
                lis.remove(u)
            p.append(u)
            if(o == 'l'):
                for i in lis:
                    if i < u:
                        first.append(i)
                    else:
                        second.append(i)
                if 0 not in first:
                    first.insert(0, 0)
                first.sort()
                first.reverse()
                second.sort()
            else:
                for i in lis:
                    if i > u:
                        first.append(i)
                    else:
                        second.append(i)
                if 199 not in first:
                    first.append(199)
                first.sort()
                second.sort()
                second.reverse()
            for i in first:
                p.append(i)
            for i in second:
                p.append(i)
            cost = 0
            qw = len(p)
            for i in range(1, qw):
                cost += abs(p[i]-p[i-1])
            self.printInfo(p, cost)
            self.explain(p, l)
            y = np.array(p)
            return p

        elif l == 'C-SCAN':
            r = int(self.No_of_tracks.text())
            lis = []
            u = int(self.Initial_RW_Head.text())
            di = self.Direction.currentText()
            if(di == 'left'):
                o = 'l'
            else:
                o = 'r'
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            p = []
            first = []
            second = []
            if u in lis:
                lis.remove(u)
            p.append(u)
            if o == 'l':
                for i in lis:
                    if i < u:
                        first.append(i)
                    else:
                        second.append(i)
                if 0 not in first:
                    first.append(0)
                if 199 not in second:
                    second.append(199)
                first.sort()
                first.reverse()
                second.sort()
                second.reverse()
            else:
                for i in lis:
                    if i > u:
                        first.append(i)
                    else:
                        second.append(i)
                if 199 not in first:
                    first.append(199)
                if 0 not in second:
                    second.append(0)
                first.sort()
                second.sort()
            for i in first:
                p.append(i)
            for i in second:
                p.append(i)
            cost = 0
            qw = len(p)
            for i in range(1, qw):
                cost += abs(p[i]-p[i-1])
            y = np.array(p)
            self.explain(p, l)
            self.printInfo(p, cost)
            return p

        elif l == 'LOOK':
            r = int(self.No_of_tracks.text())
            lis = []
            u = int(self.Initial_RW_Head.text())
            di = self.Direction.currentText()
            if(di == 'left'):
                o = 'l'
            else:
                o = 'r'
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            p = []
            first = []
            second = []
            if u in lis:
                lis.remove(u)
            p.append(u)
            if(o == 'l'):
                for i in lis:
                    if i < u:
                        first.append(i)
                    else:
                        second.append(i)
                first.sort()
                first.reverse()
                second.sort()
            else:
                for i in lis:
                    if i > u:
                        first.append(i)
                    else:
                        second.append(i)
                first.sort()
                second.sort()
                second.reverse()
            for i in first:
                p.append(i)
            for i in second:
                p.append(i)
            cost = 0
            qw = len(p)
            for i in range(1, qw):
                cost += abs(p[i]-p[i-1])
            y = np.array(p)
            self.printInfo(p, cost)
            self.explain(p, l)
            return p

        elif l == 'C-LOOK':
            r = int(self.No_of_tracks.text())
            lis = []
            u = int(self.Initial_RW_Head.text())
            di = self.Direction.currentText()
            if(di == 'left'):
                o = 'l'
            else:
                o = 'r'
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            p = []
            first = []
            second = []
            if u in lis:
                lis.remove(u)
            p.append(u)
            if o == 'l':
                for i in lis:
                    if i < u:
                        first.append(i)
                    else:
                        second.append(i)
                # if 0 not in first:first.append(0)
                # if 199 not in second:second.append(199)
                first.sort()
                first.reverse()
                second.sort()
                second.reverse()
            else:
                for i in lis:
                    if i > u:
                        first.append(i)
                    else:
                        second.append(i)
                # if 199 not in first:first.append(199)
                # if 0 not in second:second.append(0)
                first.sort()
                second.sort()
            for i in first:
                p.append(i)
            for i in second:
                p.append(i)
            cost = 0
            qw = len(p)
            for i in range(1, qw):
                cost += abs(p[i]-p[i-1])
            y = np.array(p)
            self.explain(p, l)
            self.printInfo(p, cost)
            return p

    def SingleGraph(self):
        l = self.AlgoSelect.currentText()
        if l == "FCFS":
            r = int(self.No_of_tracks.text())
            lis = []
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            u = int(self.Initial_RW_Head.text())
            p = 0
            y = []
            for i in range(r):
                if i > 0:
                    p += abs(lis[i] - lis[i - 1])
                else:
                    p += abs(lis[0] - u)
            lis.insert(0, u)
            z = np.array(lis)
            self.graph(z, l)
            return lis

        elif l == "SSTF":
            r = int(self.No_of_tracks.text())
            lis = []
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            u = int(self.Initial_RW_Head.text())
            p = 0
            q = [u]
            while(len(lis) != 0):
                dif = 200
                z = -1
                for i in lis:
                    if(abs(i-u) < dif):
                        dif = abs(i-u)
                        z = i
                u = z
                q.append(u)
                lis.remove(u)
                if(len(lis) == 1):
                    q.append(lis[0])
                    break
                p += dif
            y = np.array(q)
            self.graph(q, l)
            return q

        elif l == "LIFO":
            r = int(self.No_of_tracks.text())
            lis = []
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            lis.reverse()
            u = int(self.Initial_RW_Head.text())
            z = u
            p = 0
            for i in lis:
                p += abs(i-u)
                u = i
            lis.insert(0, z)
            y = np.array(lis)
            self.graph(y, l)
            return lis

        elif l == "SCAN":
            r = int(self.No_of_tracks.text())
            lis = []
            u = int(self.Initial_RW_Head.text())
            di = self.Direction.currentText()
            if(di == 'left'):
                o = 'l'
            else:
                o = 'r'
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            p = []
            first = []
            second = []
            if u in lis:
                lis.remove(u)
            p.append(u)
            if(o == 'l'):
                for i in lis:
                    if i < u:
                        first.append(i)
                    else:
                        second.append(i)
                if 0 not in first:
                    first.insert(0, 0)
                first.sort()
                first.reverse()
                second.sort()
            else:
                for i in lis:
                    if i > u:
                        first.append(i)
                    else:
                        second.append(i)
                if 199 not in first:
                    first.append(199)
                first.sort()
                second.sort()
                second.reverse()
            for i in first:
                p.append(i)
            for i in second:
                p.append(i)
            cost = 0
            qw = len(p)
            for i in range(1, qw):
                cost += abs(p[i]-p[i-1])
            y = np.array(p)
            self.graph(y, l)
            return p

        elif l == 'C-SCAN':
            r = int(self.No_of_tracks.text())
            lis = []
            u = int(self.Initial_RW_Head.text())
            di = self.Direction.currentText()
            if(di == 'left'):
                o = 'l'
            else:
                o = 'r'
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            p = []
            first = []
            second = []
            if u in lis:
                lis.remove(u)
            p.append(u)
            if o == 'l':
                for i in lis:
                    if i < u:
                        first.append(i)
                    else:
                        second.append(i)
                if 0 not in first:
                    first.append(0)
                if 199 not in second:
                    second.append(199)
                first.sort()
                first.reverse()
                second.sort()
                second.reverse()
            else:
                for i in lis:
                    if i > u:
                        first.append(i)
                    else:
                        second.append(i)
                if 199 not in first:
                    first.append(199)
                if 0 not in second:
                    second.append(0)
                first.sort()
                second.sort()
            for i in first:
                p.append(i)
            for i in second:
                p.append(i)
            cost = 0
            qw = len(p)
            for i in range(1, qw):
                cost += abs(p[i]-p[i-1])
            y = np.array(p)
            self.graph(y, l)
            return p

        elif l == 'LOOK':
            r = int(self.No_of_tracks.text())
            lis = []
            u = int(self.Initial_RW_Head.text())
            di = self.Direction.currentText()
            if(di == 'left'):
                o = 'l'
            else:
                o = 'r'
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            p = []
            first = []
            second = []
            if u in lis:
                lis.remove(u)
            p.append(u)
            if(o == 'l'):
                for i in lis:
                    if i < u:
                        first.append(i)
                    else:
                        second.append(i)
                first.sort()
                first.reverse()
                second.sort()
            else:
                for i in lis:
                    if i > u:
                        first.append(i)
                    else:
                        second.append(i)
                first.sort()
                second.sort()
                second.reverse()
            for i in first:
                p.append(i)
            for i in second:
                p.append(i)
            cost = 0
            qw = len(p)
            for i in range(1, qw):
                cost += abs(p[i]-p[i-1])
            y = np.array(p)
            self.graph(y, l)
            return p

        elif l == 'C-LOOK':
            r = int(self.No_of_tracks.text())
            lis = []
            u = int(self.Initial_RW_Head.text())
            di = self.Direction.currentText()
            if(di == 'left'):
                o = 'l'
            else:
                o = 'r'
            for i in range(r):
                item = self.table.item(i, 0)
                lis.append(int(item.text()))
            p = []
            first = []
            second = []
            if u in lis:
                lis.remove(u)
            p.append(u)
            if o == 'l':
                for i in lis:
                    if i < u:
                        first.append(i)
                    else:
                        second.append(i)
                # if 0 not in first:first.append(0)
                # if 199 not in second:second.append(199)
                first.sort()
                first.reverse()
                second.sort()
                second.reverse()
            else:
                for i in lis:
                    if i > u:
                        first.append(i)
                    else:
                        second.append(i)
                # if 199 not in first:first.append(199)
                # if 0 not in second:second.append(0)
                first.sort()
                second.sort()
            for i in first:
                p.append(i)
            for i in second:
                p.append(i)
            cost = 0
            qw = len(p)
            for i in range(1, qw):
                cost += abs(p[i]-p[i-1])
            y = np.array(p)
            self.graph(y, l)
            return p

    def Dark_mode(self):
        if self.clicked == 0:
            qtmodern.styles.dark(app)
            self.clicked = 1
        elif self.clicked == 1:
            qtmodern.styles.light(app)
            self.clicked = 0

    def reset(self):
        self.table.setRowCount(0)
        self.Explaination.setRowCount(0)
        self.Explaination.setColumnCount(0)
        self.Initial_RW_Head.setText("")
        self.No_of_tracks.setValue(0)
        self.AlgoSelect.setCurrentIndex(0)
        self.table.setGeometry(QtCore.QRect(20, 180, 125, 461))
        self.outputS.setText("")
        self.trackm.setText("")

    def about(self):
        if self.AlgoSelect.currentText() == "-Select Algorithm-":
            self.warning = WarningDialog()
            self.warning.setWindowTitle("Alert")
            self.warning.show()

        elif self.AlgoSelect.currentText() == "FCFS":
            self.dialog = AboutDialogFCFS()
            self.dialog.setWindowTitle("About FCFS Algorithm")
            self.dialog.show()

        elif self.AlgoSelect.currentText() == "SSTF":
            self.aboutsstf = AboutDialogSSTF()
            self.aboutsstf.setWindowTitle("About SSTF Algorithm")
            self.aboutsstf.show()

        elif self.AlgoSelect.currentText() == "LOOK":
            self.aboutlook = AboutLook()
            self.aboutlook.setWindowTitle("About LOOK Algorithm")
            self.aboutlook.show()

        elif self.AlgoSelect.currentText() == "C-LOOK":
            self.aboutclook = AboutcLook()
            self.aboutclook.setWindowTitle("About C-LOOK Algorithm")
            self.aboutclook.show()

        elif self.AlgoSelect.currentText() == "C-SCAN":
            self.aboutcscan = AboutcScan()
            self.aboutcscan.setWindowTitle("About C-SCAN Algorithm")
            self.aboutcscan.show()

        elif self.AlgoSelect.currentText() == "SCAN":
            self.aboutscan = AboutScan()
            self.aboutscan.setWindowTitle("About SCAN Algorithm")
            self.aboutscan.show()

    def graph(self, lis, l):
        plt.plot(lis, marker="o", color=colorHexCode[0])
        plt.xlabel("Order of Arrival")
        plt.ylabel("Track Numbers")
        plt.title(l)
        plt.ylim(0, 210)
        scale_x = 1
        plt.show()

    def printInfo(self, q, p):
        self.outputS.setText(str(q))
        self.trackm.setText(
            "The total numbers of seek movements are : " + str(p) + ".")

    def generateGraph(self):
        r = int(self.No_of_tracks.text())
        lis = []
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        u = int(self.Initial_RW_Head.text())
        y = []
        lis.insert(0, u)
        z1 = np.array(lis)

        r = int(self.No_of_tracks.text())
        lis = []
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        u = int(self.Initial_RW_Head.text())
        p = 0
        l = len(lis)
        q = [u]
        while(len(lis) != 0):
            dif = 200
            z = -1
            for i in lis:
                if(abs(i-u) < dif):
                    dif = abs(i-u)
                    z = i
            u = z
            q.append(u)
            lis.remove(u)
            if(len(lis) == 1):
                q.append(lis[0])
                break
            p += dif
        z2 = np.array(q)

        r = int(self.No_of_tracks.text())
        lis = []
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        lis.reverse()
        u = int(self.Initial_RW_Head.text())
        z = u
        lis.insert(0, z)
        self.printInfo(lis, p)
        z3 = np.array(lis)

        r = int(self.No_of_tracks.text())
        lis = []
        u = int(self.Initial_RW_Head.text())
        di = self.Direction.currentText()
        if(di == 'left'):
            o = 'l'
        else:
            o = 'r'
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        p = []
        first = []
        second = []
        if u in lis:
            lis.remove(u)
        p.append(u)
        if(o == 'l'):
            for i in lis:
                if i < u:
                    first.append(i)
                else:
                    second.append(i)
            if 0 not in first:
                first.insert(0, 0)
            first.sort()
            first.reverse()
            second.sort()
        else:
            for i in lis:
                if i > u:
                    first.append(i)
                else:
                    second.append(i)
            if 199 not in first:
                first.append(199)
            first.sort()
            second.sort()
            second.reverse()
        for i in first:
            p.append(i)
        for i in second:
            p.append(i)
        cost = 0
        qw = len(p)
        for i in range(1, qw):
            cost += abs(p[i]-p[i-1])
        self.printInfo(p, cost)
        z4 = np.array(p)

        r = int(self.No_of_tracks.text())
        lis = []
        u = int(self.Initial_RW_Head.text())
        di = self.Direction.currentText()
        if(di == 'left'):
            o = 'l'
        else:
            o = 'r'
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        p = []
        first = []
        second = []
        if u in lis:
            lis.remove(u)
        p.append(u)
        if o == 'l':
            for i in lis:
                if i < u:
                    first.append(i)
                else:
                    second.append(i)
            if 0 not in first:
                first.append(0)
            if 199 not in second:
                second.append(199)
            first.sort()
            first.reverse()
            second.sort()
            second.reverse()
        else:
            for i in lis:
                if i > u:
                    first.append(i)
                else:
                    second.append(i)
            if 199 not in first:
                first.append(199)
            if 0 not in second:
                second.append(0)
            first.sort()
            second.sort()
        for i in first:
            p.append(i)
        for i in second:
            p.append(i)
        cost = 0
        qw = len(p)
        for i in range(1, qw):
            cost += abs(p[i]-p[i-1])
        z5 = np.array(p)

        r = int(self.No_of_tracks.text())
        lis = []
        u = int(self.Initial_RW_Head.text())
        di = self.Direction.currentText()
        if(di == 'left'):
            o = 'l'
        else:
            o = 'r'
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        p = []
        first = []
        second = []
        if u in lis:
            lis.remove(u)
        p.append(u)
        if(o == 'l'):
            for i in lis:
                if i < u:
                    first.append(i)
                else:
                    second.append(i)
            first.sort()
            first.reverse()
            second.sort()
        else:
            for i in lis:
                if i > u:
                    first.append(i)
                else:
                    second.append(i)
            first.sort()
            second.sort()
            second.reverse()
        for i in first:
            p.append(i)
        for i in second:
            p.append(i)
        cost = 0
        qw = len(p)
        for i in range(1, qw):
            cost += abs(p[i]-p[i-1])
        z6 = np.array(p)

        r = int(self.No_of_tracks.text())
        lis = []
        u = int(self.Initial_RW_Head.text())
        di = self.Direction.currentText()
        if(di == 'left'):
            o = 'l'
        else:
            o = 'r'
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        p = []
        first = []
        second = []
        if u in lis:
            lis.remove(u)
        p.append(u)
        if o == 'l':
            for i in lis:
                if i < u:
                    first.append(i)
                else:
                    second.append(i)
            # if 0 not in first:first.append(0)
            # if 199 not in second:second.append(199)
            first.sort()
            first.reverse()
            second.sort()
            second.reverse()
        else:
            for i in lis:
                if i > u:
                    first.append(i)
                else:
                    second.append(i)
            # if 199 not in first:first.append(199)
            # if 0 not in second:second.append(0)
            first.sort()
            second.sort()
        for i in first:
            p.append(i)
        for i in second:
            p.append(i)
        cost = 0
        qw = len(p)
        for i in range(1, qw):
            cost += abs(p[i]-p[i-1])
        z7 = np.array(p)

        plt.plot(z1, marker="o", color=colorHexCode[0], label="FCFS")
        plt.plot(z2, marker="o", color=colorHexCode[1], label="SSTF")
        plt.plot(z3, marker="o", color=colorHexCode[2], label="LIFO")
        plt.plot(z4, marker="o", color=colorHexCode[3], label="SCAN")
        plt.plot(z5, marker="o", color=colorHexCode[4], label="C-SCAN")
        plt.plot(z6, marker="o", color=colorHexCode[5], label="LOOK")
        plt.plot(z7, marker="o", color=colorHexCode[6], label="C-LOOK")
        plt.ylim(0, 210)
        plt.xlabel("Order of Arrival")
        plt.ylabel("Track Numbers")
        plt.title("Comparison of Algorithms")
        plt.legend()
        plt.show()

    def explain(self, lis, l):
        self.Explaination.setColumnCount(1)
        self.Explaination.setRowCount(len(lis))
        self.Explaination.setColumnWidth(0, 410)
        self.Explaination.setHorizontalHeaderItem(
            0, QtWidgets.QTableWidgetItem(""))
        for i in range(len(lis)):
            if i == 0:
                text = QtWidgets.QTableWidgetItem(
                    "Initially R/W head is at "+str(lis[0])+" .")
                text.setTextAlignment(QtCore.Qt.AlignCenter)
                self.Explaination.setItem(i, 0, text)
            else:
                s = l
                o = str(s)
                text = QtWidgets.QTableWidgetItem(
                    "As algorithm is "+o+" it will go from "+str(lis[i-1])+" to "+str(lis[i])+" .")
                text.setTextAlignment(QtCore.Qt.AlignCenter)
                self.Explaination.setItem(i, 0, text)

    def seekGraph(self):
        l = self.AlgoSelect.currentText()
        r = int(self.No_of_tracks.text())
        lis = []
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        u = int(self.Initial_RW_Head.text())
        cost1 = 0
        y = []
        for i in range(r):
            if i > 0:
                cost1 += abs(lis[i] - lis[i - 1])
            else:
                cost1 += abs(lis[0] - u)

        r = int(self.No_of_tracks.text())
        lis = []
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        u = int(self.Initial_RW_Head.text())
        cost2 = 0
        q = [u]
        while(len(lis) != 0):
            dif = 200
            z = -1
            for i in lis:
                if(abs(i-u) < dif):
                    dif = abs(i-u)
                    z = i
            u = z
            q.append(u)
            lis.remove(u)
            if(len(lis) == 1):
                q.append(lis[0])
                cost2 += dif
                break
            cost2 += dif

        r = int(self.No_of_tracks.text())
        lis = []
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        lis.reverse()
        u = int(self.Initial_RW_Head.text())
        z = u
        cost3 = 0
        for i in lis:
            cost3 += abs(i-u)
            u = i

        r = int(self.No_of_tracks.text())
        lis = []
        u = int(self.Initial_RW_Head.text())
        di = self.Direction.currentText()
        if(di == 'left'):
            o = 'l'
        else:
            o = 'r'
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        p = []
        first = []
        second = []
        if u in lis:
            lis.remove(u)
        p.append(u)
        if(o == 'l'):
            for i in lis:
                if i < u:
                    first.append(i)
                else:
                    second.append(i)
            if 0 not in first:
                first.insert(0, 0)
            first.sort()
            first.reverse()
            second.sort()
        else:
            for i in lis:
                if i > u:
                    first.append(i)
                else:
                    second.append(i)
            if 199 not in first:
                first.append(199)
            first.sort()
            second.sort()
            second.reverse()
        for i in first:
            p.append(i)
        for i in second:
            p.append(i)
        cost4 = 0
        qw = len(p)
        for i in range(1, qw):
            cost4 += abs(p[i]-p[i-1])

        r = int(self.No_of_tracks.text())
        lis = []
        u = int(self.Initial_RW_Head.text())
        di = self.Direction.currentText()
        if(di == 'left'):
            o = 'l'
        else:
            o = 'r'
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        p = []
        first = []
        second = []
        if u in lis:
            lis.remove(u)
        p.append(u)
        if o == 'l':
            for i in lis:
                if i < u:
                    first.append(i)
                else:
                    second.append(i)
            if 0 not in first:
                first.append(0)
            if 199 not in second:
                second.append(199)
            first.sort()
            first.reverse()
            second.sort()
            second.reverse()
        else:
            for i in lis:
                if i > u:
                    first.append(i)
                else:
                    second.append(i)
            if 199 not in first:
                first.append(199)
            if 0 not in second:
                second.append(0)
            first.sort()
            second.sort()
        for i in first:
            p.append(i)
        for i in second:
            p.append(i)
        cost5 = 0
        qw = len(p)
        for i in range(1, qw):
            cost5 += abs(p[i]-p[i-1])

        r = int(self.No_of_tracks.text())
        lis = []
        u = int(self.Initial_RW_Head.text())
        di = self.Direction.currentText()
        if(di == 'left'):
            o = 'l'
        else:
            o = 'r'
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        p = []
        first = []
        second = []
        if u in lis:
            lis.remove(u)
        p.append(u)
        if(o == 'l'):
            for i in lis:
                if i < u:
                    first.append(i)
                else:
                    second.append(i)
            first.sort()
            first.reverse()
            second.sort()
        else:
            for i in lis:
                if i > u:
                    first.append(i)
                else:
                    second.append(i)
            first.sort()
            second.sort()
            second.reverse()
        for i in first:
            p.append(i)
        for i in second:
            p.append(i)
        cost6 = 0
        qw = len(p)
        for i in range(1, qw):
            cost6 += abs(p[i]-p[i-1])

        r = int(self.No_of_tracks.text())
        lis = []
        u = int(self.Initial_RW_Head.text())
        di = self.Direction.currentText()
        if(di == 'left'):
            o = 'l'
        else:
            o = 'r'
        for i in range(r):
            item = self.table.item(i, 0)
            lis.append(int(item.text()))
        p = []
        first = []
        second = []
        if u in lis:
            lis.remove(u)
        p.append(u)
        if o == 'l':
            for i in lis:
                if i < u:
                    first.append(i)
                else:
                    second.append(i)
            # if 0 not in first:first.append(0)
            # if 199 not in second:second.append(199)
            first.sort()
            first.reverse()
            second.sort()
            second.reverse()
        else:
            for i in lis:
                if i > u:
                    first.append(i)
                else:
                    second.append(i)
            # if 199 not in first:first.append(199)
            # if 0 not in second:second.append(0)
            first.sort()
            second.sort()
        for i in first:
            p.append(i)
        for i in second:
            p.append(i)
        cost7 = 0
        qw = len(p)
        for i in range(1, qw):
            cost7 += abs(p[i]-p[i-1])

        plt.bar(["FCFS", "SSTF", "LIFO", "SCAN", "C-SCAN", "LOOK", "C-LOOK"], [cost1, cost2, cost3, cost4, cost5, cost6, cost7],
                color=[colorHexCode[0], colorHexCode[1], colorHexCode[2], colorHexCode[3], colorHexCode[4], colorHexCode[5], colorHexCode[6]])
        plt.xlabel("Algorithms")
        plt.ylabel("Seek Time")
        plt.title("Seek Time Comparison")
        plt.show()


if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_DiskScheduling()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # sys.exit(app.exec_())
app = QtWidgets.QApplication(sys.argv)
qtmodern.styles.dark(app)