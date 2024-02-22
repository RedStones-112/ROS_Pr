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













class Camera(QThread) :
    update = pyqtSignal()
    isRECon = False
    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.running = False


    def run(self):
        count = 0
        while self.running == True:
            self.update.emit()
            
            time.sleep(0.05)












from_class = uic.loadUiType("/home/rds/amr_ws/ROS_Pr-1/python/pyQT_src/camera_app.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__() ## 상속받은거 __init__ 동작
        self.setupUi(self)
        self.setWindowTitle("camera_app")
        self.RECButton.hide()
        self.capture_btn.hide()

        self.pixmap = QPixmap()
        self.label.setPixmap(self.pixmap)

        self.camera = Camera(self)
        self.camera.daemon = True

        self.record = Camera(self)
        self.record.daemon = True

        self.playVideo = Camera(self)
        self.playVideo.deamon = True

        self.isCameraOn = 0
        self.count = 0
        self.threshold_RGB = 0
        self.isRECOn = False
        
        self.canDraw = False
        
        min_max = [0, 100]
        self.HSV = [min_max[1], min_max[1], min_max[1]]
        self.RGB = [min_max[1], min_max[1], min_max[1]]

        self.pen_color = "black"
        self.x = None
        self.y = None





        self.R_slider.setRange(min_max[0], min_max[1])
        self.R_slider.setValue(self.RGB[0])
        self.G_slider.setRange(min_max[0], min_max[1])
        self.G_slider.setValue(self.RGB[1])
        self.B_slider.setRange(min_max[0], min_max[1])
        self.B_slider.setValue(self.RGB[2])

        self.threshold_slider.setRange(min_max[0], 255)
        self.threshold_slider.setValue(self.threshold_RGB)

        self.S_slider.setRange(min_max[0], min_max[1])
        self.S_slider.setValue(self.HSV[1])
        self.V_slider.setRange(min_max[0], min_max[1])
        self.V_slider.setValue(self.HSV[2])






        self.R_slider.valueChanged.connect(self.silder)
        self.G_slider.valueChanged.connect(self.silder)
        self.B_slider.valueChanged.connect(self.silder)

        self.threshold_slider.valueChanged.connect(self.silder)

        self.S_slider.valueChanged.connect(self.silder)
        self.V_slider.valueChanged.connect(self.silder)





        self.capture_btn.clicked.connect(self.clickCapture)
        self.pushButton.clicked.connect(self.openFile)
        self.videoButton.clicked.connect(self.openVideoFile)
        self.camera_btn.clicked.connect(self.clickCamera)
        self.RECButton.clicked.connect(self.clickREC)


        
        self.camera.update.connect(self.updateCamera)
        # self.record.update.connect(self.playVideo)



    def pretreatment(self, img): # 전처리
        if self.blur_box.isChecked():###blur
            img = cv2.GaussianBlur(src=img, ksize=(5, 5), sigmaX=10)

        if self.cannyEdge_box.isChecked():
            img = cv2.Canny(img, 50, 200)

        img = self.contorl_color(img)

        return img

    def convertPixMapToArr(self):
        
        img = (self.pixmap.toImage()).convertToFormat(QImage.Format.Format_RGBA8888)
        w = img.width()
        h = img.height()

        img = img.bits()
        img.setsize(h * w * 4)
        img = np.array(img).reshape((h, w, 4))



        return img

    def binary(self, img):
        
        img = cv2.inRange(img, (self.threshold_RGB, self.threshold_RGB, self.threshold_RGB), (255, 255, 255))
        
        return img

    def clickCapture(self, img):
        if self.camera.running == True:
            self.clickCamera()

        img = self.convertPixMapToArr()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = self.pretreatment(img)


        h, w, c = img.shape
        qimage = QImage(img.data, w, h, w*c, QImage.Format_RGB888)
        
        self.pixmap = self.pixmap.fromImage(qimage)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

        self.label.setPixmap(self.pixmap)



        self.draw_start()

        #cv2. imwrite("/home/rds/amr_ws/ROS_Pr-1/python/cv_data/cap_img.png",img)
    


    def draw_start(self):
        self.canDraw = True

    def draw_end(self):
        self.canDraw = False
        self.x = None
        self.y = None
    
    def mouseMoveEvent(self, event):
        if self.canDraw == True:
            thick = 5
            self.painter = QPainter(self.label.pixmap())
            self.pen_color = self.pen_color_box.currentText()
            eval(f"self.painter.setPen(QPen(Qt.{self.pen_color}, {thick}, Qt.SolidLine))")
            if self.x is None:
                self.x = event.x()
                self.y = event.y()
                return
            
            x = self.label.x()
            y = self.label.y()

            self.painter.drawLine(self.x - x, self.y - y, event.x() - x, event.y() - y)
            self.painter.end()
            self.update()

            self.x = event.x()
            self.y = event.y()
            self.painter.end
        
        

    #def draw_square (self):###



    def silder(self):
        self.RGB[0] = self.R_slider.value()
        self.RGB[1] = self.G_slider.value()
        self.RGB[2] = self.B_slider.value()

        self.threshold_RGB = self.threshold_slider.value()

        self.HSV[1] = self.S_slider.value()
        self.HSV[2] = self.V_slider.value()


        self.threshold_val.setText(f"threshold : {self.threshold_RGB}")


    def contorl_color(self, img):
            
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            img[:, :, 0] = img[:, :, 0] * (self.RGB[0] / 100)
            img[:, :, 1] = img[:, :, 1] * (self.RGB[1] / 100)
            img[:, :, 2] = img[:, :, 2] * (self.RGB[2] / 100)
            
            img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

            img[:, :, 1] = img[:, :, 1] * (self.HSV[1] / 100)
            img[:, :, 2] = img[:, :, 2] * (self.HSV[2] / 100)
            
            img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

            return img


    


    def updateCamera(self):
        ret, img = self.video.read()

        if ret:
            org = img
            
            
            img = self.pretreatment(img)

            if self.binary_box.isChecked():#gray
                img = self.binary(img)
                h, w = img.shape
                qimage = QImage(img.data, w, h, QImage.Format_Grayscale8)
                
                self.pixmap = self.pixmap.fromImage(qimage)
                self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

                self.label.setPixmap(self.pixmap)
                if self.isRECOn == True:
                    self.writer.write(org)#### 그레이스케일 녹화 수정 필요

            else:#color
                
                h, w, c = img.shape
                qimage = QImage(img.data, w, h, w*c, QImage.Format_RGB888)
                
                self.pixmap = self.pixmap.fromImage(qimage)
                self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

                self.label.setPixmap(self.pixmap)
                if self.isRECOn == True:
                    self.writer.write(org)
                    self.draw_REC()
        self.count += 1


    def clickCamera(self):
        if self.isCameraOn == 0:
            self.camera_btn.setText("camera off")
            self.isCameraOn = 1
            self.RECButton.show()
            self.capture_btn.show()

            self.cameraStart()

        else:
            self.camera_btn.setText("camera on")
            self.isCameraOn = 0
            self.RECButton.hide()
            self.capture_btn.hide()

            self.cameraStop()
            self.recordStop()


    def cameraStart(self):
        self.camera.running = True
        self.camera.start()
        if self.canDraw == True:
            self.draw_end()
        self.video = cv2.VideoCapture(-1)

    def cameraStop(self):
        self.camera.running = False
        self.count = 0
        self.video.release()


    def updateRecording(self):
        self.writer.write(self.img)


    def clickREC(self):
        if self.isRECOn == False:
            self.RECButton.setText("REC End")
            self.isRECOn = True

            self.recordStart()


        else:
            self.RECButton.setText("REC Start")
            self.isRECOn = False

            self.recordStop()


    def recordStart(self):

        self.now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.now + ".avi"
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")

        w = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        self.writer = cv2.VideoWriter(filename, self.fourcc, 20.0, (w,h))

    def recordStop(self):
        if self.isRECOn == True:
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
        if self.canDraw == True:
            self.draw_end()
            
        if self.camera.running == True:###################
            pass
        self.RECButton.show()
        self.capture_btn.show()
        self.camera.running = True
        self.camera.start()
        self.video = cv2.VideoCapture(file[0])
        
    def playStop(self):
        self.RECButton.hide()
        self.capture_btn.hide()
        self.camera.running = False
        self.count = 0
        self.video.release()

    def openVideoFile(self):
        file = QFileDialog.getOpenFileName(filter="Video (*avi *webm)")
        
        self.playStart(file)
        self.video_width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.video_height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.video_channel = self.video.get(cv2.CAP_PROP_CHANNEL)

        
    def draw_REC(self):
        painter = QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.red, 10, Qt.SolidLine))
        
        font = QFont()
        font.setFamily("Times")
        font.setBold(True)
        font.setPointSize(40)

        painter.setFont(font)
        painter.drawText(50, 50, "REC")
        painter.end


    def playVideo(self):
        ret, frame = self.video.read()
        if ret:
            frame = self.contorl_color(frame)
            self.display = frame


            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            qimage = QImage(frame.data, self.video_width, self.video_height, self.video_width*self.video_channel, QImage.Format_RGB888)

            self.pixmap = self.pixmap.fromImage(qimage)
            self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

            if self.isRECOn == True:
                self.writer.write(frame)
                self.draw_REC()
            self.label.setPixmap(self.pixmap)
            self.label.resize(self.pixmap.width(), self.pixmap.height())

            
                
        self.playStop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec())








