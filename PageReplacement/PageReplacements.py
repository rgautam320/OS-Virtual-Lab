import random
from PyQt5.QtWidgets import QMainWindow
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets

from PageReplacement.src.about_PageReplacement import UI_About_PageReplacement


class UI_PageReplacement(QMainWindow):

    def gotoAboutPage(self):
        self.aboutPage = QtWidgets.QWidget()
        self.ui = UI_About_PageReplacement()
        self.ui.setupUi(self.aboutPage)
        self.aboutPage.show()

    def setupUi(self, PageReplacement):
        PageReplacement.setObjectName("PageReplacement")
        PageReplacement.resize(1280, 690)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            PageReplacement.sizePolicy().hasHeightForWidth())
        PageReplacement.setSizePolicy(sizePolicy)
        PageReplacement.setMinimumSize(QtCore.QSize(1280, 690))
        PageReplacement.setMaximumSize(QtCore.QSize(1280, 690))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        PageReplacement.setPalette(palette)
        PageReplacement.setStyleSheet("/*background-color: rgb(50, 50, 50);*/\n"
                                      "background-color: rgb(255, 255, 255);")
        PageReplacement.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(PageReplacement)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1281, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hl1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hl1.setContentsMargins(0, 0, 0, 0)
        self.hl1.setObjectName("hl1")
        self.heading = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setStyleSheet("background-color: rgb(34, 255, 0);")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.hl1.addWidget(self.heading)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(
            QtCore.QRect(10, 70, 461, 361))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.horizontalLayoutWidget_6)
        self.verticalLayout.setContentsMargins(10, 0, 10, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.no_frame = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.no_frame.setFont(font)
        self.no_frame.setObjectName("no_frame")
        self.verticalLayout.addWidget(self.no_frame)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QtCore.QSize(0, 40))
        self.spinBox.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.spinBox.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                   "border: 2px solid rgb(0, 255, 0);\n"
                                   "border-radius: 20px;")
        self.spinBox.setWrapping(True)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setMinimum(0)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        self.page_sequence = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.page_sequence.setFont(font)
        self.page_sequence.setObjectName("page_sequence")
        self.verticalLayout.addWidget(self.page_sequence)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                    "padding: 10px;\n"
                                    "border: 2px solid rgb(0, 255, 0);\n"
                                    "border-radius: 20px;")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.choose_algorithm = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.choose_algorithm.setFont(font)
        self.choose_algorithm.setObjectName("choose_algorithm")
        self.verticalLayout.addWidget(self.choose_algorithm)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 50))
        self.comboBox.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox.setStyleSheet("padding: 10px;\n"
                                    "background-color: rgb(240, 242, 240);\n"
                                    "margin-right: 1px;\n"
                                    "border: 2px solid rgb(0, 255, 0);\n"
                                    "border-radius: 10px;")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxCount(10)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setSizeAdjustPolicy(
            QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setPlaceholderText("")
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 5, 10, 5)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_graph = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_graph.sizePolicy().hasHeightForWidth())
        self.btn_graph.setSizePolicy(sizePolicy)
        self.btn_graph.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_graph.setFont(font)
        self.btn_graph.setStyleSheet("border: 2px solid rgb(0, 0, 255);\n"
                                     "border-radius: 20px;\n"
                                     "background-color: rgb(0, 0, 255);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "")
        self.btn_graph.setObjectName("btn_graph")
        self.gridLayout.addWidget(self.btn_graph, 0, 2, 1, 1)
        self.btn_run = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_run.sizePolicy().hasHeightForWidth())
        self.btn_run.setSizePolicy(sizePolicy)
        self.btn_run.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_run.setFont(font)
        self.btn_run.setStyleSheet("border: 2px solid rgb(0, 0, 255);\n"
                                   "border-radius: 20px;\n"
                                   "background-color: rgb(0, 0, 255);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "")
        self.btn_run.setObjectName("btn_run")
        self.gridLayout.addWidget(self.btn_run, 0, 1, 1, 1)
        self.btn_compare = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_compare.sizePolicy().hasHeightForWidth())
        self.btn_compare.setSizePolicy(sizePolicy)
        self.btn_compare.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_compare.setFont(font)
        self.btn_compare.setStyleSheet("border: 2px solid rgb(0, 0, 255);\n"
                                       "border-radius: 20px;\n"
                                       "background-color: rgb(0, 0, 255);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "\n"
                                       "")
        self.btn_compare.setObjectName("btn_compare")
        self.gridLayout.addWidget(self.btn_compare, 1, 2, 1, 1)
        self.btn_explanation = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_explanation.sizePolicy().hasHeightForWidth())
        self.btn_explanation.setSizePolicy(sizePolicy)
        self.btn_explanation.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_explanation.setFont(font)
        self.btn_explanation.setStyleSheet("border: 2px solid rgb(0, 0, 255);\n"
                                           "border-radius: 20px;\n"
                                           "background-color: rgb(0, 0, 255);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "\n"
                                           "")
        self.btn_explanation.setObjectName("btn_explanation")
        self.gridLayout.addWidget(self.btn_explanation, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 439, 921, 241))
        self.table.setStyleSheet("")
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(940, 500, 331, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.v_report = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.v_report.setContentsMargins(10, 10, 10, 0)
        self.v_report.setSpacing(5)
        self.v_report.setObjectName("v_report")
        self.t_hit = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t_hit.setFont(font)
        self.t_hit.setObjectName("t_hit")
        self.v_report.addWidget(self.t_hit)
        self.t_fault = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t_fault.setFont(font)
        self.t_fault.setObjectName("t_fault")
        self.v_report.addWidget(self.t_fault)
        self.hit_rate = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.hit_rate.setFont(font)
        self.hit_rate.setObjectName("hit_rate")
        self.v_report.addWidget(self.hit_rate)
        self.fault_rate = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fault_rate.setFont(font)
        self.fault_rate.setObjectName("fault_rate")
        self.v_report.addWidget(self.fault_rate)
        self.explain_table = QtWidgets.QTableWidget(self.centralwidget)
        self.explain_table.setGeometry(QtCore.QRect(480, 70, 791, 361))
        self.explain_table.setObjectName("explain_table")
        self.explain_table.setColumnCount(0)
        self.explain_table.setRowCount(0)
        self.btn_desc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_desc.setGeometry(QtCore.QRect(990, 440, 221, 50))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_desc.sizePolicy().hasHeightForWidth())
        self.btn_desc.setSizePolicy(sizePolicy)
        self.btn_desc.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_desc.setFont(font)
        self.btn_desc.setStyleSheet("border: 2px solid rgb(0, 0, 255);\n"
                                    "border-radius: 20px;\n"
                                    "background-color: rgb(0, 0, 255);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "\n"
                                    "")
        self.btn_desc.setObjectName("btn_desc")
        PageReplacement.setCentralWidget(self.centralwidget)

        stylesheet_horizontal = "QHeaderView::section{" \
                                "Background-color:rgb(0,0,255); " \
                                "color: white; " \
                                "font-size: 22px; " \
                                "height: 45px;}"
        stylesheet_vertical = "QHeaderView::section{" \
                              "Background-color:rgb(128, 128, 0); " \
                              "color: white; " \
                              "font-size: 18px;" \
                              "font-weight: bold;" \
                              "width: 110px;}"

        self.table.horizontalHeader().setStyleSheet(stylesheet_horizontal)
        self.table.verticalHeader().setStyleSheet(stylesheet_vertical)

        self.explain_table.horizontalHeader().setStyleSheet(stylesheet_horizontal)
        self.explain_table.verticalHeader().setStyleSheet(stylesheet_vertical)

        self.retranslateUi(PageReplacement)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PageReplacement)

        self.btn_run.clicked.connect(self.Algorithm)
        self.btn_graph.clicked.connect(self.graph)
        self.btn_explanation.clicked.connect(self.explanation)
        self.btn_compare.clicked.connect(self.compare)

        self.btn_desc.clicked.connect(self.gotoAboutPage)

    def retranslateUi(self, PageReplacement):
        _translate = QtCore.QCoreApplication.translate
        PageReplacement.setWindowTitle(_translate(
            "PageReplacement", "Page Replacement Algorithm"))
        self.heading.setText(_translate("PageReplacement",
                                        "<html><head/><body><p><span style=\" color:#ffffff;\">Page Replacement Algorithm with Belady\'s Anomaly</span></p></body></html>"))
        self.no_frame.setText(_translate(
            "PageReplacement", "Number of Frames: "))
        self.page_sequence.setText(_translate(
            "PageReplacement", "Page Sequence:"))
        self.choose_algorithm.setText(_translate(
            "PageReplacement", "Choose an Algorithm"))
        self.comboBox.setCurrentText(_translate("PageReplacement", "FIFO"))
        self.comboBox.setItemText(0, _translate("PageReplacement", "FIFO"))
        self.comboBox.setItemText(1, _translate("PageReplacement", "LIFO"))
        self.comboBox.setItemText(2, _translate("PageReplacement", "LRU"))
        self.comboBox.setItemText(3, _translate("PageReplacement", "OPR"))
        self.comboBox.setItemText(4, _translate("PageReplacement", "RPR"))
        self.comboBox.setItemText(5, _translate("PageReplacement", "SCR"))
        self.btn_graph.setText(_translate("PageReplacement", "Graph"))
        self.btn_run.setText(_translate("PageReplacement", "Run"))
        self.btn_compare.setText(_translate("PageReplacement", "Compare"))
        self.btn_explanation.setText(_translate("PageReplacement", "Explain"))
        self.t_hit.setText(_translate("PageReplacement", "Total Hit: "))
        self.t_fault.setText(_translate("PageReplacement", "Total Fault: "))
        self.hit_rate.setText(_translate("PageReplacement", "Hit Rate:"))
        self.fault_rate.setText(_translate("PageReplacement", "Fault Rate:"))
        self.btn_desc.setText(_translate("PageReplacement", "Description"))

    def pageFault_FIFO(self, frame, ref):
        pageFaults = 0
        top = 0
        fifo_lst = []
        for i in ref:
            if i not in fifo_lst:
                if len(fifo_lst) < frame:
                    fifo_lst.append(i)
                else:
                    fifo_lst[top] = i
                    top = (top + 1) % frame
                pageFaults += 1

        return pageFaults

    def pageFault_LIFO(self, x, ref):
        pagefaults = 0
        hitrate = 0
        frames = []
        y = len(ref)
        i = 0
        while (i < y):
            while (i < y and len(frames) < x):
                if (ref[i] not in frames):
                    frames.append(ref[i])
                    pagefaults += 1
                else:
                    frames.remove(ref[i])
                    frames.append(ref[i])
                    hitrate += 1
                i += 1
            if (i >= y):
                break
            if (ref[i] not in frames):
                frames.pop()
                frames.append(ref[i])
                pagefaults += 1
            else:
                hitrate += 1
            i += 1
        return pagefaults

    def pageFault_LRU(self, frame, ref):
        pageFaults = 0
        lru_lst = []
        st = []

        for i in ref:
            if i not in lru_lst:
                if len(lru_lst) < frame:
                    lru_lst.append(i)
                    st.append(len(lru_lst) - 1)
                else:
                    ind = st.pop(0)
                    lru_lst[ind] = i
                    st.append(ind)
                pageFaults += 1

            else:
                st.append(st.pop(st.index(lru_lst.index(i))))

        return pageFaults

    def pageFault_OPR(self, frame, ref):
        pageFaults = 0
        opr_lst = []
        occurance = [None for i in range(frame)]
        for i in range(len(ref)):
            if ref[i] not in opr_lst:
                if len(opr_lst) < frame:
                    opr_lst.append(ref[i])

                else:
                    for x in range(len(opr_lst)):
                        if opr_lst[x] not in ref[i + 1:]:
                            opr_lst[x] = ref[i]
                            break
                        else:
                            occurance[x] = ref[i + 1:].index(opr_lst[x])
                    else:
                        opr_lst[occurance.index(max(occurance))] = ref[i]
                pageFaults += 1

        return pageFaults

    def pageFault_RPR(self, frame, ref):
        ran_val = random.randint(0, frame - 1)
        pageFaults = 0
        rpr_lst = []
        for i in ref:
            if i not in rpr_lst:
                if len(rpr_lst) < frame:
                    rpr_lst.append(i)
                else:
                    rpr_lst[ran_val] = i
                pageFaults += 1

        return pageFaults

    class secondChance:
        count = 0

        def findAndUpdate(self, x, stack, second_chance, frame):
            for i in range(frame):
                if x == stack[i]:
                    index = i
                    if not second_chance[index]:
                        second_chance[index] = True
                    elif second_chance[index]:
                        pass
                    return True

            return False

        def replaceAndUpdate(self, x, stack, second_chance, frame, pointer):
            self.count = self.count + 1
            while True:
                if not second_chance[pointer]:
                    stack[pointer] = x
                    return (pointer + 1) % frame

                second_chance[pointer] = False
                pointer = (pointer + 1) % frame

        def PageFault_SC(self, frame, ref):
            pointer = 0
            pf = 0
            stack = [-1] * frame
            second_chance = [False] * frame
            for i in range(len(ref)):
                y = ref[i]
                if not self.findAndUpdate(y, stack, second_chance, frame):
                    pointer = self.replaceAndUpdate(
                        y, stack, second_chance, frame, pointer)
                    pf = pf + 1

            return pf

    def Algorithm(self):
        frame = self.spinBox.text()
        frame = int(frame)

        my_pages = self.lineEdit.text()
        pages = my_pages.split()

        count = 0
        chance_count = 0
        no_chance = 0

        val = self.comboBox.currentIndex()

        if val == 0:
            stack = []
            hit_stack = []
            count = 0
            fault = 0
            self.table.setRowCount(frame + 1)
            self.table.setColumnCount(len(pages))

            for i in range(len(pages)):
                tablerow = 0
                self.table.setColumnWidth(i, 80)
                self.table.setRowHeight(i, 42)
                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(frame, i, item)

                self.table.item(frame, i).setBackground(
                    QtGui.QColor(0, 125, 125))
                self.table.item(frame, i).setForeground(
                    QtGui.QColor(255, 255, 255))

                for v_head in range(frame):
                    item = QtWidgets.QTableWidgetItem(
                        "Frame " + str(v_head + 1))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        v_head, QtWidgets.QTableWidgetItem(item))

                    page = QtWidgets.QTableWidgetItem("Pages")
                    page.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        frame, QtWidgets.QTableWidgetItem(page))

                if len(stack) < frame:
                    if pages[i] in stack:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("H"))
                        hit_stack.append(i)

                    else:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))
                        stack.append(pages[i])
                        fault = fault + 1

                else:
                    if pages[i] in stack:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("H"))
                        hit_stack.append(i)

                    else:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))
                        stack[count] = pages[i]

                        count = count + 1
                        fault = fault + 1

                        if count == frame:
                            count = 0

                for row in range(len(stack)):
                    item = QtWidgets.QTableWidgetItem(str(stack[row]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(tablerow, i, item)
                    tablerow += 1

                for row in range(frame):
                    for column in range(len(hit_stack)):
                        self.table.item(row, hit_stack[column]).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.table.item(row, hit_stack[column]).setForeground(
                            QtGui.QColor(255, 255, 255))

            fault_count = self.pageFault_FIFO(frame, pages)
            hit_count = len(pages) - fault_count
            fault_rate = "{:.2f}".format((fault_count / len(pages)))
            hit_rate = "{:.2f}".format((hit_count / len(pages)))

            self.t_hit.setText("Total Hit: \t" + str(hit_count))
            self.t_fault.setText("Total Fault: \t" + str(fault_count))
            self.hit_rate.setText("Hit Rate: \t\t" + str(hit_rate))
            self.fault_rate.setText("Fault Rate: \t" + str(fault_rate))

        if val == 1:
            stack = []
            hit_stack = []
            count = 0
            fault = 0
            tablerow = 0
            y = len(pages)
            stack = []
            self.table.setRowCount(frame + 1)
            self.table.setColumnCount(len(pages))
            for i in range(len(pages)):
                tablerow = 0
                self.table.setColumnWidth(i, 80)
                self.table.setRowHeight(i, 42)
                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(frame, i, item)
                self.table.item(frame, i).setBackground(
                    QtGui.QColor(0, 125, 125))
                self.table.item(frame, i).setForeground(
                    QtGui.QColor(255, 255, 255))
                for v_head in range(frame):
                    item = QtWidgets.QTableWidgetItem(
                        "Frame " + str(v_head + 1))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        v_head, QtWidgets.QTableWidgetItem(item))

                    page = QtWidgets.QTableWidgetItem("Pages")
                    page.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        frame, QtWidgets.QTableWidgetItem(page))
                if i < y and len(stack) < frame:
                    if pages[i] not in stack:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))
                        stack.append(pages[i])
                        fault = fault + 1
                    else:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("H"))
                        hit_stack.append(i)
                else:
                    if pages[i] in stack:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("H"))
                        hit_stack.append(i)

                    else:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))
                        stack.pop()
                        stack.append(pages[i])
                        fault += 1
                for row in range(len(stack)):
                    item = QtWidgets.QTableWidgetItem(str(stack[row]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(tablerow, i, item)
                    tablerow += 1
                for row in range(frame):
                    for column in range(len(hit_stack)):
                        self.table.item(row, hit_stack[column]).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.table.item(row, hit_stack[column]).setForeground(
                            QtGui.QColor(255, 255, 255))

            fault_count = self.pageFault_LIFO(frame, pages)
            hit_count = len(pages) - fault_count
            fault_rate = "{:.2f}".format((fault_count / len(pages) * 100))
            hit_rate = "{:.2f}".format((hit_count / len(pages) * 100))

            self.t_hit.setText("Total Hit: \t" + str(hit_count))
            self.t_fault.setText("Total Fault: \t" + str(fault_count))
            self.hit_rate.setText("Hit Rate: \t\t" + str(hit_rate))
            self.fault_rate.setText("Fault Rate: \t" + str(fault_rate))

        if val == 2:
            fault = 0
            hit_stack = []
            stack = []
            st = []
            self.table.setRowCount(frame + 1)
            self.table.setColumnCount(len(pages))

            for i in range(len(pages)):
                tablerow = 0
                self.table.setColumnWidth(i, 80)
                self.table.setRowHeight(i, 42)
                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(frame, i, item)

                self.table.item(frame, i).setBackground(
                    QtGui.QColor(0, 125, 125))
                self.table.item(frame, i).setForeground(
                    QtGui.QColor(255, 255, 255))

                for v_head in range(frame):
                    item = QtWidgets.QTableWidgetItem(
                        "Frame " + str(v_head + 1))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        v_head, QtWidgets.QTableWidgetItem(item))

                    page = QtWidgets.QTableWidgetItem("Pages")
                    page.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        frame, QtWidgets.QTableWidgetItem(page))

                if pages[i] not in stack:
                    if len(stack) < frame:
                        stack.append(pages[i])
                        st.append(len(stack) - 1)
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))

                    else:
                        ind = st.pop(0)
                        stack[ind] = pages[i]
                        st.append(ind)
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))

                    fault += 1

                else:
                    st.append(st.pop(st.index(stack.index(pages[i]))))
                    self.table.setHorizontalHeaderItem(
                        i, QtWidgets.QTableWidgetItem("H"))
                    hit_stack.append(i)

                for row in range(len(stack)):
                    item = QtWidgets.QTableWidgetItem(str(stack[row]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(tablerow, i, item)
                    tablerow += 1

                for row in range(frame):
                    for column in range(len(hit_stack)):
                        self.table.item(row, hit_stack[column]).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.table.item(row, hit_stack[column]).setForeground(
                            QtGui.QColor(255, 255, 255))

            fault_count = self.pageFault_LRU(frame, pages)
            hit_count = len(pages) - fault_count
            fault_rate = "{:.2f}".format((fault_count / len(pages)))
            hit_rate = "{:.2f}".format((hit_count / len(pages)))

            self.t_hit.setText("Total Hit: \t" + str(hit_count))
            self.t_fault.setText("Total Fault: \t" + str(fault_count))
            self.hit_rate.setText("Hit Rate: \t\t" + str(hit_rate))
            self.fault_rate.setText("Fault Rate: \t" + str(fault_rate))

        if val == 3:
            fault = 0
            hit_stack = []
            stack = []
            occurance = [None for i in range(frame)]
            self.table.setRowCount(frame + 1)
            self.table.setColumnCount(len(pages))

            for i in range(len(pages)):
                tablerow = 0
                self.table.setColumnWidth(i, 80)
                self.table.setRowHeight(i, 42)
                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(frame, i, item)

                self.table.item(frame, i).setBackground(
                    QtGui.QColor(0, 125, 125))
                self.table.item(frame, i).setForeground(
                    QtGui.QColor(255, 255, 255))

                for v_head in range(frame):
                    item = QtWidgets.QTableWidgetItem(
                        "Frame " + str(v_head + 1))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        v_head, QtWidgets.QTableWidgetItem(item))

                    page = QtWidgets.QTableWidgetItem("Pages")
                    page.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        frame, QtWidgets.QTableWidgetItem(page))

                if pages[i] not in stack:
                    if len(stack) < frame:
                        stack.append(pages[i])
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))

                    else:
                        for x in range(len(stack)):
                            if stack[x] not in pages[i + 1:]:
                                stack[x] = pages[i]
                                break
                            else:
                                occurance[x] = pages[i + 1:].index(stack[x])
                        else:
                            stack[occurance.index(max(occurance))] = pages[i]
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))

                    fault += 1

                else:
                    hit_stack.append(i)
                    self.table.setHorizontalHeaderItem(
                        i, QtWidgets.QTableWidgetItem("H"))

                for row in range(len(stack)):
                    item = QtWidgets.QTableWidgetItem(str(stack[row]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(tablerow, i, item)
                    tablerow += 1

                for row in range(frame):
                    for column in range(len(hit_stack)):
                        self.table.item(row, hit_stack[column]).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.table.item(row, hit_stack[column]).setForeground(
                            QtGui.QColor(255, 255, 255))

            fault_count = self.pageFault_OPR(frame, pages)
            hit_count = len(pages) - fault_count
            fault_rate = "{:.2f}".format((fault_count / len(pages)))
            hit_rate = "{:.2f}".format((hit_count / len(pages)))

            self.t_hit.setText("Total Hit: \t" + str(hit_count))
            self.t_fault.setText("Total Fault: \t" + str(fault_count))
            self.hit_rate.setText("Hit Rate: \t\t" + str(hit_rate))
            self.fault_rate.setText("Fault Rate: \t" + str(fault_rate))

        if val == 4:
            self.ran = random.randint(0, frame - 1)
            stack = []
            hit_stack = []
            fault = 0
            self.table.setRowCount(frame + 1)
            self.table.setColumnCount(len(pages))

            for i in range(len(pages)):
                tablerow = 0
                self.table.setColumnWidth(i, 80)
                self.table.setRowHeight(i, 42)
                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(frame, i, item)

                self.table.item(frame, i).setBackground(
                    QtGui.QColor(0, 125, 125))
                self.table.item(frame, i).setForeground(
                    QtGui.QColor(255, 255, 255))

                for v_head in range(frame):
                    item = QtWidgets.QTableWidgetItem(
                        "Frame " + str(v_head + 1))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        v_head, QtWidgets.QTableWidgetItem(item))

                    page = QtWidgets.QTableWidgetItem("Pages")
                    page.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        frame, QtWidgets.QTableWidgetItem(page))

                if len(stack) < frame:
                    if pages[i] in stack:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("H"))
                        hit_stack.append(i)

                    else:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))
                        stack.append(pages[i])
                        fault = fault + 1

                else:
                    if pages[i] in stack:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("H"))
                        hit_stack.append(i)

                    else:
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("F"))
                        stack[self.ran] = pages[i]

                        fault = fault + 1

                for row in range(len(stack)):
                    item = QtWidgets.QTableWidgetItem(str(stack[row]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(tablerow, i, item)
                    tablerow += 1

                for row in range(frame):
                    for column in range(len(hit_stack)):
                        self.table.item(row, hit_stack[column]).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.table.item(row, hit_stack[column]).setForeground(
                            QtGui.QColor(255, 255, 255))

            fault_count = fault
            hit_count = len(pages) - fault_count
            fault_rate = "{:.2f}".format((fault_count / len(pages)))
            hit_rate = "{:.2f}".format((hit_count / len(pages)))

            self.t_hit.setText("Total Hit: \t" + str(hit_count))
            self.t_fault.setText("Total Fault: \t" + str(fault_count))
            self.hit_rate.setText("Hit Rate: \t\t" + str(hit_rate))
            self.fault_rate.setText("Fault Rate: \t" + str(fault_rate))

        if val == 5:
            stack = [-1] * frame
            hit_stack = []
            second_chance = [False] * frame
            pointer = 0
            index = 0
            no_stack = []

            self.table.setRowCount(frame + 1)
            self.table.setColumnCount(len(pages))

            for i in range(len(pages)):
                tablerow = 0
                self.table.setColumnWidth(i, 80)
                self.table.setRowHeight(i, 42)
                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.table.setItem(frame, i, item)

                self.table.item(frame, i).setBackground(
                    QtGui.QColor(0, 125, 125))
                self.table.item(frame, i).setForeground(
                    QtGui.QColor(255, 255, 255))
                for v_head in range(frame):
                    item = QtWidgets.QTableWidgetItem(
                        "Frame " + str(v_head + 1))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        v_head, QtWidgets.QTableWidgetItem(item))

                    page = QtWidgets.QTableWidgetItem("Pages")
                    page.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setVerticalHeaderItem(
                        frame, QtWidgets.QTableWidgetItem(page))

                if pages[i] in stack:
                    for k in range(frame):
                        if stack[k] == pages[i]:
                            index = k
                            break

                    if not second_chance[index]:
                        second_chance[index] = True
                        chance_count += 1
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("S"))
                        hit_stack.append(i)
                    else:
                        no_stack.append(i)
                        no_chance += 1
                        self.table.setHorizontalHeaderItem(
                            i, QtWidgets.QTableWidgetItem("N"))

                else:
                    self.table.setHorizontalHeaderItem(
                        i, QtWidgets.QTableWidgetItem("F"))
                    while True:
                        if not second_chance[pointer]:
                            count = count + 1
                            stack[pointer] = pages[i]
                            pointer = (pointer + 1) % frame
                            break

                        second_chance[pointer] = False
                        pointer = (pointer + 1) % frame
                        count = count + 1

                for row in range(len(stack)):
                    item = QtWidgets.QTableWidgetItem(str(stack[row]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(tablerow, i, item)
                    tablerow += 1

                for row in range(frame):
                    for column in range(len(hit_stack)):
                        self.table.item(row, hit_stack[column]).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.table.item(row, hit_stack[column]).setForeground(
                            QtGui.QColor(255, 255, 255))

                for row in range(frame):
                    for column in range(len(no_stack)):
                        self.table.item(row, no_stack[column]).setBackground(
                            QtGui.QColor(0, 0, 0))
                        self.table.item(row, no_stack[column]).setForeground(
                            QtGui.QColor(255, 255, 255))

            hit_count = chance_count + no_chance
            fault_count = len(pages) - hit_count
            fault_rate = "{:.2f}".format((fault_count / len(pages)))
            hit_rate = "{:.2f}".format((hit_count / len(pages)))

            self.t_hit.setText("Total Hit: \t" + str(hit_count))
            self.t_fault.setText("Total Fault: \t" + str(fault_count))
            self.hit_rate.setText("Hit Rate: \t\t" + str(hit_rate))
            self.fault_rate.setText("Fault Rate: \t" + str(fault_rate))

    def graph(self):
        pages = self.lineEdit.text()
        pages = pages.split()

        f_lst = []
        h_lst = []

        val = self.comboBox.currentIndex()
        if val == 0:
            for x in range(10):
                fal = self.pageFault_FIFO(x + 1, pages)
                hit = len(pages) - fal
                f_lst.append(fal)
                h_lst.append(hit)

            array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            plt.figure("FIFO Graph", figsize=(12.8, 6.9), dpi=100)
            plt.title("Graph of Number of Frames v/s Hit/Fault", fontsize=20)
            plt.xlabel("Number of Frames -->")
            plt.ylabel("Total Hit and Total Fault")
            plt.plot(array, f_lst, 'r.-', label="Fault Rate")
            plt.plot(array, h_lst, 'b.-', label="Hit Rate")
            plt.legend()
            plt.show()

        if val == 1:
            for x in range(10):
                fal = self.pageFault_LIFO(x + 1, pages)
                hit = len(pages) - fal
                f_lst.append(fal)
                h_lst.append(hit)

            array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            plt.figure("LIFO Graph", figsize=(12.8, 6.9), dpi=100)
            plt.title("Graph of Number of Frames v/s Hit/Fault", fontsize=20)
            plt.xlabel("Number of Frames -->")
            plt.ylabel("Total Hit and Total Fault")
            plt.plot(array, f_lst, 'r.-', label="Fault Rate")
            plt.plot(array, h_lst, 'b.-', label="Hit Rate")
            plt.legend()
            plt.show()

        if val == 2:
            for x in range(10):
                fal = self.pageFault_LRU(x + 1, pages)
                hit = len(pages) - fal
                f_lst.append(fal)
                h_lst.append(hit)

            array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            plt.figure("LRU Graph", figsize=(12.8, 6.9), dpi=100)
            plt.title("Graph of Number of Frames v/s Hit/Fault", fontsize=20)
            plt.xlabel("Number of Frames -->")
            plt.ylabel("Total Hit and Total Fault")
            plt.plot(array, f_lst, 'r.-', label="Fault Rate")
            plt.plot(array, h_lst, 'b.-', label="Hit Rate")
            plt.legend()
            plt.show()

        if val == 3:
            for x in range(10):
                fal = self.pageFault_OPR(x + 1, pages)
                hit = len(pages) - fal
                f_lst.append(fal)
                h_lst.append(hit)

            array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            plt.figure("OPR Graph", figsize=(12.8, 6.9), dpi=100)
            plt.title("Graph of Number of Frames v/s Hit/Fault", fontsize=20)
            plt.xlabel("Number of Frames -->")
            plt.ylabel("Total Hit and Total Fault")
            plt.plot(array, f_lst, 'r.-', label="Fault Rate")
            plt.plot(array, h_lst, 'b.-', label="Hit Rate")
            plt.legend()
            plt.show()

        if val == 4:
            for x in range(10):
                fal = self.pageFault_RPR(x + 1, pages)
                hit = len(pages) - fal
                f_lst.append(fal)
                h_lst.append(hit)

            array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            plt.figure("RPR Graph", figsize=(12.8, 6.9), dpi=100)
            plt.title("Graph of Number of Frames v/s Hit/Fault", fontsize=20)
            plt.xlabel("Number of Frames -->")
            plt.ylabel("Total Hit and Total Fault")
            plt.plot(array, f_lst, 'r.-', label="Fault Rate")
            plt.plot(array, h_lst, 'b.-', label="Hit Rate")
            plt.legend()
            plt.show()

        if val == 5:
            for x in range(10):
                fal = self.secondChance().PageFault_SC(x + 1, pages)
                hit = len(pages) - fal
                f_lst.append(fal)
                h_lst.append(hit)

            array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            plt.figure("SC Graph", figsize=(12.8, 6.9), dpi=100)
            plt.title("Graph of Number of Frames v/s Hit/Fault", fontsize=20)
            plt.xlabel("Number of Frames -->")
            plt.ylabel("Total Hit and Total Fault")
            plt.plot(array, f_lst, 'r.-', label="Fault Rate")
            plt.plot(array, h_lst, 'b.-', label="Hit Rate")
            plt.legend()
            plt.show()

    def explanation(self):
        frame = self.spinBox.text()
        frame = int(frame)

        pages = self.lineEdit.text()
        pages = pages.split()

        stack = []
        hit_stack = []
        count = 0
        fault = 0

        val = self.comboBox.currentIndex()

        if val == 0:
            tablerow = 0
            self.explain_table.setRowCount(len(pages))
            self.explain_table.setColumnCount(2)
            self.explain_table.setColumnWidth(0, 110)
            self.explain_table.setColumnWidth(1, 550)
            for i in range(len(pages)):

                self.explain_table.setRowHeight(i, 45)

                self.explain_table.setHorizontalHeaderItem(
                    0, QtWidgets.QTableWidgetItem("Status"))
                self.explain_table.setHorizontalHeaderItem(
                    1, QtWidgets.QTableWidgetItem("Explanation"))

                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.explain_table.setVerticalHeaderItem(
                    i, QtWidgets.QTableWidgetItem(item))

                if len(stack) < frame:
                    if pages[i] in stack:
                        hit_stack.append(i)

                        status = QtWidgets.QTableWidgetItem("Page Hit")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem("As " + pages[
                            i] + " found in the stack, Page Hit occured.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                    else:
                        stack.append(pages[i])
                        fault = fault + 1

                        status = QtWidgets.QTableWidgetItem("Page Fault")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem(
                            "As Stack has empty place, " + pages[
                                i] + " inserted there.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                else:
                    if pages[i] in stack:
                        hit_stack.append(i)

                        status = QtWidgets.QTableWidgetItem("Page Hit")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem("As " + pages[
                            i] + " found in the stack, Page Hit occured.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                    else:
                        status = QtWidgets.QTableWidgetItem("Page Fault")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem(
                            " As " + pages[i] + " not found in the stack, " + pages[i] + " replaced " + stack[
                                count] + ".")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                        stack[count] = pages[i]

                        count = count + 1
                        fault = fault + 1

                        if count == frame:
                            count = 0

                for row in range(len(hit_stack)):
                    for col in range(2):
                        self.explain_table.item(hit_stack[row], col).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.explain_table.item(hit_stack[row], col).setForeground(
                            QtGui.QColor(255, 255, 255))

        if val == 1:
            tablerow = 0
            x = frame
            i = 0
            y = len(pages)
            self.explain_table.setRowCount(len(pages))
            self.explain_table.setColumnCount(2)
            self.explain_table.setColumnWidth(0, 110)
            self.explain_table.setColumnWidth(1, 550)
            for k in range(y):
                self.explain_table.setRowHeight(k, 45)
                self.explain_table.setHorizontalHeaderItem(
                    0, QtWidgets.QTableWidgetItem("Status"))
                self.explain_table.setHorizontalHeaderItem(
                    1, QtWidgets.QTableWidgetItem("Explanation"))
                item = QtWidgets.QTableWidgetItem(str(pages[k]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.explain_table.setVerticalHeaderItem(
                    k, QtWidgets.QTableWidgetItem(item))
            while (i < y):
                while (i < y and len(stack) < x):
                    if (pages[i] not in stack):
                        stack.append(pages[i])
                        fault += 1
                        status = QtWidgets.QTableWidgetItem("Page Fault")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)
                        item = QtWidgets.QTableWidgetItem(
                            "As Stack has empty place, " + pages[
                                i] + " inserted there.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)
                        tablerow += 1

                    else:
                        hit_stack.append(i)
                        status = QtWidgets.QTableWidgetItem("Page Hit")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem("As " + pages[
                            i] + " found in the stack, Page Hit occured.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)
                        tablerow += 1
                    i += 1

                if (pages[i] not in stack):
                    status = QtWidgets.QTableWidgetItem("Page Fault")
                    status.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.explain_table.setItem(tablerow, 0, status)
                    item = QtWidgets.QTableWidgetItem(
                        " As " + pages[i] + " not found in the stack, " + pages[i] + " replaced " + stack[
                            frame - 1] + ".")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.explain_table.setItem(tablerow, 1, item)
                    tablerow += 1
                    stack.pop()
                    stack.append(pages[i])
                    fault += 1

                else:
                    hit_stack.append(i)
                    status = QtWidgets.QTableWidgetItem("Page Hit")
                    status.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.explain_table.setItem(tablerow, 0, status)
                    item = QtWidgets.QTableWidgetItem("As " + pages[
                        i] + " found in the stack, Page Hit occured.")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.explain_table.setItem(tablerow, 1, item)
                    tablerow += 1
                i += 1
            for row in range(len(hit_stack)):
                for col in range(2):
                    self.explain_table.item(hit_stack[row], col).setBackground(
                        QtGui.QColor(255, 0, 0))
                    self.explain_table.item(hit_stack[row], col).setForeground(
                        QtGui.QColor(255, 255, 255))

        if val == 2:
            st = []
            tablerow = 0
            self.explain_table.setRowCount(len(pages))
            self.explain_table.setColumnCount(2)
            self.explain_table.setColumnWidth(0, 110)
            self.explain_table.setColumnWidth(1, 550)
            for i in range(len(pages)):

                self.explain_table.setRowHeight(i, 45)

                self.explain_table.setHorizontalHeaderItem(
                    0, QtWidgets.QTableWidgetItem("Status"))
                self.explain_table.setHorizontalHeaderItem(
                    1, QtWidgets.QTableWidgetItem("Explanation"))

                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.explain_table.setVerticalHeaderItem(
                    i, QtWidgets.QTableWidgetItem(item))

                if pages[i] not in stack:
                    if len(stack) < frame:
                        stack.append(pages[i])
                        st.append(len(stack) - 1)
                        status = QtWidgets.QTableWidgetItem("Page Fault")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem(
                            "As Stack has empty place, " + pages[
                                i] + " inserted there.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                    else:
                        ind = st.pop(0)
                        stack[ind] = pages[i]
                        st.append(ind)
                        status = QtWidgets.QTableWidgetItem("Page Fault")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem(
                            " As " + pages[i] + " not found in the stack, " + pages[
                                i] + " replaced least recently used.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                    fault += 1

                else:
                    st.append(st.pop(st.index(stack.index(pages[i]))))
                    hit_stack.append(i)
                    status = QtWidgets.QTableWidgetItem("Page Hit")
                    status.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.explain_table.setItem(tablerow, 0, status)

                    item = QtWidgets.QTableWidgetItem("As " + pages[
                        i] + " found in the stack, Page Hit occured.")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.explain_table.setItem(tablerow, 1, item)

                    tablerow += 1

                for row in range(len(hit_stack)):
                    for col in range(2):
                        self.explain_table.item(hit_stack[row], col).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.explain_table.item(hit_stack[row], col).setForeground(
                            QtGui.QColor(255, 255, 255))

        if val == 3:
            tablerow = 0
            occurance = [None for i in range(frame)]
            self.explain_table.setRowCount(len(pages))
            self.explain_table.setColumnCount(2)
            self.explain_table.setColumnWidth(0, 110)
            self.explain_table.setColumnWidth(1, 550)
            for i in range(len(pages)):

                self.explain_table.setRowHeight(i, 45)

                self.explain_table.setHorizontalHeaderItem(
                    0, QtWidgets.QTableWidgetItem("Status"))
                self.explain_table.setHorizontalHeaderItem(
                    1, QtWidgets.QTableWidgetItem("Explanation"))

                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.explain_table.setVerticalHeaderItem(
                    i, QtWidgets.QTableWidgetItem(item))

                if pages[i] not in stack:
                    if len(stack) < frame:
                        stack.append(pages[i])
                        status = QtWidgets.QTableWidgetItem("Page Fault")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem(
                            "As Stack has empty place, " + pages[
                                i] + " inserted there.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                    else:
                        for x in range(len(stack)):
                            if stack[x] not in pages[i + 1:]:
                                stack[x] = pages[i]
                                break
                            else:
                                occurance[x] = pages[i + 1:].index(stack[x])
                        else:
                            stack[occurance.index(max(occurance))] = pages[i]

                        status = QtWidgets.QTableWidgetItem("Page Fault")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem(
                            " As " + pages[i] + " not found in the stack, " + pages[
                                i] + " replaced the existing one optimally.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                    fault += 1

                else:
                    hit_stack.append(i)

                    status = QtWidgets.QTableWidgetItem("Page Hit")
                    status.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.explain_table.setItem(tablerow, 0, status)

                    item = QtWidgets.QTableWidgetItem("As " + pages[
                        i] + " found in the stack, Page Hit occured.")
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.explain_table.setItem(tablerow, 1, item)

                    tablerow += 1

                for row in range(len(hit_stack)):
                    for col in range(2):
                        self.explain_table.item(hit_stack[row], col).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.explain_table.item(hit_stack[row], col).setForeground(
                            QtGui.QColor(255, 255, 255))

        if val == 4:
            tablerow = 0
            self.explain_table.setRowCount(len(pages))
            self.explain_table.setColumnCount(2)
            self.explain_table.setColumnWidth(0, 110)
            self.explain_table.setColumnWidth(1, 550)

            for i in range(len(pages)):

                self.explain_table.setRowHeight(i, 45)

                self.explain_table.setHorizontalHeaderItem(
                    0, QtWidgets.QTableWidgetItem("Status"))
                self.explain_table.setHorizontalHeaderItem(
                    1, QtWidgets.QTableWidgetItem("Explanation"))

                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.explain_table.setVerticalHeaderItem(
                    i, QtWidgets.QTableWidgetItem(item))

                if len(stack) < frame:
                    if pages[i] in stack:
                        hit_stack.append(i)

                        status = QtWidgets.QTableWidgetItem("Page Hit")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem("As " + pages[
                            i] + " found in the stack, Page Hit occured.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                    else:
                        stack.append(pages[i])
                        fault = fault + 1

                        status = QtWidgets.QTableWidgetItem("Page Fault")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem(
                            "As Stack has empty place, " + pages[
                                i] + " inserted there.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                else:
                    if pages[i] in stack:
                        hit_stack.append(i)

                        status = QtWidgets.QTableWidgetItem("Page Hit")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem("As " + pages[
                            i] + " found in the stack, Page Hit occured.")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                    else:
                        status = QtWidgets.QTableWidgetItem("Page Fault")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem(
                            " As " + pages[i] + " not found in the stack, " + pages[i] + " replaced " + stack[self.ran] + ".")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                        tablerow += 1

                        stack[self.ran] = pages[i]

                        fault = fault + 1

                for row in range(len(hit_stack)):
                    for col in range(2):
                        self.explain_table.item(hit_stack[row], col).setBackground(
                            QtGui.QColor(255, 0, 0))
                        self.explain_table.item(hit_stack[row], col).setForeground(
                            QtGui.QColor(255, 255, 255))

        if val == 5:
            stack = [-1] * frame
            hit_stack = []
            second_chance = [False] * frame
            pointer = 0
            no_stack = []
            tablerow = 0

            self.explain_table.setRowCount(len(pages))
            self.explain_table.setColumnCount(2)
            self.explain_table.setColumnWidth(0, 110)
            self.explain_table.setColumnWidth(1, 550)

            for i in range(len(pages)):
                self.explain_table.setRowHeight(i, 45)
                self.explain_table.setHorizontalHeaderItem(
                    0, QtWidgets.QTableWidgetItem("Status"))
                self.explain_table.setHorizontalHeaderItem(
                    1, QtWidgets.QTableWidgetItem("Explanation"))

                item = QtWidgets.QTableWidgetItem(str(pages[i]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)

                self.explain_table.setVerticalHeaderItem(
                    i, QtWidgets.QTableWidgetItem(item))

                if pages[i] in stack:
                    index = 0
                    for k in range(frame):
                        if stack[k] == pages[i]:
                            index = k
                            break

                    if not second_chance[index]:
                        second_chance[index] = True
                        hit_stack.append(i)

                        status = QtWidgets.QTableWidgetItem("SecondChance")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem("'" + pages[i] + "' got Hit in the Frame: " + str(index + 1)
                                                          + ". So, its bit becomes '" + str(
                            second_chance[index]) + "'. So, it will get second chance. ["
                            + "Second_Chance = " + str(second_chance) + "]]")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)
                    else:
                        no_stack.append(i)
                        status = QtWidgets.QTableWidgetItem("NoEffect")
                        status.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 0, status)

                        item = QtWidgets.QTableWidgetItem(
                            "'" +
                            pages[i] + "' again got Hit in the Frame: " +
                            str(index + 1)
                            + ". So, this time it will remain unchanged. This means, its second chance bit will remain same."
                              " i.e, '" + str(second_chance[index]) +
                            "'. [Second_Chance = " + str(second_chance) + "]]")
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.explain_table.setItem(tablerow, 1, item)

                    tablerow += 1

                else:
                    while True:
                        if not second_chance[pointer]:
                            stack[pointer] = pages[i]
                            status = QtWidgets.QTableWidgetItem("Page Fault")
                            status.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.explain_table.setItem(tablerow, 0, status)

                            item = QtWidgets.QTableWidgetItem(
                                "'" + pages[i] + "'" + " got inserted in the Frame = " + str(
                                    pointer + 1) + ". [Second_Chance = "
                                + str(second_chance) + "]")
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.explain_table.setItem(tablerow, 1, item)

                            pointer = (pointer + 1) % frame
                            break

                        second_chance[pointer] = False
                        pointer = (pointer + 1) % frame

                    tablerow += 1

            for row in range(len(hit_stack)):
                for col in range(2):
                    self.explain_table.item(hit_stack[row], col).setBackground(
                        QtGui.QColor(255, 0, 0))
                    self.explain_table.item(hit_stack[row], col).setForeground(
                        QtGui.QColor(255, 255, 255))
            for row in range(len(no_stack)):
                for col in range(2):
                    self.explain_table.item(no_stack[row], col).setBackground(
                        QtGui.QColor(0, 0, 0))
                    self.explain_table.item(no_stack[row], col).setForeground(
                        QtGui.QColor(255, 255, 155))

    def compare(self):
        pages = self.lineEdit.text()
        pages = pages.split()

        fifo_f_lst = []
        fifo_h_lst = []

        lifo_f_lst = []
        lifo_h_lst = []

        lru_f_lst = []
        lru_h_lst = []

        opr_f_lst = []
        opr_h_lst = []

        rp_f_lst = []
        rp_h_lst = []

        sc_f_lst = []
        sc_h_lst = []

        for x in range(10):
            fifo_fal = self.pageFault_FIFO(x + 1, pages)
            fifo_hit = len(pages) - fifo_fal
            fifo_f_lst.append(fifo_fal)
            fifo_h_lst.append(fifo_hit)

        for x in range(10):
            lifo_fault = self.pageFault_LIFO(x + 1, pages)
            lifo_hit = len(pages) - lifo_fault
            lifo_f_lst.append(lifo_fault)
            lifo_h_lst.append(lifo_hit)

        for x in range(10):
            lru_fault = self.pageFault_LRU(x + 1, pages)
            lru_hit = len(pages) - lru_fault
            lru_f_lst.append(lru_fault)
            lru_h_lst.append(lru_hit)

        for x in range(10):
            opr_fault = self.pageFault_OPR(x + 1, pages)
            opr_hit = len(pages) - opr_fault
            opr_f_lst.append(opr_fault)
            opr_h_lst.append(opr_hit)

        for x in range(10):
            rp_fault = self.pageFault_RPR(x + 1, pages)
            rp_hit = len(pages) - rp_fault
            rp_f_lst.append(rp_fault)
            rp_h_lst.append(rp_hit)

        for x in range(10):
            sc_fal = self.secondChance().PageFault_SC(x + 1, pages)
            sc_hit = len(pages) - sc_fal
            sc_f_lst.append(sc_fal)
            sc_h_lst.append(sc_hit)

        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        fig = plt.figure("Comparison in Page Replacement Algorithm",
                         figsize=(12.8, 6.9), dpi=100)
        gs = fig.add_gridspec(2, hspace=0.2)
        axs = gs.subplots(sharex=True, sharey=True)
        fig.suptitle('Comparison of All Algorithms', fontsize=26)

        fig.text(0.5, 0.04, 'Number of Frames -->',
                 ha='center', va='center', fontsize=16)
        fig.text(0.06, 0.5, 'Total Page Hit and Total Page Fault', ha='center', va='center', rotation='vertical',
                 fontsize=16)

        line_labels = ["FIFO", "LRU", "OPR", "LIFO", "RPR", "SCR"]

        axs[0].set_title("Fault Rate", fontsize=18)
        l1 = axs[0].plot(array, fifo_f_lst, 'tab:orange')
        l2 = axs[0].plot(array, lru_f_lst, 'tab:green')
        l3 = axs[0].plot(array, opr_f_lst, 'tab:red')
        l4 = axs[0].plot(array, lifo_f_lst, 'tab:pink')
        l5 = axs[0].plot(array, rp_f_lst, 'tab:blue')
        l6 = axs[0].plot(array, rp_f_lst, 'tab:orange')

        axs[1].set_title("Hit Rate", fontsize=18)
        axs[1].plot(array, fifo_h_lst, 'tab:orange')
        axs[1].plot(array, lru_h_lst, 'tab:green')
        axs[1].plot(array, opr_h_lst, 'tab:red')
        axs[1].plot(array, lifo_h_lst, 'tab:pink')
        axs[1].plot(array, rp_h_lst, 'tab:blue')
        axs[1].plot(array, sc_h_lst, 'tab:orange')

        lines = [l1, l2, l3, l4, l5, l6]
        fig.legend(lines, labels=line_labels,
                   loc="upper right",
                   borderaxespad=0.5,
                   title="Legend Title"
                   )

        plt.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PageReplacement = QtWidgets.QMainWindow()
    ui = UI_PageReplacement()

    ui.setupUi(PageReplacement)
    PageReplacement.show()
    sys.exit(app.exec_())
