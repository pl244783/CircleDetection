import cv2
import numpy as np

cap = cv2.VideoCapture('path/to/video')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 2)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('
