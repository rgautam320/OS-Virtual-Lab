# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\aboutsstf.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSSFT(object):
    def setupUi(self, DialogSSFT):
        DialogSSFT.setObjectName("DialogSSFT")
        DialogSSFT.resize(1218, 717)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogSSFT.sizePolicy().hasHeightForWidth())
        DialogSSFT.setSizePolicy(sizePolicy)
        DialogSSFT.setMinimumSize(QtCore.QSize(1218, 717))
        DialogSSFT.setMaximumSize(QtCore.QSize(1218, 717))
        self.textBrowser = QtWidgets.QTextBrowser(DialogSSFT)
        self.textBrowser.setGeometry(QtCore.QRect(0, -10, 1221, 731))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(DialogSSFT)
        QtCore.QMetaObject.connectSlotsByName(DialogSSFT)

    def retranslateUi(self, DialogSSFT):
        _translate = QtCore.QCoreApplication.translate
        DialogSSFT.setWindowTitle(_translate("DialogSSFT", "Dialog"))
        self.textBrowser.setHtml(_translate("DialogSSFT", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#40424e;\">SSTF (Shortest Seek Time First)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">In SSTF (Shortest Seek Time First), requests having the shortest seek time are executed first. So, the seek time of every request is calculated in advance in the queue and then they are scheduled according to their calculated seek time. As a result, the request near the disk arm will get executed first. SSTF is certainly an improvement over FCFS as it decreases the average response time and increases the throughput of the system. Let us understand this with the help of an example.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:14pt; font-weight:600; color:#40424e;\">Algorithm</span><span style=\" font-size:14pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">   </span><span style=\" font-size:13pt; color:#40424e;\">Let Request array represents an array storing indexes of tracks that have been requested. ‘Head’ is the position of disk head.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">   </span><span style=\" font-size:13pt; color:#40424e;\">Find the positive distance of all tracks in the request array from head.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">   </span><span style=\" font-size:13pt; color:#40424e;\">Find a track from the requested array which has not been accessed/serviced yet and has minimum distance from head.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">   </span><span style=\" font-size:13pt; color:#40424e;\">Increment the total seek count with this distance.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">   </span><span style=\" font-size:13pt; color:#40424e;\">Currently serviced track position now becomes the new head position.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">   </span><span style=\" font-size:13pt; color:#40424e;\">Go to step 2 until all tracks in the request array have not been serviced.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:14pt; font-weight:600; background-color:#ffffff;\">Advantages</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">      </span><span style=\" font-size:13pt; color:#40424e;\">Average Response Time decreases</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">      </span><span style=\" font-size:13pt; color:#40424e;\">Throughput increases</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:14pt; font-weight:600; color:#000000;\">Disadvantages</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">      </span><span style=\" font-size:13pt; color:#40424e;\">Overhead to calculate seek time in advance</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">      </span><span style=\" font-size:13pt; color:#40424e;\">Can cause Starvation for a request if it has higher seek time as compared to incoming requests</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:13pt; color:#40424e;\">●</span><span style=\" font-family:\'Times New Roman\'; font-size:7pt; color:#40424e;\">      </span><span style=\" font-size:13pt; color:#40424e;\">High variance of response time as SSTF favors only some requests</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))