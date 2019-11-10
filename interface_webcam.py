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


status1 = 0
status2 = 1
status3 = 1
status4 = 0
status5 = 0

global last_frame                                      #creating global variable
last_frame = np.zeros((480, 640, 3), dtype=np.uint8)
global cap
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def show_vid():                                        #creating a function
    if not cap.isOpened():                             #checks for the opening of camera
        print("cant open the camera")
    flag, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if flag is None:
        print "Major error!"
    elif flag:
        global last_frame
        last_frame = frame.copy()

    pic = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)     #we can change the display color of the frame gray,black&white here
    img = Image.fromarray(pic)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_vid)

if __name__ == '__main__':
    root=tk.Tk()                             #assigning root variable for Tkinter as tk
    root.config(background = "#FFFFFF")
    lmain = tk.Label(master=root)
    lmain.grid(row=9, column=0, columnspan=3, sticky=W+E+N+S)
    root.title("Sistema de reconhecimento de expressões faciais")            #you can give any title
    photoCapa = PhotoImage(file="capa.png")
    photoCapa = photoCapa.zoom(2,1)
    Label (root, image=photoCapa, bg="white").grid(row=0, column=0, columnspan=3, sticky=W+E+N+S)

    Label (root, text=" ", bg="white", fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W+E)

    Label (root, text="Descrição", bg="white", fg="black", font="none 12 bold") .grid(row=2, column=0, sticky=W)
    Label (root, text="Abrir amplamente a boca", bg="white", fg="black", font="none 12 ") .grid(row=3, column=0, sticky=W)
    Label (root, text="Sugar os lábios", bg="white", fg="black", font="none 12 ") .grid(row=4, column=0, sticky=W)
    Label (root, text="Piscar", bg="white", fg="black", font="none 12 ") .grid(row=7, column=0, sticky=W)
    Label (root, text="Inclinar cabeça para esquerda", bg="white", fg="black", font="none 12 ") .grid(row=5, column=0, sticky=W)
    Label (root, text="Inclinar cabeça para direita", bg="white", fg="black", font="none 12 ") .grid(row=6, column=0, sticky=W)

    Label (root, text="AU", bg="white", fg="black", font="none 12 bold") .grid(row=2, column=1, sticky=W)
    Label (root, text="27", bg="white", fg="black", font="none 12 ") .grid(row=3, column=1, sticky=W)
    Label (root, text="28", bg="white", fg="black", font="none 12 ") .grid(row=4, column=1, sticky=W)
    Label (root, text="45", bg="white", fg="black", font="none 12 ") .grid(row=5, column=1, sticky=W)
    Label (root, text="55", bg="white", fg="black", font="none 12 ") .grid(row=6, column=1, sticky=W)
    Label (root, text="56", bg="white", fg="black", font="none 12 ") .grid(row=7, column=1, sticky=W)


    photoGreen = PhotoImage(file="green.png")
    photoGreen = photoGreen.subsample(8,8)
    photoRed = PhotoImage(file="red.png")
    photoRed = photoRed.subsample(8,8)
    Label (root, text="Status", bg="white", fg="black", font="none 12 bold") .grid(row=2, column=2, sticky=W+E+S+N)
    if (status1 == 0):
        Label (root, image=photoRed, bg="white") .grid(row=3, column=2, sticky=W+E+S+N)
    else:
        Label (root, image=photoGreen, bg="white") .grid(row=3, column=2, sticky=W+E+S+N) 

    if (status2 == 0):
        Label (root, image=photoRed, bg="white") .grid(row=4, column=2, sticky=W+E+S+N)
    else:
        Label (root, image=photoGreen, bg="white") .grid(row=4, column=2, sticky=W+E+S+N) 

    if (status3 == 0):
        Label (root, image=photoRed, bg="white") .grid(row=5, column=2, sticky=W+E+S+N)
    else:
        Label (root, image=photoGreen, bg="white") .grid(row=5, column=2, sticky=W+E+S+N) 
    if (status4 == 0):
        Label (root, image=photoRed, bg="white") .grid(row=6, column=2, sticky=W+E+S+N)
    else:
        Label (root, image=photoGreen, bg="white") .grid(row=6, column=2, sticky=W+E+S+N) 
    if (status5 == 0):
        Label (root, image=photoRed, bg="white") .grid(row=7, column=2, sticky=W+E+S+N)
    else:
        Label (root, image=photoGreen, bg="white") .grid(row=7, column=2, sticky=W+E+S+N) 

    Label (root, text="  ", bg="white", fg="black", font="none 12 ") .grid(row=8, column=0, columnspan=3, sticky=W)

    show_vid()

    root.mainloop()                                  #keeps the application in an infinite loop so it works continuosly