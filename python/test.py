#import tensorflow as tf


################################
answer = []
################################
import cv2



path = '/home/rds/Videos/Screencasts/20240220_171801.avi'


cap = cv2.VideoCapture(path)



while cap.isOpened():
    ret, img = cap.read()
    print(ret)
    if ret:
        cv2.imshow("frame", img)
        cv2.waitKey(25)
    else:
        break

cap.release()
cv2.destroyAllWindows()