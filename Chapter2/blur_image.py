import cv2

img = cv2.imread('Chapter1/resources/jacuzi.jpg')
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),0)
cv2.imshow("output",imgBlur)
cv2.waitKey(0)