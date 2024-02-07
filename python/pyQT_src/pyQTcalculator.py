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
        self.label.setText("")
        self.label_2.setText("0")

        self.pushButton_1.clicked.connect(self.all_clear)
        self.pushButton_2.clicked.connect(self.back_space)
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
        

    def check_double(self, order):
        try:
            
            if self.order[-1] in ["/", "x", "-", "+"]:
                if self.order[-3] == "%" and order == "%":
                    pass
                else:
                    self.order = self.order[:-2] + order
                    self.to_text()
            else:
                if self.order[-1] == "%" and order == "%":
                    pass
                else:
                    self.order += order
                    self.to_text()

        except IndexError:
            self.label_2.setText("숫자없이 연산을 진행할 수 없습니다.")


    def to_text(self):
        self.label.setText(self.order)

    def middle_calculation(self):
        self.label_2.setText(self.order)

    def all_clear(self):
        self.order = ""
        self.to_text()

    def back_space(self):
        try:
            if self.order[-1] in ["/", "x", "-", "+"]:
                self.order = self.order[:-2]
            else:
                self.order = self.order[:-1]
        except IndexError:
            pass
        self.to_text()

    def per(self):
        self.check_double("%")
        
    def div(self):
        self.check_double(" /")

    def multi(self):
        self.check_double(" x")

    def minus(self):
        self.check_double(" -")

    def plus(self):
        self.check_double(" +")

    def reversal(self):
        self.order += "x(-1)"
        self.to_text()

    def dot(self):
        try:
            if self.order[-1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                self.order += "."
        
        except IndexError:
            pass
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
        self.order += "0"
        self.to_text()
        

    


# 첫번쨰 숫자가 0일때(예 0154, 089) 계산식 정상적이지 않은 문제(해결)
# . 이후 = 하면 에러(해결)
# 연산자 이후 % 누를시 연산자가 %로 바뀌면서 무한 %가되는 에러(해결)
# 소수에 .이 추가로 붙는 에러(해...결?)
# / 뒤에 0이 눌리지않아 소숫점 나누기가 불가능한 에러(해결)
# 연산자 지우면 연산자 앞의 띄어쓰기 안지워지던 에러(해결)
# 아무것도 없이 backspace 누르면 인덱스에러 발생(해결)

    def percent(self):
        order_list = self.order.split("%")
        word = ""
        self.order += " "
        for val in order_list:
            if val != order_list[-1] and len(order_list) > 2:
                word += val + "*(" + str(eval(val[:val.rfind(" ")])) + "*0.01)"
            elif val != order_list[-1] and len(order_list) <= 2:
                word += val + "*(0.01)"
            else:
                if val != " ":
                    word += val
                
        self.order = word

    def end(self):
        self.order = self.order.replace("x", "*")
        self.percent()#테스트 필요
        try:
            if self.order[-1] in ["/", "x", "-", "+"]:
                self.label_2.setText("수식을 완성시켜주세요")
            else:
                self.order = str(eval(self.order))
                self.label.setText(self.order)

        except IndexError:
            self.label_2.setText("숫자없이 연산을 진행할 수 없습니다.")
            
        except ZeroDivisionError:
            self.label_2.setText("0으로는 나눌 수 없습니다.")
        
        except SyntaxError:
            self.label_2.setText("정상적인 수식이 아닙니다.")
    

    
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())
