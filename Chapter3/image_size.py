import cv2

img = cv2.imread('Chapter1/resources/jacuzi.jpg')
imgResize = cv2.resize(img,(400,300))

print(img.shape)

#cv2.imshow("output",imgGrey)
cv2.imshow("resize",imgResize)
cv2.waitKey(0)