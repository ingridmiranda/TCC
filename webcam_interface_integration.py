#importing modules required
# -*- coding: utf-8 -*-

from ttk import *
import Tkinter as tk
from Tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import os
import numpy as np
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
bocaAberta = 0
Piscada = 0
olhoDireitoAberto = 0




detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/home/ingrid/unb/tcc2/git/TCC/shape_predictor_68_face_landmarks.dat")

global last_frame                                      #creating global variable
last_frame = np.zeros((480, 640, 3), dtype=np.uint8)
global cap
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

## Boca Aberta True
def callbackBATrue():
    Label (root, image=photoGreen, bg="#d7f1ef") .grid(row=3, column=2, sticky=W+E+S+N) 
 
## Boca Aberta False
def callbackBAFalse():
    Label (root, image=photoRed, bg="#d7f1ef") .grid(row=3, column=2, sticky=W+E+S+N) 

## Boca Comprimida False
def callbackBCFalse():
    Label (root, image=photoRed, bg="#d7f1ef") .grid(row=4, column=2, sticky=W+E+S+N)

## Boca Comprimida True
def callbackBCTrue():
    Label (root, image=photoGreen, bg="#d7f1ef") .grid(row=4, column=2, sticky=W+E+S+N)
## Cabeça Inclinada para Esquerda False
def callbackCIEFalse():
    Label (root, image=photoRed, bg="#d7f1ef") .grid(row=5, column=2, sticky=W+E+S+N)

## Cabeça Inclinada para Esquerda True
def callbackCIETrue():
    Label (root, image=photoGreen, bg="#d7f1ef") .grid(row=5, column=2, sticky=W+E+S+N) 

## Cabeça Inclinada para Direita False
def callbackCIDFalse():
    Label (root, image=photoRed, bg="#d7f1ef") .grid(row=6, column=2, sticky=W+E+S+N)

## Cabeça Inclinada para Direita True
def callbackCIDTrue():
    Label (root, image=photoGreen, bg="#d7f1ef") .grid(row=6, column=2, sticky=W+E+S+N) 

## Piscada False      
def callbackPFalse():
    Label (root, image=photoRed, bg="#d7f1ef") .grid(row=7, column=2, sticky=W+E+S+N)

## Piscada True
def callbackPTrue():
    Label (root, image=photoGreen, bg="#d7f1ef") .grid(row=7, column=2, sticky=W+E+S+N) 

## Virar cadeira para direita
def callbackVD():
    Label (root, image=photoCadeiraDireita,  bg="white") .grid(row = 8, column = 0, sticky=W+E+S+N)

## Virar cadeira para Esquerda
def callbackVE():
    Label (root, image=photoCadeiraEsquerda, bg="white") .grid(row = 8, column = 0, sticky=W+E+S+N)

## Seguir com cadeira para frente
def callbackSF():
    Label (root, image=photoCadeiraFrente,  bg="white") .grid(row = 8, column = 0, sticky=W+E+S+N)

## Parar a cadeira
def callbackPC():
    Label (root, image=photoCadeiraStop,  bg="white") .grid(row = 8, column = 0, sticky=W+E+S+N)

def callbackST():
    Label (root, image=photoCadeiraTras,  bg="white") .grid(row = 8, column = 0, sticky=W+E+S+N)

