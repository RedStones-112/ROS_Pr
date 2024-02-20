import sys
import cv2, imutils
import urllib.request
import time
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic













class Camera(QThread) :
    update = pyqtSignal()
    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running = True


    def run(self):
        count = 0
        while self.running == True:
            self.update.emit()
            time.sleep(0.1)











from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/qt09.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("09pt")

        self.pixmap = QPixmap()

        self.camera = Camera(self)
        self.camera.daemon = True

        self.record = Camera(self)
        self.record.daemon = True

        self.playVideo = Camera(self)
        self.playVideo.deamon = True

        self.isCameraOn = 0
        self.count = 0
        self.isRECOn = 0
        self.RECButton.hide()


        self.pushButton.clicked.connect(self.openFile)
        self.videoButton.clicked.connect(self.openVideo)
        self.camera_btn.clicked.connect(self.clickCmera)
        self.RECButton.clicked.connect(self.clickREC)
        self.camera.update.connect(self.updateCamera)


    def updateCamera(self):
        ret, img = self.video.read()
        if ret:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            h, w, c = img.shape
            qimage = QImage(img.data, w, h, w*c, QImage.Format_RGB888)
            
            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            self.label.setPixmap(self.pixmap)
        
        self.count += 1


    def clickCmera(self):
        
        if self.isCameraOn == 0:
            self.camera_btn.setText("camera off")
            self.isCameraOn = 1
            self.RECButton.show()

            self.cameraStart()

        else:
            self.camera_btn.setText("camera on")
            self.isCameraOn = 0
            self.RECButton.hide()

            self.cameraStop()
            self.recordStop()


    def cameraStart(self):
        self.camera.running = True
        self.camera.start()
        self.video = cv2.VideoCapture(-1)

    def cameraStop(self):
        self.camera.running = False
        self.count = 0
        self.video.release()


    def updateRecording(self):
        self.writer.write(self.img)


    def clickREC(self):
        if self.isRECOn == 0:
            self.RECButton.setText("REC End")
            self.isRECOn = 1

            self.recordStart()


        else:
            self.RECButton.setText("REC Start")
            self.isRECOn = 0

            self.recordStop()


    def recordStart(self):
        self.record.running = True
        self.record.start()

        self.now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.now + ".avi"
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")

        w = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        self.writer = cv2.VideoWriter(filename, self.fourcc, 20.0, (w,h))

    def recordStop(self):
        self.record.running = False

        if self.isRECOn == 1:
            self.writer.release()
        
        


    def openFile(self):
        file = QFileDialog.getOpenFileName(filter="Image (*.*)")

        image = cv2.imread(file[0])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        h, w, c = image.shape
        qimage = QImage(image.data, w, h, w*c, QImage.Format_RGB888)

        self.pixmap = self.pixmap.fromImage(qimage)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())


    def playStart(self, file):
        self.camera.running = True
        self.camera.start()
        self.video = cv2.VideoCapture(file[0])
        
    def playStop(self):
        self.camera.running = False
        self.count = 0
        self.video.release()

    def openVideo(self):
        file = QFileDialog.getOpenFileName(filter="Video (*avi *webm)")
        print(file)
        self.playStart(file)
        

        if self.video.isOpened():
            f_width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
            f_height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
            f_channel = self.video.get(cv2.CAP_PROP_CHANNEL)


        while self.video.isOpened():
            ret, frame = self.video.read()

            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                qimage = QImage(frame.data, f_width, f_height, f_width*f_channel, QImage.Format_RGB888)

                self.pixmap = self.pixmap.fromImage(qimage)
                self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

                self.label.setPixmap(self.pixmap)
                self.label.resize(self.pixmap.width(), self.pixmap.height())
                key = cv2.waitKey(10)
                if key == 27:
                    break
            else:
                break
                
        self.playStop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec())








