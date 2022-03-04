import cv2
import numpy as np
import time 

cam = cv2.VideoCapture(0)
time.sleep(2)
bg = 0

#Creating video file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outputFile = cv2.VideoWriter('ouput.avi', fourcc, 20.0, (640, 480))

for i in range(60):
    ret, frame = cam.read()

while (cam.isOpened()):
    ret, img = cam.read()
    if not ret: 
        break
    
    frame = cv2.resize(frame, (640, 480))
    img = cv2.resize(img, (640, 480))

    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])
    mask = cv2.inRange(frame, u_black, l_black)
    res = cv2.bitwise_and(frame, frame, mask= mask)
    f = frame - res
    f = np.where(f == 0, img, f)

    cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()