def show_vid():                                        #creating a function
    global bocaAberta
    global Piscada
    global shape
    global olhoDireitoAberto
    global status

    if not cap.isOpened():                             #checks for the opening of camera
        print("cant open the camera")
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rects = detector(gray,1) 

    if ret is None:
        print "Major error!"
    elif ret:
        global last_frame
        last_frame = frame.copy()

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


		try:
			olhoEsquerdoAberto = aberturaOlhoEsquerdo[2]/(2*comprimentoOlhoEsquerdo[0])
			if (olhoEsquerdoAberto <= 0.2):
					print("Blink olho esquerdo")
					Piscada = True

			else: 
				Piscada = False

		except ZeroDivisionError:
			olhoEsquerdoAberto = 0

        if (Piscada == TRUE):
                callbackPTrue()
        if (Piscada == FALSE):
                callbackPFalse()


		#if olhoEsquerdoAberto < EYE_AR_THRESH:
		#		print("BLINK LEFT DETECTED")
        #        callbackPTrue()
        #else:
        #    callbackPFalse()
		
    #    if olhoDireitoAberto < EYE_AR_THRESH:
       #     print("BLINK RIGHT DETECTED")
        #    callbackPTrue()
        #else:
         #   callbackPFalse()
        
        
		
		#print("olhos", olhoDireitoAberto, olhoEsquerdoAberto)

		#print(olhos)

    #    sobrancelha = []
    #    sobrancelha.append(shape[36][1]-shape[17][1]) #pontos 37 e 18 (y)
    #    sobrancelha.append(shape[37][1]-shape[18][1]) #pontos 38 e 19 (y)
    #    sobrancelha.append(shape[37][1]-shape[19][1]) #pontos 38 e 20 (y)
    #    sobrancelha.append(shape[38][1]-shape[20][1]) #pontos 39 e 21 (y)
    #    sobrancelha.append(shape[38][1]-shape[21][1]) #pontos 39 e 22 (y)
    #    sobrancelha.append(shape[45][1]-shape[26][1]) #pontos 46 e 27 (y)
    #    sobrancelha.append(shape[44][1]-shape[25][1]) #pontos 45 e 26 (y)
    #    sobrancelha.append(shape[44][1]-shape[24][1]) #pontos 45 e 25 (y)
    #    sobrancelha.append(shape[43][1]-shape[23][1]) #pontos 44 e 24 (y)
    #    sobrancelha.append(shape[43][1]-shape[22][1]) #pontos 44 e 23 (y)

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
            
        BocaAberta = False
        BocaComprimida = False

        print(bocaAberta)

        if (bocaAberta < 6):
                print("Boca aberta!!")
                BocaAberta = True
                callbackBATrue()
                callbackBCFalse()


        if ((bocaAberta > 7) & (bocaAberta < 40)):
            BocaAberta = False
            callbackBAFalse()
            callbackBCFalse()

            
        if (bocaAberta > 40):
                BocaComprimida = True
                print("Boca comprimida!!")
                callbackBCTrue()
                callbackBAFalse;
               
        #else:
         #   BocaComprimida = False
          #  callbackBCFalse()
        
		
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
        
        if (rot2 <= -40):
            #print("Cabeca inclinada para direita")
                CabecaInclinadaDireita = True
                callbackCIDTrue()
                callbackCIEFalse()
                #ser.write('2');
        else:
                CabecaInclinadaDireita = False
                callbackCIDFalse()    

        if (rot2 >= 40):
            #print("Cabeca inclinada para esquerda")
                CabecaInclinadaEsquerda = True
                callbackCIETrue()
                callbackCIDFalse()
        else:
                CabecaInclinadaEsquerda = False
                callbackCIEFalse()
                
			#ser.write('1')
		# show the face number
		#cv2.putText(frame, "Face #{}".format(i + 1), (x - 10, y - 10),
		#cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


	#	if ((bocaAberta < 8) & (rot2 >= 40)):
	#		print("VIRAR PARA DIREITA")
	#	if ((bocaAberta < 8) & (rot2 <= -40)):
	#		print("VIRAR PARA ESQUERDA")
        status = "Nenhum comando detectado!"

        if (BocaAberta & CabecaInclinadaDireita):
                print("VIRAR PARA DIREITA!!")
                status = "Virar para direita"
                callbackVD()

        if (BocaAberta & CabecaInclinadaEsquerda):
                print("VIRAR PARA ESQUERDA!!")
                status = "Virar para esquerda"
                callbackVE()

        if (BocaComprimida & Piscada):
                print("SEGUIR EM FRENTE")
                status = "Seguir em frente"
                callbackSF()

        if (BocaAberta & Piscada):
                print("IR PARA TRÁS")
                status = "Ir para trás"
                callbackST()
        
        #else:
        #        print("PARAR CADEIRA")
        #        status = "Parar cadeira"
        #        callbackPC()
        

    pic = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)     #we can change the display color of the frame gray,black&white here
    img = Image.fromarray(pic)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, show_vid)

