import cv2
import numpy as np

def empty(a):
    pass

bird_path = 'Chapter5/resources/bird.jpg'
cv2.namedWindow("Track Bar")
cv2.resizeWindow("Track Bar",640,240)
cv2.createTrackbar("hue min","Track Bar",0,179,empty)
cv2.createTrackbar("hue max","Track Bar",179,179,empty)
cv2.createTrackbar("saturation min","Track Bar",0,255,empty)
cv2.createTrackbar("saturation max","Track Bar",255,255,empty)
cv2.createTrackbar("value min","Track Bar",0,255,empty)
cv2.createTrackbar("value max","Track Bar",255,255,empty)

while True:
    img3 = cv2.imread(bird_path)
    img3s = cv2.resize(img3,(400,300))
    imgHSV = cv2.cvtColor(img3s, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("hue min","Track Bar")
    h_max = cv2.getTrackbarPos("hue max","Track Bar")
    s_min = cv2.getTrackbarPos("saturation min","Track Bar")
    s_max = cv2.getTrackbarPos("saturation max","Track Bar")
    v_min = cv2.getTrackbarPos("value min","Track Bar")
    v_max = cv2.getTrackbarPos("value max","Track Bar")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(imgHSV,lower,upper)

    cv2.imshow("card",imgHSV)
    cv2.imshow("mask",mask)
    cv2.waitKey(1)