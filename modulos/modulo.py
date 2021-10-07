import tkinter
from tkinter import *
from tkinter.messagebox import *

def set_frames(root):
    frame_data = Frame(master=root, width=400, height=270, borderwidth=1, relief=SOLID)
    frame_data.pack()

    lbl_fecha=Label(master=frame_data, text="Fecha", width=50, anchor=W)
    lbl_fecha.place(x=5, y=5)
    ent_fecha=Entry(master=frame_data).place(x=60, y=5)
    ent_fecha.place(x=60, y=5)
    lbl_fecha.pack()
    ent_fecha.pack()

    lbl_medio=Label(master=frame_data, text="Medio", width=50, anchor=W)
    lbl_medio.place(x=5, y=35)
    ent_medio=Entry(master=frame_data, width=50).place(x=60, y=35)
    lbl_medio.pack()
    ent_medio.pack()

    lbl_seccion=Label(master=frame_data, text="Sección", width=50, anchor=W)
    lbl_seccion.place(x=5, y=65)
    ent_seccion=Entry(master=frame_data, width=50).place(x=60, y=65)
    lbl_seccion.pack()
    ent_seccion.pack()

    lbl_titulo=Label(master=frame_data, text="Título", width=50, anchor=W)
    lbl_titulo.place(x=5, y=95)
    ent_titulo=Entry(master=frame_data, width=50).place(x=60, y=95)
    lbl_titulo.pack()
    ent_titulo.pack()

    lbl_cuerpo=Label(master=frame_data, text="Cuerpo", width=50, anchor=W)
    lbl_cuerpo.place(x=5, y=125)
    txt_cuerpo=Text(master=frame_data, width=40, height=4).place(x=60, y=125)
    lbl_cuerpo.pack()
    txt_cuerpo.pack()

    lbl_imagen=Label(master=frame_data, text="Imagen", width=50, anchor=W)
    lbl_imagen.place(x=5, y=205)
    ent_imagen=Entry(master=frame_data, width=50).place(x=60, y=205)
    lbl_imagen.pack()
    ent_imagen.pack()

    frame_list = Frame(master=root, width=400, height=150, bg="yellow")
    frame_list.pack()

    frame_control = Frame(master=root, width=400, height=50, bg="blue")
    frame_control.pack()

    btn_save = Button(master=frame_control, text="Set Data", command = lambda: save_data(ent_fecha.get(), ent_medio.get(), ent_seccion.get(), ent_titulo.get(), txt_cuerpo.get(), ent_imagen.get()))
    btn_save.place(x=15, y=5)

    btn_get = Button(master=frame_control, text="Get Data", command = lambda: get_data())
    btn_get.place(x=100, y=5)

def set_menu(root):
    menubar = Menu(root)

    # Elemento desplegable “Archivo”
    menuArchivo = Menu(menubar, tearoff=0)
    menuArchivo.add_separator()
    menuArchivo.add_command(label="Acerca de..", command=about)
    menuArchivo.add_command(label="Salir", command=root.quit)
    menubar.add_cascade(label="Archivo", menu=menuArchivo)

    # Mostrar menú
    root.config(menu=menubar)

def save_data(fecha, medio, seccion, titulo, cuerpo, imagen):
    print(f"Guardando fecha {fecha}, medio {medio}, seccion {seccion}, titulo {titulo}, cuerpo {cuerpo}, imagen {imagen}")

def get_data():
        print("geteando")

def about():
    showinfo("Entrega Intermedia", "Cargador de Noticias\n\nGrupo:\n- Luis Carro\n- Cristian Maier")

def hola():
    print("Hola!")