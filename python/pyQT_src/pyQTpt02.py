import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os


from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/buttons.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("Hello, Qt!")

        self.pushButton_1.clicked.connect(self.button1Clicked)
        self.pushButton_2.clicked.connect(self.button2Clicked)
        
    def button1Clicked(self) :
        self.textEdit.setText("Button_1")
    
    def button2Clicked(self) :
        self.textEdit.setText("Button_2")
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())







