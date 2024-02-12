import cv2
import numpy as np
import sys
oldx = oldy = -1


def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    print(cv2.EVENT_MOUSEMOVE)
    if event == cv2.EVENT_LBUTTONDOWN:
        print("EVENT_LBUTTONDOWN: %d, %d," % (x,y))
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print("EVENT_LBUTTONUP: %d, %d" % (x,y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x,y), (0,0,255), 4, cv2.LINE_AA)
            cv2.imshow("image",img)

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow(winname="image")
cv2.setMouseCallback("image", on_mouse, img)

cv2.imshow("image", img)
cv2.waitKey()




cv2.destroyAllWindows()