import cv2

img = cv2.imread('Chapter1/resources/jacuzi.jpg')
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img,240,250)
cv2.imshow("output",imgCanny)
cv2.waitKey(0)