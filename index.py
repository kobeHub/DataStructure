#!/usr/bin/python3
"""
Pillow >= 2.1.0 no longer supports “import _imaging”. Please use 
“from PIL.Image import core as _imaging” instead.


Pillow >= 1.0 no longer supports “import Image”. 
Please use “from PIL import Image” instead.


ｐｉｌｌｏw版本：５．０．０　支持ｐｙｔｈｏｎ　　２．７　　３．４　３．５　３．６
python3 -V = 3.6.4
"""
import tkinter as tk
from PIL import Image, ImageTk
import os

def create_window():
	top.destroy()
	os.system('python3 console.py')
	

top = tk.Tk()
top.title('1D Bin-packing System')
top.geometry('1020x800')

im = Image.open('source/index1.jpg')
# im.show()
#title = tk.Label(top, text='The Bin-packing System', font='’Helvetica -24 bold')
#title.pack()
im_jpg = ImageTk.PhotoImage(im)
im_label = tk.Label(top, image=im_jpg)
b = tk.Button(top, text='Welcome to the System!', command=create_window)
im_label.pack() 
b.pack()

top.mainloop()
