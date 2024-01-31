import serial

py_serial = serial.Serial(
    port = "/dev/ttyACM0",
    baudrate=9600
)
while 1:
    commend = input("각도")
    py_serial.write(commend.encode())
    