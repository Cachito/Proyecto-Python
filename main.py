from modulos.modulo import *
from tkinter import *
from tkinter.messagebox import *

root = Tk()

root.title("Carga de Noticias")
root.iconbitmap("./imagenes/noticias.ico")
root.resizable(False, False)

width = 425
height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

set_frames(root)
set_menu(root)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))

root.mainloop()
