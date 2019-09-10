# USAGE
# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg 

# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import serial


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/ingrid/unb/tcc2/git/TCC/shape_predictor_68_face_landmarks.dat")

# initialize webcam
captura = cv2.VideoCapture(0)

# initialize serial communication
ser = serial.Serial('/dev/ttyACM0', 9600)

 
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

		olhos = []
		olhos.append(shape[41][1]-shape[37][1]) # pontos 42 e 38 (y)
		olhos.append(shape[40][1]-shape[38][1]) # pontos 41 e 39 (y)
		olhos.append(shape[39][0]-shape[36][0]) # pontos 37 e 40 (x)
		olhos.append(shape[47][1]-shape[43][1]) # pontos 48 e 44 (y)
		olhos.append(shape[46][1]-shape[44][1]) # pontos 47 e 45 (y)
		olhos.append(shape[45][0]-shape[42][0]) # pontos 46 e 43 (x)
		#print(olhos)

		sobrancelha = []
		sobrancelha.append(shape[36][1]-shape[17][1]) #pontos 37 e 18 (y)
		sobrancelha.append(shape[37][1]-shape[18][1]) #pontos 38 e 19 (y)
		sobrancelha.append(shape[37][1]-shape[19][1]) #pontos 38 e 20 (y)
		sobrancelha.append(shape[38][1]-shape[20][1]) #pontos 39 e 21 (y)
		sobrancelha.append(shape[38][1]-shape[21][1]) #pontos 39 e 22 (y)
		sobrancelha.append(shape[45][1]-shape[26][1]) #pontos 46 e 27 (y)
		sobrancelha.append(shape[44][1]-shape[25][1]) #pontos 45 e 26 (y)
		sobrancelha.append(shape[44][1]-shape[24][1]) #pontos 45 e 25 (y)
		sobrancelha.append(shape[43][1]-shape[23][1]) #pontos 44 e 24 (y)
		sobrancelha.append(shape[43][1]-shape[22][1]) #pontos 44 e 23 (y)

		boca = []
		boca.append(shape[67][1]-shape[61][1]) #pontos 68 e 62 (y)
		boca.append(shape[66][1]-shape[62][1]) #pontos 67 e 63 (y)
		boca.append(shape[65][1]-shape[63][1]) #pontos 66 e 64 (y)
		boca.append(shape[48][0]-shape[3][0]) #pontos 49 e 4 (x)
		boca.append(shape[59][0]-shape[4][0]) #pontos 60 e 5 (x)
		boca.append(shape[49][0]-shape[2][0]) #pontos 50 e 3 (x)
		boca.append(shape[13][0]-shape[54][0]) #pontos 14 e 55 (x)
		boca.append(shape[12][0]-shape[55][0]) #pontos 13 e 56 (x)
		boca.append(shape[14][0]-shape[53][0]) #pontos 15 e 54 (x)

		rosto = []
		rosto.append(shape[0][1]-shape[16][1]) #pontos 1 e 17 (y)
		rosto.append(shape[1][1]-shape[15][1]) #pontos 2 e 16 (y)
		rosto.append(shape[2][1]-shape[14][1]) #pontos 3 e 15 (y)
		rosto.append(shape[3][1]-shape[13][1]) #pontos 4 e 14 (y)
		rosto.append(shape[4][1]-shape[12][1]) #pontos 5 e 13 (y)
		rosto.append(shape[5][1]-shape[11][1]) #pontos 6 e 12 (y)
		rosto.append(shape[6][1]-shape[10][1]) #pontos 7 e 11 (y)
		rosto.append(shape[7][1]-shape[9][1]) #pontos 8 e 10 (y)


		dif_y = shape[0][1]-shape[16][1] # linha(68) coluna(2) negativo: esquerda - positivo: direita
		dif_tot1 = shape[8][1]-shape[0][1] 
		dif_tot2 = shape[8][1]-shape[16][1]
		dif_med = (dif_tot1+dif_tot2)/2

		#rot_y = y/(x/dif_y); # para vetorizar
		#print(rot_y)
		rot2 = (dif_y*100)/dif_med
		print(rot2)
		#print("x", x)
		#print(rot_y)
		tam = len(shape)
		tam2 = len(shape[0])
		if (rot2 >= 40):
			print("Cabeca inclinada para direita")
			#ser.write('2');
		if (rot2 <= -40):
			print("Cabeca inclinada para esquerda")
			#ser.write('1')
		# show the face number
		#cv2.putText(frame, "Face #{}".format(i + 1), (x - 10, y - 10),
		#cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

		# loop over the (x, y)-coordinates for the facial landmarks
		# and draw them on the image
		for (x, y) in shape:
			cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
			#cv2.putText(frame, (x, y), 1, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			cv2.putText(frame, str(y), (x - 10, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			#print("x:", str(x))
			#print("y:", str(y))

		cv2.imshow('frame',frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
				break
 
captura.release()
cv2.destroyAllWindows()



