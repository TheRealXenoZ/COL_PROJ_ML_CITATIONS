# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondset.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 316)
        MainWindow.setStyleSheet("color: rgb(255, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 260, 251, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 50, 41, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 421, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(470, 90, 41, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(470, 130, 41, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 170, 41, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 210, 41, 33))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 441, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 381, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 371, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 210, 431, 21))
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(330, 10, 161, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Second set of Features"))
        self.pushButton.setText(_translate("MainWindow", "Store Second Set in Data base"))
        self.lineEdit_4.setText(_translate("MainWindow", "1"))
        self.label_4.setText(_translate("MainWindow", "\'Effects of lesions\'occurences(0 for no occurence, 1 for any number of occurences)"))
        self.lineEdit_5.setText(_translate("MainWindow", "1"))
        self.lineEdit_6.setText(_translate("MainWindow", "1"))
        self.lineEdit_7.setText(_translate("MainWindow", "1"))
        self.lineEdit_8.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "\'V/Q ratioOxygen\'occurences(0 for no occurence, 1 for any number of occurences)"))
        self.label_7.setText(_translate("MainWindow", "\'GFR\'occurences(0 for no occurence, 1 for any number of occurences)"))
        self.label_8.setText(_translate("MainWindow", "\'Micturition\'occurences(0 for no occurence, 1 for any number of occurences)"))
        self.label_9.setText(_translate("MainWindow", "\'Testosterone\'occurences(0 for no occurence, 1 for any number of occurences)"))
        self.label_5.setText(_translate("MainWindow", "Research paper ID:"))
        self.lineEdit_9.setText(_translate("MainWindow", "000001"))


