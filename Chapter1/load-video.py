import cv2

cap = cv2.VideoCapture('Chapter1/resources/skate.mp4')

while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    while cv2.waitKey(1) & 0xFF==ord('q'):
        break