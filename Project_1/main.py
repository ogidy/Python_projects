from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

label = Label(root, font=("ds-digital", 90), background='black', foreground="gold")
label.pack(anchor="center")