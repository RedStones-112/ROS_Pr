import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import mysql.connector
import pandas as pd



from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/qt07-1.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("07pt")
        
        
        agency_list = ["All", "EDAM엔터테이먼트", "울림엔터테이먼트", "나무엑터스", "YG엔터테이먼트", "안테나"]
        job_list = ["All", "가수", "텔런트", "영화배우", "MC", "개그맨", "모델"]
        gender_list = ["All", "남자", "여자", "그외"]

        #self.tableWidget.horizontalHeader().setSectionResizeMode()
        
        for job in job_list:
            self.job_cb.addItem(job)
        for agency in agency_list:
            self.agency_cb.addItem(agency)
        for gender in gender_list:
            self.gender_cb.addItem(gender)
        
        #self.start_BD.setDateTime(19600101)
        self.pushButton.clicked.connect(self.create_query)


    def create_query(self):
        job = self.job_cb.currentText()
        sex = self.gender_cb.currentText()
        agency = self.agency_cb.currentText()

        if sex == "남자":
            sex = "m"
        elif sex == "여자":
            sex = "f"

        Query = """select * from celeb where """
        names = ["job_title", "sex", "agency"]
        data = [job, sex, agency]
        
        Query += f"""birthday <= {self.end_BD.date().toString("yyyyMMdd")} and birthday >= {self.start_BD.date().toString("yyyyMMdd")} """

        for i in range(len(data)):# 

            if data[i] == "All":
                pass
            else:
                if names[i] == "job_title":
                    Query += f"and {names[i]} like '%{data[i]}%'"
                else:
                    Query += f"and {names[i]}='{data[i]}'"
                    

           
        Query += ";"


        self.PyToDB(Query)


    def PyToDB(self, Query):

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "8470",
            database = "amrbase",
        )
        cur = mydb.cursor()
        cur.execute(Query)
        result = cur.fetchall()
        mydb.close()
        df = pd.DataFrame(result)


        
        self.Add(df)



    def Add(self, df):
        self.tableWidget.clear()
        try:
            for i in range(0, len(df)):
                self.tableWidget.insertRow(i)
                for j in range(0, len(df.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(df[j][i])))
        
        except KeyError:
            pass
        except ValueError:
            pass
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec())







