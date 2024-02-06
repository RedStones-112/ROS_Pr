import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os


from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/calculator.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("PyQTcalculator")
        self.order = ""
        self.middle_calculation = ""
        self.label.setText("")
        self.label2.setText("0")

        self.pushButton_1.clicked.connect(self.clear)
        # self.pushButton_2.clicked.connect()## 괄호 힘들꺼같다
        self.pushButton_3.clicked.connect(self.per)
        self.pushButton_4.clicked.connect(self.div)
        self.pushButton_5.clicked.connect(self.number_click_1)
        self.pushButton_6.clicked.connect(self.number_click_2)
        self.pushButton_7.clicked.connect(self.number_click_3)
        self.pushButton_8.clicked.connect(self.multi)
        self.pushButton_9.clicked.connect(self.number_click_4)
        self.pushButton_10.clicked.connect(self.number_click_5)
        self.pushButton_11.clicked.connect(self.number_click_6)
        self.pushButton_12.clicked.connect(self.minus)
        self.pushButton_13.clicked.connect(self.number_click_7)
        self.pushButton_14.clicked.connect(self.number_click_8)
        self.pushButton_15.clicked.connect(self.number_click_9)
        self.pushButton_16.clicked.connect(self.plus)
        self.pushButton_17.clicked.connect(self.reversal)
        self.pushButton_18.clicked.connect(self.number_click_0)
        self.pushButton_19.clicked.connect(self.dot)
        self.pushButton_20.clicked.connect(self.end)
        

    def check_double(self):
        try:
            if self.order[-1] in ["%", "/", "x", "-", "+"]:
                self.label.setText("완성되지않은 수식입니다.")
        except IndexError:
            self.label.setText("완성되지않은 수식입니다.")

    def clear(self):
        self.order = ""
        self.to_text()

    def per(self):
        self.order += "%"
        self.to_text()

    def div(self):
        self.order += " /"
        self.to_text()

    def multi(self):
        self.order += " x"
        self.to_text()

    def minus(self):
        self.order += " -"
        self.to_text()

    def plus(self):
        self.order += " +"
        self.to_text()

    def reversal(self):
        self.order += "x(-1)"
        self.to_text()

    def dot(self):
        self.order += "."
        self.to_text()


    def number_click_1(self):
        self.order += "1"
        self.to_text()
    def number_click_2(self):
        self.order += "2"
        self.to_text()
    def number_click_3(self):
        self.order += "3"
        self.to_text()
    def number_click_4(self):
        self.order += "4"
        self.to_text()
    def number_click_5(self):
        self.order += "5"
        self.to_text()
    def number_click_6(self):
        self.order += "6"
        self.to_text()
    def number_click_7(self):
        self.order += "7"
        self.to_text()
    def number_click_8(self):
        self.order += "8"
        self.to_text()
    def number_click_9(self):
        self.order += "9"
        self.to_text()
    def number_click_0(self):
        if self.order[-1] == "/":
            self.label.setText("0으로는 나눌 수 없습니다.")
        else:
            self.order += "0"
            self.to_text()

    def zero_division_error(self):
        pass


    def percent(self):
        order_list = self.order.split("%")
        word = ""
        for val in order_list:
            if val != " ":
                word += val + "*(" + str(eval(val[:val.rfind(" ")])) + "*0.01)"
                #word += "*(" + str(eval(val))# + "*0.01)"
            else:
                pass
        self.order = word

    def end(self):
        
        self.order += " "
        self.order = self.order.replace("x", "*")
        try:
            self.percent()#수정 필요
            self.order = str(eval(self.order))
            self.label.setText(self.order)
        except ZeroDivisionError:
            self.label.setText("0으로는 나눌 수 없습니다.")
            self.order = ""
        

    def to_text(self):
        
        self.label.setText(self.order)
    

    
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())
