# USAGE
# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg 

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

# initialize webcam

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/ingrid/unb/tcc2/git/TCC/shape_predictor_68_face_landmarks.dat")


captura = cv2.VideoCapture(0)
 
while(captura.isOpened()):
	ret, frame = captura.read()
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
	rects = detector(gray,1)
	
	for (i, rect) in enumerate(rects):
# determine the facial landmarks for the face region, then
# convert the facial landmark (x, y)-coordinates to a NumPy
# array
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

# convert dlib's rectangle to a OpenCV-style bounding box
# [i.e., (x, y, w, h)], then draw the face bounding box
		(x, y, w, h) = face_utils.rect_to_bb(rect)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

		# show the face number
		cv2.putText(frame, "Face #{}".format(i + 1), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

		# loop over the (x, y)-coordinates for the facial landmarks
		# and draw them on the image
		for (x, y) in shape:
			cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

		cv2.imshow('frame',frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
				break
 
captura.release()
cv2.destroyAllWindows()


