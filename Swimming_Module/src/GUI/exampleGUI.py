# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nicol\Desktop\exampleGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1302, 793)
        font = QtGui.QFont()
        font.setPointSize(28)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 500, 291, 171))
        self.pushButton.setObjectName("pushButton")
        self.Background = QtWidgets.QGraphicsView(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(70, 50, 256, 192))
        self.Background.setObjectName("Background")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 180, 161, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 50, 20, 191))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Speed = QtWidgets.QLCDNumber(self.centralwidget)
        self.Speed.setGeometry(QtCore.QRect(120, 90, 151, 81))
        self.Speed.setObjectName("Speed")
        self.Background.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.line.raise_()
        self.Speed.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1302, 56))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start Swim Test"))
        self.label.setText(_translate("MainWindow", "Speed (m/s)"))
