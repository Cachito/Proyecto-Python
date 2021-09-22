from tkinter import *

root = Tk()

width = 425
height = 150

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))

root.minsize(width, height)
root.maxsize(width, height)

root.title("Proyecto")

lbl_titulo = Label(
    root, text="Ingrese datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60
)  # válido
lbl_titulo.grid(row=0, column=0, padx=1, pady=1, sticky=W + E, columnspan=4)

titulo_val = StringVar()
fecha_val = StringVar()
cuerpo_val = StringVar()

Label(root, text="Título").grid(row=2, column=0, sticky=W)
Label(root, text="Fecha").grid(row=4, column=0, sticky=W)
Label(root, text="Cuerpo").grid(row=6, column=0, sticky=W)

titulo = Entry(root, textvariable=titulo_val)
fecha = Entry(root, textvariable=fecha_val)
cuerpo = Entry(root, textvariable=cuerpo_val)

titulo.grid(row=2, column=1)
fecha.grid(row=4, column=1)
cuerpo.grid(row=6, column=1)

btn_save = Button(root, text="Guardar")
btn_save.grid(row=8, column=1, sticky=W + E)

btn_get = Button(root, text="Traer")
btn_get.grid(row=8, column=2, sticky=W + E)

mainloop()