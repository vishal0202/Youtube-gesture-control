import cv2
import numpy as np

def empty(a):
    pass
capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',640,240)
cv2.createTrackbar("hue min",'Trackbars',0,179,empty)
cv2.createTrackbar("sat min", 'Trackbars', 0, 179, empty)
cv2.createTrackbar("val min", 'Trackbars', 0, 255, empty)
cv2.createTrackbar("hue max", 'Trackbars', 0, 179, empty)
cv2.createTrackbar("sat max", 'Trackbars', 0, 255, empty)
cv2.createTrackbar("val max", 'Trackbars', 0, 255, empty)
while True:
    h_min = cv2.getTrackbarPos('hue min', 'Trackbars')
    s_min = cv2.getTrackbarPos('sat min', 'Trackbars')
    v_min = cv2.getTrackbarPos('val min', 'Trackbars')
    h_max = cv2.getTrackbarPos('hue max', 'Trackbars')
    s_max = cv2.getTrackbarPos('sat max', 'Trackbars')
    v_max = cv2.getTrackbarPos('val max', 'Trackbars')
    success, frame = capture.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame,(340,180),(540,380),(0,255,0))
    aoi = frame[180:380,340:540]
    hsv = cv2.cvtColor(aoi,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,np.array([h_min,s_min,v_min]),np.array([h_max,s_max,v_max]))
    mask = cv2.dilate(mask,(5,5),iterations=10)
    mask = cv2.GaussianBlur(mask, (3,3), cv2.BORDER_DEFAULT)
    contour, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)



    cv2.imshow('mask', mask)
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#0 97 59 84 108 255
