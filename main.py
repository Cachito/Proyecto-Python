from modulos.modulo import *
from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Menú Principal")

menubar = Menu(root)

# Elemento desplegable “Archivo”
menuArchivo = Menu(menubar, tearoff=0)
menuArchivo.add_command(label="Medios", command = lambda: abm_medios(root))
menuArchivo.add_command(label="Divisiones", command=abm_divisiones)
menuArchivo.add_command(label="Noticias", command=cargador)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=menuArchivo)

# Elemento desplegable “Ayuda”
menuAyuda = Menu(menubar, tearoff=0)
menuAyuda.add_command(label="Acerca de..", command=about)
menubar.add_cascade(label="Ayuda", menu=menuAyuda)

# Mostrar menú
root.config(menu=menubar)

root.mainloop()
