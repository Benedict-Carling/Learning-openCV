import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),1)
cv2.rectangle(img, (0,0),(250,300),(255,0,0))
cv2.circle(img,(300,250),50,(0,0,255))
print(img.shape)
cv2.putText(img,"Open CV",(10,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)

#cv2.imshow("output",imgGrey)
cv2.imshow("Line",img)
cv2.waitKey(0)