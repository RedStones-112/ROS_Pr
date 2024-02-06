import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os


from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/count.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("Hello, Qt!")
        self.count = 0
        self.label.setText(str(self.count))
        self.pushButton_1.clicked.connect(self.buttonClicked_1)
        self.pushButton_2.clicked.connect(self.buttonClicked_2)
        self.pushButton_3.clicked.connect(self.buttonClicked_3)
        
        
        self.lineEdit_2.textChanged.connect(self.change)



    def buttonClicked_1(self) :
        self.count += 1
        self.label.setText(str(self.count))

    def buttonClicked_2(self) :
        self.count = 0
        self.label.setText(str(self.count))

    def buttonClicked_3(self) :
        self.label.setText(self.lineEdit.text())

    def change(self):
        self.lineEdit_3.setText(self.lineEdit_2.text())

        
    

    
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())







