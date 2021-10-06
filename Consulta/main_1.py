import sys
from tkinter import *

sys.path.append("../Proyecto-Python/modulos")

from modulo import *

root = Tk()

width = 425
height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

#root.geometry("%dx%d+%d+%d" % (width, height, x, y))

#root.minsize(width, height)
#root.maxsize(width, height)

root.title("Proyecto")

root.iconbitmap("./imagenes/noticias.ico")

lbl_titulo = Label(text="Título")
val_titulo = Entry()

lbl_titulo.pack()
val_titulo.pack()

root.mainloop()