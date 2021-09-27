import tkinter
from tkinter import *
from tkinter.messagebox import *

def save_medio(nombre):
    print(f"Guardando medio {nombre}")

def cancel_medio():
        print("Cancelando")

def about():
    showinfo("Entrega Intermedia", "Cargador de Noticias\n\nGrupo:\n- Luis Carro\n- Cristian Maier")

def abm_medios(root):
    medios_window = tkinter.Toplevel(root)
    medios_window.title("ABM de Medios")

    nombre_val = StringVar()
    Label(medios_window, text="Nombre").grid(row=2, column=0, sticky=W)
    nombre = Entry(medios_window, textvariable=nombre_val)
    nombre.grid(row=2, column=1)

    btn_save = Button(medios_window, text="Guardar", command = save_medio(nombre_val.get()))
    btn_save.grid(row=8, column=1)

    btn_cancel = Button(medios_window, text="Cancelar", command = cancel_medio())
    btn_cancel.grid(row=8, column=2)

    medios_window.mainloop()

def abm_divisiones():
    showinfo("Entrega Intermedia", "ABM de Divisiones")

def cargador():
    showinfo("Entrega Intermedia", "Carga de Noticias")

def hola():
    print("Hola!")    