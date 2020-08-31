import cv2
import numpy as np

width, height = 250, 350
img = cv2.imread('Chapter5/resources/card.jpg')
img2 = cv2.imread('Chapter5/resources/jacuzi.jpg')
img3 = cv2.imread('Chapter5/resources/bird.jpg')

imgSmall = cv2.resize(img2,(500,300))

imgHoriz = np.hstack((imgSmall,imgSmall))
imgVert = np.vstack((imgHoriz,imgHoriz))

cv2.imshow("card",imgVert)
cv2.waitKey(0)