if __name__ == '__main__':
    root=tk.Tk()                            #assigning root variable for Tkinter as tk
    root.config(background = "#d7f1ef")
    lmain = tk.Label(master=root, bg="white")
    lmain.grid(row=8, column=1, rowspan=1, columnspan=2, sticky=W+E+N+S)
    root.title("Sistema de reconhecimento de expressões faciais")            #you can give any title

    ### Image Declarations ###
    photoGreen = PhotoImage(file="green.png")
    photoGreen = photoGreen.subsample(6,6)
    photoRed = PhotoImage(file="red.png")
    photoRed = photoRed.subsample(6,6)
    photoCadeiraDireita = PhotoImage(file="CadeiraDireita.png")
    photoCadeiraEsquerda = PhotoImage(file="CadeiraEsquerda.png")
    photoCadeiraFrente = PhotoImage(file="CadeiraFrente.png")
    photoCadeiraStop = PhotoImage(file="CadeiraStop.png")
    photoCadeiraTras = PhotoImage(file="CadeiraRe.png")
    photoCapa = PhotoImage(file="capaIG2.png")
    photoCapa = photoCapa.zoom(1,1)

    Label (root, image=photoCapa, bg="#d7f1ef").grid(row=0, column=0, columnspan = 3, sticky=W+E)

    Label (root, text="DESCRIÇÃO", bg="#d7f1ef", fg="black", font="helvetica 16 bold") .grid(row=2, column=0, columnspan=1, sticky=W)
    Label (root, text="Abrir amplamente a boca", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=3, column=0, columnspan=1, sticky=W)
    Label (root, text="Sugar os lábios", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=4, column=0, columnspan=1, sticky=W)
    Label (root, text="Piscar", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=7, column=0, columnspan=1, sticky=W)
    Label (root, text="Inclinar cabeça para esquerda", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=5, column=0, columnspan=1, sticky=W)
    Label (root, text="Inclinar cabeça para direita", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=6, column=0, columnspan=1, sticky=W)

    Label (root, text="AU", bg="#d7f1ef", fg="black", font="helvetica 16 bold") .grid(row=2, column=1, columnspan=1, sticky=W)
    Label (root, text="27", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=3, column=1, columnspan=1, sticky=W)
    Label (root, text="28", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=4, column=1, columnspan=1, sticky=W)
    Label (root, text="45", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=5, column=1, columnspan=1, sticky=W)
    Label (root, text="55", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=6, column=1, columnspan=1, sticky=W)
    Label (root, text="56", bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(row=7, column=1, columnspan=1, sticky=W)

    Label (root, text="STATUS", bg="#d7f1ef", fg="black", font="helvetica 16 bold") .grid(row=2, column=2, columnspan=1, sticky=W+E+S+N)
    

    Label (root, image=photoCadeiraStop, bg="white").grid(row=8, column=0, columnspan=1, sticky=W+E+N+S)

    while(TRUE):
        show_vid()

        root.update_idletasks()
        #root.mainloop()                                  #keeps the application in an infinite loop so it works continuosly

    Label (root, textvariable=status, bg="#d7f1ef", fg="black", font="helvetica 16 ") .grid(column=0, columnspan=3, sticky=W)
    Label (root, text="", bg="white", fg="black", font="helvetica 16 ") .grid(row=10, column=0, columnspan=3, sticky=W)


