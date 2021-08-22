from tkinter import *
from time import strftime
window = Tk()
icon = PhotoImage(file="icon.png")
window.iconphoto(True,icon)
window.title("CLOCK")
def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)
label = Label(font=("Arial",80))
label.pack(anchor="center")
time()

window.mainloop()