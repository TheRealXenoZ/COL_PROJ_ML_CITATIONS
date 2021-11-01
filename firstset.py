# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstset.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 309)
        MainWindow.setStyleSheet("color: rgb(255, 0, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 240, 251, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(490, 40, 31, 33))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(490, 80, 31, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(490, 120, 31, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(490, 160, 31, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 471, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 451, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 411, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 391, 21))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 401, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 200, 31, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(330, 0, 161, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 131, 21))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "First set of Features"))
        self.pushButton.setText(_translate("MainWindow", "Store Fisrt set in Data base"))
        self.lineEdit_3.setText(_translate("MainWindow", "1"))
        self.lineEdit_4.setText(_translate("MainWindow", "1"))
        self.lineEdit_5.setText(_translate("MainWindow", "1"))
        self.lineEdit_6.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "\'Body fluid compartments\' occurences(0 if No occurence, 1 if for any number of  occurences)"))
        self.label_4.setText(_translate("MainWindow", "\'Sarcomere\'occurences(0 for no occurence, 1 for any number of occurences)"))
        self.label_5.setText(_translate("MainWindow", "\'Cardiac output\'occurences(0 for no occurence, 1 for any number of occurences)"))
        self.label_6.setText(_translate("MainWindow", "\'Cardiac cycle\'occurences(0 for no occurence, 1 for any number of occurences)"))
        self.label_2.setText(_translate("MainWindow", "\'Lung volumes\'occurences(0 for no occurence, 1 for any number of occurences)"))
        self.lineEdit_2.setText(_translate("MainWindow", "1"))
        self.lineEdit_9.setText(_translate("MainWindow", "000001"))
        self.label_7.setText(_translate("MainWindow", "Research paper  ID:"))


