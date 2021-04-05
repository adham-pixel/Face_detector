import numpy as np
import cv2
cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0), 5)
        roi_gray= gray[x:x+w, y:y+w]
        roi_color =frame[y:y+h, x:x+w]

        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        
    cv2.imshow('b.salas', frame)

    if cv2.waitKey(1) == ord('z'):
        break    



cap.release()
cv2.destroyAllWindows() 