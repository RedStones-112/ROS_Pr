import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os


from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/qt05.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("05pt")
        
        self.pushButton_1.clicked.connect(self.buttonClicked_1)
        
        
        self.lineEdit.returnPressed.connect(self.enter)
        


    def buttonClicked_1(self) :
        self.count += 1
        self.label.setText(str(self.count))


    def change(self):
        
        pass
        

        
    def enter(self):
        self.textEdit.setText(self.lineEdit.text())
        self.lineEdit.setText("")
        try:
            pass
        except:
            pass
        

    
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())







