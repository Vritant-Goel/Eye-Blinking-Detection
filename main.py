import cv2
import numpy as np

# init camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        continue
#below code converts all the colors to gray as to make the roi(region of interest) pop. so we can later on work upon roi
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Frame", frame)
    cv2.imshow("gray frame", gray_frame)





    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
