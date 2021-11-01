import sys
import os
from citation import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.ssftr)
     self.ui.pushButton_2.clicked.connect(self.crtcsv)
     self.ui.pushButton_3.clicked.connect(self.sv1)
     self.ui.pushButton_4.clicked.connect(self.dr1)
     self.ui.pushButton_5.clicked.connect(self.fsftr)
     

  def ssftr(self):
    os.system("python secondset1.py")

  def crtcsv(self):
    os.system("python createcsv1.py")

  def sv1(self):
    os.system("start /B start cmd.exe @cmd /k python -W ignore svm1.py")
 

  def dr1(self):
    os.system("start /B start cmd.exe @cmd /k python -W ignore drl1.py")

  def fsftr(self):
    os.system("python firstset1.py")
	


          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
