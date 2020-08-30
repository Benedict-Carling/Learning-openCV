import cv2

img = cv2.imread('Chapter1/resources/jacuzi.jpg')
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("output",imgGrey)
cv2.waitKey(0)