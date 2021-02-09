import PyPDF2 as pdf
from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path
import pathlib 
from tkinter import filedialog

from tkinter import *
import string
import pandas as pd
import datetime
import tkinter as tk
from PIL import ImageTk, Image
import os

from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename

from datetime import datetime

def openFolder():
	 global folder_location
	 folder_location= tk.filedialog.askdirectory()

def exit():
    app.destroy()

"---------------------------------Application Interface-----------------------------------"

app=Tk()

app.title("PDFs")

B1=Button(app,text="Input Folder",width=40, height=4, command=openFolder, bg="LightSkyBlue2")
B1.pack(side='top')

B2=Button(app,text="Run and Save",width=40, height=4, command=exit, bg="Purple4", fg="white")
B2.pack(side='top')

app.mainloop()

a=0

for file in os.listdir(folder_location):
	infile = PdfFileReader(folder_location+"/"+file, 'rb')
	output = PdfFileWriter()
	a=a+1
	inform=infile.getDocumentInfo()
	title = inform.title

	for i in range(infile.getNumPages()):
	    p = infile.getPage(i)
	    if i > 0:
	        output.addPage(p)

	with open(folder_location + '/Updated' + str(a) + '.pdf', 'wb') as f:
	    output.write(f)
