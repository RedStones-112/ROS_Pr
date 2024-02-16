# %이후 숫자가 눌러지는 에러 (해결)
# 첫번쨰 숫자가 0일때(예 0154, 089) 계산식 정상적이지 않은 문제(해결)
# . 이후 = 하면 에러(해결)
# 연산자 이후 % 누를시 연산자가 %로 바뀌면서 무한 %가되는 에러(해결)
# / 뒤에 0이 눌리지않아 소숫점 나누기가 불가능한 에러(해결)
# 연산자 지우면 연산자 앞의 띄어쓰기 안지워지던 에러(해결)
# 아무것도 없이 backspace 누르면 인덱스에러 발생(해결)
# 여러개의 %연산이 들어갈 시 에러발생(해결)
# %연산 오류(해결)
# 부호 반전 반복시 무한으로 수식이 늘어나던 문제(해결)
# .뒤에 반전붙이고 %가 붙는 문제(해결)
# 소수에 .이 추가로 붙는 에러(해결)
# 정수와 소수의 계산시 쓰래기값 붙음(해결못함)
# 연속으로 괄호를 열거나 닫을 수 없던 문제(해결)
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import os

#/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/calculator_1.02.ui
from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/calculator_1.02.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("PyQTcalculator")
        self.order = ""
        self.operators = ["/", "x", "-", "+"]
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.label.setText("")
        self.label_2.setText("")

        self.pushButton_5.clicked.connect(self.number_click)
        self.pushButton_6.clicked.connect(self.number_click)
        self.pushButton_7.clicked.connect(self.number_click)
        self.pushButton_9.clicked.connect(self.number_click)
        self.pushButton_10.clicked.connect(self.number_click)
        self.pushButton_11.clicked.connect(self.number_click)
        self.pushButton_13.clicked.connect(self.number_click)
        self.pushButton_14.clicked.connect(self.number_click)
        self.pushButton_15.clicked.connect(self.number_click)
        self.pushButton_18.clicked.connect(self.number_click)
        self.pushButton_1.clicked.connect(self.all_clear)
        self.pushButton_2.clicked.connect(self.back_space)
        self.pushButton_3.clicked.connect(self.Operator)
        self.pushButton_4.clicked.connect(self.Operator)
        self.pushButton_8.clicked.connect(self.Operator)
        self.pushButton_12.clicked.connect(self.Operator)
        self.pushButton_16.clicked.connect(self.Operator)
        self.pushButton_17.clicked.connect(self.reversal)
        self.pushButton_19.clicked.connect(self.dot)
        self.pushButton_20.clicked.connect(self.end)
        self.pushButton_21.clicked.connect(self.open_parenthesis)
        self.pushButton_22.clicked.connect(self.close_parenthesis)
        

    def Operator(self):
        self.check_double(self.sender().text())

    def number_click(self):
        self.to_text(self.sender().text())


    def check_double(self, order):
        try:
            if self.order[-1] in self.operators:
                
                if order == "%":
                    self.label_2.setText("숫자를 먼저 입력해 주십시오")
                else:
                    self.order = self.order[:-2] + order
                    self.label.setText(self.order)

            else:
                if self.order[-1] == "%" and order == "%":
                    self.order = self.order[:-1]
                    self.label.setText(self.order)
                elif self.order[-1] == "(":
                    self.label_2.setText("숫자를 먼저 입력해 주십시오")
                else:
                    self.order += order
                    self.label.setText(self.order)


            self.middle_calculation()

        except IndexError:
            self.label_2.setText("숫자없이 연산을 진행할 수 없습니다.")



    def to_text(self, order):
        try:
            if self.order[-1] == "%" or self.order[-5:] == "x(-1)" or self.order[-1] == ")":
                self.label_2.setText("먼저 연산자를 붙여주세요.")
            else:
                self.order += order
                self.label.setText(self.order)
                self.middle_calculation()

        except IndexError: #
            self.order += order
            self.label.setText(self.order)
            self.middle_calculation()

    

    def middle_calculation(self):
        try:
            result = self.order.replace("x", "*")
            result = self.percent(result)
            result = eval(result)
            self.label_2.setText(str(result))
        except:
            pass



    def all_clear(self):
        self.order = ""
        self.label.setText(self.order)
        self.label_2.setText("")



    def back_space(self):
        try:
            if self.order[-1] in self.operators:
                self.order = self.order[:-2]
            elif self.order[-5:] == "x(-1)":
                self.order = self.order[:-5]
            else:
                self.order = self.order[:-1]
        except IndexError:# null data + back_space
            pass


        self.label.setText(self.order)
        self.middle_calculation()



    def reversal(self):
        try:
            if self.order[-5:] == "x(-1)":
                self.order = self.order[:-5]
            elif self.order[-1] in ["/", "x", "-", "+", "("]:
                pass
            else:
                self.order += "x(-1)"
        except:
            pass


        self.label.setText(self.order)
        self.middle_calculation()



    def dot(self):
        try:
            if self.order.rfind(" ") == -1 and self.order.count(".") == 0:
                if self.order[-1] in self.numbers:
                    self.order += "."
            elif self.order.rfind(" ") != -1 and self.order[self.order.rfind(" "):].count(".") == 0:
                if self.order[-1] in self.numbers:
                    self.order += "."
        
        except IndexError: # null data + dot
            pass
        self.label.setText(self.order)


    
    def open_parenthesis(self):#앞에 연산기호만 허용
        try:
            if self.order[-1] in self.operators or self.order[-1] == "(":
                self.order += "("
            else:
                self.label_2.setText("연산기호 없이 괄호를 열 수 없습니다.")
        
        except IndexError:
            self.order += "("

        self.label.setText(self.order)

    def close_parenthesis(self):#앞에 숫자, %, ) 만 허용
        try:
            if self.order.count("(") > self.order.count(")"):
                if self.order[-1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "%", ".", ")"]:
                    self.order += ")"
                else:
                    self.label_2.setText("기호 뒤에 괄호를 닫거나 공백괄호를 만들 수 없습니다.")
            else:
                self.label_2.setText("열려있는 괄호가 없습니다.")
        except IndexError:
            pass


        self.middle_calculation()
        self.label.setText(self.order)
    

        
    def percent(self, order):
        if order.count("%") >= 1:
            order += " "
            order_list = order.split("%")
            result = ""

            for val in order_list:
                try:
                    if val.count(" ") == 0:
                        result = val + "*0.01"
                    elif val != order_list[-1]:
                        result = "(" + result + val[:val.rfind(" ")] + ")" + f"""*(1{val[val.rfind(" ")+1]}({val[val.rfind(" ")+2:]}*0.01))"""
                        
                    elif val == order_list[-1]:
                        result += val
                    
                except:
                    pass
        else:
            result = order


        return result

    def end(self):
        self.order = self.order.replace("x", "*")
        try:
            if self.order[-1] in self.operators:
                self.label_2.setText("수식을 완성시켜주세요")
            else:
                self.order = self.percent(self.order)
                self.order = str(eval(self.order))
                self.label.setText(self.order)

        except IndexError:
            self.label_2.setText("숫자없이 연산을 진행할 수 없습니다.")
            
        except ZeroDivisionError:
            self.label_2.setText("0으로는 나눌 수 없습니다.")
        
        except SyntaxError as E:
            if str(E)[:20] == "'(' was never closed":
                self.label_2.setText("괄호가 닫히지 않은 수식입니다.")
            else:
                self.label_2.setText("정상적인 수식이 아닙니다.")
    

    
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())
