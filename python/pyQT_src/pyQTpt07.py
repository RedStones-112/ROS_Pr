import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic

# import mysql.connector
# import pandas as pd
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "8470",
#     database = "amrbase",
# )
# cur = mydb.cursor()


from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/qt07.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("06pt")

        #self.tableWidget.horizontalHeader().setSectionResizeMode()
    
        self.pushButton.clicked.connect(self.create_Q)


    def create_Q(self):
        pass

    def Add(self, name, gender, brithday):
        row = self.tableWidget.rowCount()

        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, name)
        self.tableWidget.setItem(row, 1, gender)
        self.tableWidget.setItem(row, 2, brithday)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec())







