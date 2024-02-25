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







from_class = uic.loadUiType("./python/pyQT_src/camera_app_re.ui")[0]
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

        self.camera = Camera(self)
        self.camera.daemon = True



        self.status_Thread = Camera(self)
        self.status_Thread.deamon = True



        
        self.video = None
        self.image = None
        
        self.draw_status = "False"
        self.display_status = "None"
        self.isCameraOn = False
        self.isRECOn = False
        

        self.isImage = False
        

        self.pointCount = 0
        self.pointXY = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.x = None
        self.y = None

        self.org = np.array([[None]])
        self.capture = np.array([[None]])




        min_max = [0, 100]
        self.HSV = [min_max[1], min_max[1], min_max[1]]
        self.RGB = [min_max[1], min_max[1], min_max[1]]

    

        self.R_slider.setRange(min_max[0], min_max[1])
        self.R_slider.setValue(self.RGB[0])
        self.G_slider.setRange(min_max[0], min_max[1])
        self.G_slider.setValue(self.RGB[1])
        self.B_slider.setRange(min_max[0], min_max[1])
        self.B_slider.setValue(self.RGB[2])

        # self.threshold_slider.setRange(min_max[0], 255)
        # self.threshold_slider.setValue(self.threshold_RGB)

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
        self.camera_btn.clicked.connect(self.clickCamera)
        self.RECButton.clicked.connect(self.clickREC)
        self.pointButton.clicked.connect(self.clickFourPoint)
        self.saveButton.clicked.connect(self.saveImg)
        
        self.camera.update.connect(self.updateDisplay)
        self.status_Thread.update.connect(self.updateStatus)
        


    def imgToPixmap(self, img):
        h, w, c = img.shape
        qimage = QImage(img.data, w, h, w*c, QImage.Format_RGB888)
        
        self.pixmap = self.pixmap.fromImage(qimage)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())

    def unfurl(self):
        
        points1 =  self.pointXY
        #points1.sort() ## point 순서 정하는 알고리즘 필요
        points1 = np.float32(points1)
        
        img = self.convertPixMapToArr()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        points2 = np.float32([[0, 0],[0, 700],[700, 0],[700, 700]]) #수정필요

        M = cv2.getPerspectiveTransform(points1, points2)

        img = cv2.warpPerspective(img, M, (1100,1100))# 수정필요

        img = self.pretreatment(img)
        img = cv2.flip(img, 0)

        h, w, c = img.shape
        qimage = QImage(img.data, w, h, w*c, QImage.Format_RGB888)
        
        self.pixmap = self.pixmap.fromImage(qimage)
        self.pixmap = self.pixmap.scaled(self.label.width(), self.label.height())

        self.label.setPixmap(self.pixmap)
        

    def compareImg(self, img):
        pixmap_img = self.convertPixMapToArr()


    def saveImg(self):
        img = self.convertPixMapToArr()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite("./cap_img.png", img)

    def clickFourPoint(self):
        if self.canDraw == "True":
            self.pointCount = 0
            self.canDraw = "point"
            self.pointButton.setText("cancel")

        elif self.canDraw == "point":
            self.canDraw = "True"
            self.pointButton.setText("4 point")


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

    def clickCapture(self):
        if self.display_status == "Video":
            self.display_status = "Image"
            
            self.image = self.convertPixMapToArr()
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            
        
    


    def draw_start(self):
        pass

    def draw_end(self):
        pass
    
    def mouseMoveEvent(self, event):
        if self.canDraw == "True":
            thick = 5
            
            self.pen_color = self.pen_color_box.currentText()
            eval(f"self.painter.setPen(QPen(Qt.{self.pen_color}, {thick}, Qt.SolidLine))")
            if self.x is None:
                self.x = event.x()
                self.y = event.y()
                return
            
            x = self.label.x()
            y = self.label.y()

            self.painter.drawLine(self.x - x, self.y - y, event.x() - x, event.y() - y)
            
            self.update()

            self.x = event.x()
            self.y = event.y()
            

    def mouseReleaseEvent(self):
        self.x = None
        self.y = None

        
    def mousePressEvent(self, event):
        if self.canDraw == "point" and self.pointCount < 4:
            
            self.painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            
            x = self.label.x()
            y = self.label.y()

            self.painter.drawEllipse(event.x() - x, event.y() - y, 5, 5)
            
            self.update()
            
            self.pointXY[self.pointCount] = [event.x() - x, event.y() - y]
            self.pointCount += 1
            if self.pointCount == 4:
                self.canDraw = "False"
                self.unfurl()
                self.clickFourPoint()

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


    


    def updateDisplay(self):
        ret = False
        if self.display_status == "Video":
            ret, img = self.video.read()
        elif self.display_status == "Image":
            img = self.image
            
        
            
        if ret or self.image.all() != None:
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
                
                self.imgToPixmap(img)

                if self.isRECOn == True:
                    self.writer.write(org)
                    self.draw_REC()
        
    def updateStatus(self):
        pass

    def clickCamera(self):
        if self.isCameraOn == False:
            self.camera_btn.setText("camera off")
            self.isCameraOn = True
            
            
            self.cameraStart()

        else:
            self.camera_btn.setText("camera on")
            self.isCameraOn = False
            
            self.cameraStop()
            

    def cameraStart(self):
        self.display_status = "Video"
        self.camera.running = True
        self.camera.start()
        
        self.video = cv2.VideoCapture(-1)
        self.RECButton.show()
        self.capture_btn.show()

    def cameraStop(self):
        self.display_status = "None"
        self.camera.running = False
        
        self.video.release()
        self.RECButton.hide()
        self.capture_btn.hide()

    def playStart(self, file):
        self.display_status = "Video"
        self.camera.running = True
        self.camera.start()
        
        self.video = cv2.VideoCapture(file[0])
        self.RECButton.show()
        self.capture_btn.show()
        
        self.video_width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.video_height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.video_channel = self.video.get(cv2.CAP_PROP_CHANNEL)
        
        
        
    def playStop(self):
        self.camera.running = False
        self.video.release()
    
    def clickREC(self):
        if self.isRECOn == False:
            self.RECButton.setText("REC off")
            self.isRECOn = True
            
            self.recordStart()

        else:
            self.RECButton.setText("REC on")
            self.isRECOn = False
            
            self.RECButton.hide()
            self.capture_btn.hide()
            self.recordStop()

    def recordStart(self):
        pass

    def recordStop(self):
        pass
        
    def draw_REC(self):
        pass
        
    def startImage(self):
        self.display_status = "Image"
        self.image_Thread.running = True
        self.image_Thread.start()
    
    def endImage(self):
        self.camera.running = False
        

    def openFile(self):################
        file = QFileDialog.getOpenFileName(filter="Image,Video (*png *jpg *avi *webm)")
        if "jpg" in file[0] or "png" in file[0]:
            self.image = cv2.imread(file[0])
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.startImage()
            
        elif "avi" in file[0] or "webm" in file[0]:
            self.playStart(file)
                        
        else: # 추후 에러창 추가
            pass



        

            

            
                
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec())








