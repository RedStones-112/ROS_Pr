#import tensorflow as tf


################################
answer = []
################################
import sys
import cv2, imutils
import urllib.request
import time
import datetime
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/camera_app_re.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("camera_app")
        self.RECButton.hide()
        self.capture_btn.hide()
        self.pointButton.hide()

        self.pixmap = QPixmap()
        self.label.setPixmap(self.pixmap)



        
        self.pushButton.clicked.connect(self.openFile)
        






    def openFile(self):################
        file = QFileDialog.getOpenFileName(filter="Image,Video (*png *jpg *avi *webm)")
        if  "jpg" in file[0] or "png" in file[0]:
            print("I")
            # image = cv2.imread(file[0])
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        elif "avi" in file[0] or "webm" in file[0]:
            print("V")
            # self.playStart(file)
            # self.video_width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
            # self.video_height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
            # self.video_channel = self.video.get(cv2.CAP_PROP_CHANNEL)

        


            

            
                
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec())








