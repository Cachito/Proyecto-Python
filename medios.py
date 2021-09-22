from modulos.modulo import *
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

width = 450
height = 300

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

window.geometry("%dx%d+%d+%d" % (width, height, x, y))

#window.minsize(width, height)
#window.maxsize(width, height)

window.title("Noticias")

lbl_title = Label(
    window, text="Carga de Noticias", 
    bg="DarkOrchid3", 
    fg="thistle1", 
    height=1,
    width=60
)  # válido
lbl_title.grid(row=0, column=0, padx=1, pady=1, sticky=W + E, columnspan=4)


Label(window, text="Medio").grid(row=2, column=0, sticky=W)
data_medio=("Diario", "Revista", "Web", "Radio")
cb_medio=Combobox(window, values=data_medio)
cb_medio.grid(row=2, column=1)

Label(window, text="División").grid(row=3, column=0, sticky=W)
data_div=("Política", "Deportes", "Actualidad")
cb_div=Combobox(window, values=data_div)
cb_div.grid(row=3, column=1)


fecha_val = StringVar()
Label(window, text="Fecha").grid(row=4, column=0, sticky=W)
fecha = Entry(window, textvariable=fecha_val)
fecha.grid(row=4, column=1)

titulo_val = StringVar()
Label(window, text="Título").grid(row=5, column=0, sticky=W)
titulo = Entry(window, textvariable=titulo_val)
titulo.grid(row=5, column=1)

cuerpo_val = StringVar()
Label(window, text="Cuerpo").grid(row=6, column=0, sticky=W)
cuerpo = Entry(window, textvariable=cuerpo_val)
cuerpo.grid(row=6, column=1)

autor_val = StringVar()
Label(window, text="Autor").grid(row=7, column=0, sticky=W)
autor = Entry(window, textvariable=autor_val)
autor.grid(row=6, column=1)

archivo_val = StringVar()
Label(window, text="Archivo").grid(row=7, column=0, sticky=W)
archivo = Entry(window, textvariable=archivo_val)
archivo.grid(row=7, column=1)

btn_nuevo = Button(window, text="Nuevo", command=save_data)
btn_nuevo.grid(row=9, column=0, sticky=W + E)

btn_save = Button(window, text="Guardar", command=save_data)
btn_save.grid(row=9, column=1, sticky=W + E)

btn_get = Button(window, text="Cancelar", command=get_data)
btn_get.grid(row=9, column=2, sticky=W + E)


mainloop()