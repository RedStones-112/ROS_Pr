import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic


from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/qt06.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("06pt")
        
        for year in range(1990, 2025 + 1):
            self.cbYear.addItem(str(year))

        for month in range(1, 12 + 1):
            self.cbMonth.addItem(str(month))

        for day in range(1, 31 + 1):
            self.cbDay.addItem(str(day))
        
        self.cbYear.setCurrentText(str(1990))
        self.cbDay.currentIndexChanged.connect(self.printBirthday)

        self.calendarWidget.clicked.connect(self.selectDate)


    def printBirthday(self):
        year = self.cbYear.currentText()
        month = self.cbMonth.currentText()
        day = self.cbDay.currentText()
        self.lineEdit.setText(year + month.zfill(2) + day.zfill(2))


    def selectDate(self):
        date = self.calendarWidget.selectedDate()
        year = date.toString("yyyy")
        month = date.toString("M")
        day = date.toString("d")

        self.cbYear.setCurrentText(year)
        self.cbYear.setCurrentText(month)
        self.cbYear.setCurrentText(day)

        self.cbYear.setCurrentText(year)
        self.cbMonth.setCurrentText(month)
        self.cbDay.setCurrentText(day)

        self.lineEdit.setText(year + month.zfill(2) + day.zfill(2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec())







