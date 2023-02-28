import cv2
import numpy as np

# Load the video file
cap = cv2.VideoCapture('circleVid.MOV')

# Define the parameters for circle detection
dp = 1
minDist = 1000000000
param1 = 50
param2 = 30
minRadius = 0
maxRadius = 0

while cap.isOpened():
    # Read each frame of the video file
    ret, frame = cap.read()
    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply circle detection using HoughCircles method
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

        # If circles are detected, draw them on the frame
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(frame, (x, y), r, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow("Circle Detection", frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and destroy any open windows
cap.release()
cv2.destroyAllWindows()
