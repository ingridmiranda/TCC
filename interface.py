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

root=tk.Tk()                             #assigning root variable for Tkinter as tk
root.config(background = "#FFFFFF")
lmain = tk.Label(master=root)
root.title("Sistema de reconhecimento de expressões faciais")            #you can give any title
photoCapa = PhotoImage(file="capa.png")
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


root.mainloop()                                  #keeps the application in an infinite loop so it works continuosly