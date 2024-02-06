import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os


from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/radiobuttons.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("Hello, Qt!")

        self.radioButton_1.clicked.connect(self.buttonClicked)
        self.radioButton_2.clicked.connect(self.buttonClicked)
        self.radioButton_3.clicked.connect(self.buttonClicked)

        self.checkBox_1.clicked.connect(self.checkbox)
        self.checkBox_2.clicked.connect(self.checkbox)
        self.checkBox_3.clicked.connect(self.checkbox)
        self.checkBox_4.clicked.connect(self.checkbox)
        self.checkBox_5.clicked.connect(self.checkbox)
        self.checkBox_6.clicked.connect(self.checkbox)
        self.checkBox_7.clicked.connect(self.checkbox)
        self.checkBox_8.clicked.connect(self.checkbox)
        
        
    def buttonClicked(self) :
        if self.radioButton_1.isChecked():
            self.textEdit.setText("Button_1")

        elif self.radioButton_2.isChecked():
            self.textEdit.setText("Button_2")

        elif self.radioButton_3.isChecked():
            self.textEdit.setText("Button_3")
        else:
            self.textEdit.setText("???")
    
    def checkbox(self):
        if self.checkBox_1.isChecked():
            self.checkBox_5.setChecked(True)
        else:
            self.checkBox_5.setChecked(False)

        if self.checkBox_2.isChecked():
            self.checkBox_6.setChecked(True)
        else:
            self.checkBox_6.setChecked(False)

        if self.checkBox_3.isChecked():
            self.checkBox_7.setChecked(True)
        else:
            self.checkBox_7.setChecked(False)

        if self.checkBox_4.isChecked():
            self.checkBox_8.setChecked(True)
        else:
            self.checkBox_8.setChecked(False)
    
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())







