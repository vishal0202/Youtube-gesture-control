import cv2
import pyautogui as pg
import time
import numpy as np
pg.hotkey('alt','tab')
capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
#0 97 59 84 108 255
skin_lower = np.array([0,59,108])
skin_upper = np.array([97,84,255])
while True:
    success, frame = capture.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame,(340,180),(540,380),(0,255,0))
    aoi = frame[180:380,340:540]
    hsv = cv2.cvtColor(aoi,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,skin_lower,skin_upper)
    mask = cv2.dilate(mask,(5,5),iterations=10)
    mask = cv2.GaussianBlur(mask, (3,3), cv2.BORDER_DEFAULT)
    contour, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(list(contour))>0:
        hand = max(contour, key=lambda x: cv2.contourArea(x))
        hand_area = cv2.contourArea(hand)
        hull = [cv2.convexHull(i) for i in contour]
        hull_area = [cv2.contourArea(i) for i in hull]
        if hand_area>14000:
            cv2.drawContours(aoi,hull,-1,(0,0,0))
            area_ratio = (max(hull_area) / hand_area)
            if len(hull_area)==0:
                pass
            else:
                if area_ratio>1.3:
                    print('pause')
                    pg.press('space')
                    time.sleep(0.5)
                elif area_ratio>1and area_ratio<1.3:
                    print('mute')
                    pg.press('m')
                    time.sleep(0.5)
    else:
        pass
    cv2.imshow('mask', mask)
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
