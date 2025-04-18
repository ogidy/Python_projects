from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p") #%H makes it call 24hr time whiles %I call 12hr time
    label.config(text=string)
    label.after(1000,time) #call time function after every 1000 millisecond
label = Label(root, font=("ds-digital", 50), background='black', foreground="gold")
label.pack(anchor="center")
time()

mainloop()