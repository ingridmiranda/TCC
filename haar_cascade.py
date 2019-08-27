from  __future__ import print_function
import numpy as np
import cv2
 
captura = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/home/ingrid/unb/tcc2/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

while(captura.isOpened()):
    ret, frame = captura.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE,minSize=(50, 50), maxSize=None)
  
    if len(faces) > 0:
        print("Pessoa detectada!")
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x - 10, y - 20), (x + w + 10, y + h + 10), (0, 255, 0), 2)
            #roi_gray = frame[y-15:y + h+10, x-10:x + w+10]
 
        cv2.imshow("Metodo haar cascade", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
captura.release()
cv2.destroyAllWindows()
