import serial
import struct
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
class Receiver(QThread):
    detected = pyqtSignal(bytes)
    recvTotal = pyqtSignal(int)
    changedTotal = pyqtSignal()
    noCard = pyqtSignal()
    def __init__(self, conn, parent=None):
        super(Receiver, self).__init__(parent)
        self.isRunning = False
        self.conn = conn
        print("recv_init")

    def run(self):
        print("recv start")
        self.isRunning = True
        while (self.isRunning == True) :
            if self.conn.readable():
                res = self.conn.read_until(b"\n")
                if len(res) > 0:
                    # print(res)
                    res = res[:-2]
                    cmd = res[:2].decode()
                    if cmd == "GS" and res[2] == 0:
                        print("recv detected")
                        self.detected.emit(res[3:])
                    elif cmd == "GT" and res[2] == 0:
                        print("recvTotal")
                        print(len(res))
                        self.recvTotal.emit(int.from_bytes(res[3:7], "little"))
                    elif cmd == "ST" and res[2] == 0:
                        print("setTotal")
                        self.changedTotal.emit()
                    elif res[2].to_bytes(1, "litle") == b"\xfa":
                        print("recv noCard")
                        self.noCard.emit()
                    else:
                        print("error")
                        print(res)

    def stop(self):
        print("recv stop")
        self.isRunning = False

from_class = uic.loadUiType("/home/rds/Desktop/ROS_Pr/python/pyQT_src/card_machine.ui")[0]
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.uid = bytes(4)

        self.conn = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1)

        self.recv = Receiver(self.conn)
        self.recv.start()
        
        self. resetButton.clicked.connect(self.reset)
        self. paymentButton.clicked.connect(self.payment)
        self. chargeButton.clicked.connect(self.charge)

        self.disable()

        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.getStatus)
        self.timer.start()

        self.recv.detected.connect(self.detected)
        self.recv.recvTotal.connect(self.recvTotal)
        self.recv.changedTotal.connect(self.changedTotal)
        self.rece.noCard.connect(self.noCard)

    def noCard(self):
        print("noCard")
        if (self.timer.isActive() == False):
            print("startTimer")
            self.timer.start()
        self.disable()

    def changedTotal(self):
        self.getTotal()

    def recvTotal(self, total):
        print("tecvTotal")
        self.enble(total)
        self.chargeEdit.setText("")
        self.paymentEdit.setText("")

    def detected(self, uid) : 
        print("detected")
        self.uid = uid
        self.timer.stop()
        # self.enable(0)
        self.getTotal()
        self.resetButton.setDisabled(False)
        return

        
    def enable(self, total):
        self.totalLabel.setText(str(total))
        self.chargeEdit.setDisabled(False)
        self.chargeButton.setDisabled(False)
        self.paymentEdit.setDisabled(False)
        self.paymentButton.setDisabled(False)

    def disable(self):
        self.totalLabel.setText("-")
        self.resetButton.setDisabled(True)
        self.chargeEdit.setDisabled(True)
        self.chargeButton.setDisabled(True)
        self.paymentEdit.setDisabled(True)
        self.paymentButton.setDisabled(True)
        
    def send(self, command, data=0):
        print("send")
        req_data = struct.pack("<2s4sic", command, self.uid, data, b"\n")
        self.conn.write(req_data)
        return
    
    def getStatus(self):
        print("getstats")
        self.send(b"GS")
        return
    
    def getTotal(self):
        print("gettotal")
        self.send(b"GT")
        return
    
    def setTotal(self, total):
        print("settotal")
        self.send(b"ST", total)
        return
    
    
    
    def reset(self):
        print("reset")
        self.setTotal(0)
        return

    def charge(self):
        print("charge")
        total = int(self.totalLabel.text())
        charge = int(self.chargeEdit.text())
        self.setTotal(total + charge)
        return

    def payment(self):
        print("payment")
        total = int(self.totalLabel.text())
        payment = int(self.paymentEdit.text())
        if (total < payment):
            QMessageBox.warning(self, "test", "잔액부족")
            self.paymentEdit.setText("")
        else :
            total = total - payment
            self.setTotal(total)
        return



def main():
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec())



if __name__ == "__main__":
    main()