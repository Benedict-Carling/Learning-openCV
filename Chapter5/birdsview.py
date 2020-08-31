import cv2
import numpy as np

width, height = 250, 350
img = cv2.imread('Chapter5/resources/card.jpg')

points1 = np.float32([[387,177],[568,143],[465,399],[672,378]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(points1,points2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("card",img)
cv2.imshow("orientedcard",imgOutput)
cv2.waitKey(0)