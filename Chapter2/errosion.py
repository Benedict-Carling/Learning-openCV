import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

img = cv2.imread('Chapter1/resources/jacuzi.jpg')
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img,240,250)
imgErrosion = cv2.erode(imgCanny,kernel,iterations=1)
cv2.imshow("output",imgErrosion)
cv2.waitKey(0)