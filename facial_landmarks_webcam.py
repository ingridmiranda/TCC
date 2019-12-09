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
import math
import Tkinter as Tk

BocaAberta = False
BocaComprimida = False
Piscada = False
CabecaInclinadaEsquerda = False
CabecaInclinadaDireita = False
EYE_AR_THRESH = 0.2
EYE_AR_CONSEC_FRAMES = 3
COUNTER = 0
TOTAL = 0


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
		#abertura do olho direito
		olhos.append(shape[41][1]-shape[37][1]) # pontos 42 e 38 (y)
		olhos.append(shape[41][0]-shape[37][0]) # pontos 42 e 38 (x)
		olhos.append(shape[40][1]-shape[38][1]) # pontos 41 e 39 (y)
		olhos.append(shape[40][0]-shape[38][0]) # pontos 41 e 39 (x)

		#comprimento do olho direito
		olhos.append(shape[39][0]-shape[36][0]) # pontos 37 e 40 (x)
		olhos.append(shape[39][1]-shape[36][1]) # pontos 37 e 40 (y)

		#abertura do olho esquerdo
		olhos.append(shape[47][1]-shape[43][1]) # pontos 48 e 44 (y)
		olhos.append(shape[47][0]-shape[43][0]) # pontos 48 e 44 (x)
		olhos.append(shape[46][1]-shape[44][1]) # pontos 47 e 45 (y)
		olhos.append(shape[46][0]-shape[44][0]) # pontos 47 e 45 (x)

		#comprimento do olho esquerdo
		olhos.append(shape[45][0]-shape[42][0]) # pontos 46 e 43 (x)
		olhos.append(shape[45][1]-shape[42][1]) # pontos 46 e 43 (x)

		aberturaOlhoDireito = []
		aberturaOlhoDireito.append(math.sqrt((olhos[0] ** 2) + (olhos[1] ** 2)))
		aberturaOlhoDireito.append(math.sqrt((olhos[2] ** 2) + (olhos[3] ** 2)))
		aberturaOlhoDireito.append((aberturaOlhoDireito[0] + aberturaOlhoDireito[1]))

		comprimentoOlhoDireito = []
		comprimentoOlhoDireito.append(math.sqrt((olhos[4] ** 2) + (olhos[5] ** 2)))


		try:
			olhoDireitoAberto = aberturaOlhoDireito[2]/(2*comprimentoOlhoDireito[0])
			if (olhoDireitoAberto <= 0.2):
				print("Blink olho direito")
				Piscada = True
			else:
					Piscada = False


		except ZeroDivisionError:
			olhoDireitoAberto = 0

		aberturaOlhoEsquerdo = []
		aberturaOlhoEsquerdo.append(math.sqrt((olhos[6] ** 2) + (olhos[7] ** 2)))
		aberturaOlhoEsquerdo.append(math.sqrt((olhos[8] ** 2) + (olhos[9] ** 2)))
		aberturaOlhoEsquerdo.append((aberturaOlhoEsquerdo[0] + aberturaOlhoEsquerdo[1]))

		comprimentoOlhoEsquerdo = []
		comprimentoOlhoEsquerdo.append(math.sqrt((olhos[10] ** 2) + (olhos[11] ** 2)))

		counterLeft = 0

		try:
			olhoEsquerdoAberto = aberturaOlhoEsquerdo[2]/(2*comprimentoOlhoEsquerdo[0])
			if (olhoEsquerdoAberto <= 0.2):
					print("Blink olho esquerdo")
					Piscada = True
			else: 
				Piscada = False

		except ZeroDivisionError:
			olhoEsquerdoAberto = 0

		
		#print("olhos", olhoDireitoAberto, olhoEsquerdoAberto)

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
		# nivel de abertura de boca
		boca.append(shape[67][1]-shape[61][1]) #pontos 68 e 62 (y)
		boca.append(shape[67][0]-shape[61][0]) #pontos 68 e 62 (x)
		boca.append(shape[66][1]-shape[62][1]) #pontos 67 e 63 (y)
		boca.append(shape[66][0]-shape[62][0]) #pontos 67 e 63 (x)
		boca.append(shape[65][1]-shape[63][1]) #pontos 66 e 64 (y)
		boca.append(shape[65][0]-shape[63][0]) #pontos 66 e 64 (x)

		#comprimento da boca
		boca.append(shape[54][0]-shape[48][0]) #pontos 55 e 49 (x)
		boca.append(shape[54][0]-shape[48][0]) #pontos 55 e 49 (x)

		# torcao da boca
		boca.append(shape[48][0]-shape[3][0]) #pontos 49 e 4 (x)
		boca.append(shape[59][0]-shape[4][0]) #pontos 60 e 5 (x)
		boca.append(shape[49][0]-shape[2][0]) #pontos 50 e 3 (x)
		boca.append(shape[13][0]-shape[54][0]) #pontos 14 e 55 (x)
		boca.append(shape[12][0]-shape[55][0]) #pontos 13 e 56 (x)
		boca.append(shape[14][0]-shape[53][0]) #pontos 15 e 54 (x)
		#aberturaBoca = ((boca[0] ** 2) + (boca[1] ** 2) + (boca[3] ** 2) ** (1/2)) #implementando distancias euclidianas
		#boca1 = aberturaBoca/boca[3]
		#print("boca:", aberturaBoca, boca[3], boca1)
		#if (boca1 > 10):
		#	print("Boca aberta")
		
		aberturaBoca = []
		aberturaBoca.append(math.sqrt((boca[0] ** 2) + (boca[1] ** 2)))
		aberturaBoca.append(math.sqrt((boca[2] ** 2) + (boca[3] ** 2)))
		aberturaBoca.append(math.sqrt((boca[4] ** 2) + (boca[5] ** 2)))
		aberturaBoca.append((aberturaBoca[0] + aberturaBoca[1] + aberturaBoca[2])/3)

		comprimentoBoca = []
		comprimentoBoca.append(math.sqrt((boca[6] ** 2) + (boca[7] ** 2)))

		try:
			bocaAberta = comprimentoBoca[0]/aberturaBoca[3]
		except ZeroDivisionError:
			bocaAberta = 0

		if (bocaAberta < 6):
				print("Boca aberta!!")
				BocaAberta = True
				BocaComprimida = False
		#else:
		#		BocaAberta = False

		if ((bocaAberta > 6) & (bocaAberta < 40)):
    			BocaAberta = False

		if (bocaAberta > 40):
				BocaComprimida = True
				BocaAberta = False
				print("Boca comprimida!!")
		#else:
		#		BocaComprimida = False
		


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
		try:
			rot2 = (dif_y*100)/dif_med
		except ZeroDivisionError:
			rot2 = 0

		#print(rot2)
		#print("x", x)
		#print(rot_y)
		tam = len(shape)
		tam2 = len(shape[0])
		if (rot2 >= 40):
			#print("Cabeca inclinada para direita")
			CabecaInclinadaDireita = True
			#ser.write('2');
		else:
				CabecaInclinadaDireita = False
		if (rot2 <= -40):
			#print("Cabeca inclinada para esquerda")
			CabecaInclinadaEsquerda = True
		else:
				CabecaInclinadaEsquerda = False
			#ser.write('1')
		# show the face number
		#cv2.putText(frame, "Face #{}".format(i + 1), (x - 10, y - 10),
		#cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


	#	if ((bocaAberta < 8) & (rot2 >= 40)):
	#		print("VIRAR PARA DIREITA")
	#	if ((bocaAberta < 8) & (rot2 <= -40)):
	#		print("VIRAR PARA ESQUERDA")

		if (BocaAberta & CabecaInclinadaDireita):
				print("VIRAR PARA DIREITA!!")
				ser.write('1')
		
		else:
			if (BocaAberta & CabecaInclinadaEsquerda):
					print("VIRAR PARA ESQUERDA!!")
					ser.write('2')
			else:
				if (BocaComprimida & Piscada):
						print("SEGUIR EM FRENTE")
						ser.write('3')
				else:
					if (BocaAberta & Piscada):
							print("IR PARA TRAS")
							ser.write('4')
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

