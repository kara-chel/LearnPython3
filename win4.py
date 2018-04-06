#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import *
from tkinter import *

f = input('f(x):')

root = Tk()

canv = Canvas(root, width = 1000, height = 1000, bg = "lightblue", cursor = "pencil")
canv.create_line(500,1000,500,0,width=2,arrow=LAST) 
canv.create_line(0,500,1000,500,width=2,arrow=LAST) 

canv.pack()
root.mainloop()

