import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic




from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/qt08.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("08pt")
        
        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()
        
        self.lineEdit_1.setText(str(min))
        self.lineEdit_2.setText(str(max))
        self.lineEdit_3.setText(str(step))
        
        self.slider.setRange(min, max)
        self.slider.setSingleStep(step)

        self.spinBox.valueChanged.connect(self.change_spin_box)
        self.pushButton.clicked.connect(self.Apply)
        self.slider.valueChanged.connect(self.change_slider)

        self.pixmap = QPixmap()
        self.pixmap.load("/home/rds/amr_ws/ROS_Pr-1/python/cv_data/test_img")
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())



    def Apply(self):
        min = self.lineEdit_1.text()
        max = self.lineEdit_2.text()
        step = self.lineEdit_3.text()

        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))

        self.slider.setRange(int(min), int(max))
        self.slider.setSingleStep(int(step))

    
    def change_slider(self):
        actualValue = self.slider.value()
        self.label_4.setText(str(actualValue))
        self.spinBox.setValue(actualValue)


    def change_spin_box(self):
        actualValue = self.spinBox.value()
        self.label_4.setText(str(actualValue))
        self.slider.setValue(actualValue)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec())








