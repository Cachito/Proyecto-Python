#from modulos.modulo import *
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

class Noticias:
    def __init__(self, parent=None, **configs):
        # Defino parámetros
        ancho_boton = 10

        # Defino variables por defecto
        self.fecha = StringVar()
        self.medio = StringVar()
        self.seccion = StringVar()
        self.titulo = StringVar()
        self.cuerpo = StringVar()
        self.archivo = StringVar()

        # Ventana principal
        self.my_parent = parent
        self.my_parent.geometry("800x600")
        self.my_parent.title("Carga de Noticias")
        self.my_parent.iconbitmap("./imagenes/noticias.ico")

        # Contenedor
        self.frm_contenedor = Frame(self.my_parent, borderwidth=1)

        # controles: guardar
        self.frm_controles = Frame(master=self.frm_contenedor, height=40, borderwidth=1, relief=RAISED)

        self.img_db = PhotoImage(file = r"./imagenes/iconDb.png")
        self.btn_db = Button(master=self.frm_controles, text="Base de Detos", image=self.img_db, width=30, command=lambda: create_data())
        self.btn_db.place(x=15, y=2)

        self.img_table = PhotoImage(file = r"./imagenes/iconTable.png")
        self.btn_table = Button(master=self.frm_controles, text="Tabla", image=self.img_table, width=30, command=lambda: create_table())
        self.btn_table.place(x=50, y=2)

        self.img_nuevo = PhotoImage(file = r"./imagenes/iconNew.png")
        self.btn_nuevo = Button(master=self.frm_controles, text="Nuevo", image=self.img_nuevo, width=30, command=lambda: clear_data(self))
        self.btn_nuevo.place(x=85, y=2)

        self.img_guardar = PhotoImage(file = r"./imagenes/iconSave.png")
        self.btn_guardar = Button(master=self.frm_controles, text="Guardar", image=self.img_guardar, width=30, command=lambda: save_data(self.ent_fecha.get()))
        self.btn_guardar.place(x=120, y=2)

        self.img_buscar = PhotoImage(file = r"./imagenes/iconSearch.png")
        self.btn_buscar = Button(master=self.frm_controles, text="Buscar", image=self.img_buscar, width=30, command=lambda: buscar())
        self.btn_buscar.place(x=155, y=2)

        self.frm_controles.pack(side=TOP, expand=NO, fill=X) #place(x=5,y=400)

        self.frm_datos = Frame(master=self.frm_contenedor, height=300, borderwidth=1, relief=SOLID)

        self.lbl_fecha=Label(master=self.frm_datos, text="Fecha", width=50, anchor=W)
        self.lbl_fecha.place(x=5, y=5)
        #self.lbl_fecha.pack()

        self.ent_fecha=Entry(master=self.frm_datos, textvariable=self.fecha, width=50)
        self.ent_fecha.place(x=60, y=5)
        #self.ent_fecha.pack()

        self.frm_datos.pack(side=TOP, expand=NO, fill=X) #place(x=5,y=400)

        self.frm_contenedor.pack(expand=YES, fill=BOTH)

        self.menu_bar = Menu(root)
        self.menu_archivo = Menu(self.menu_bar, tearoff=0)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Acerca de..", command=about)
        self.menu_archivo.add_command(label="Salir", command=root.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.menu_archivo)
        
        root.config(menu=self.menu_bar)

def save_data(fecha):
    print(f"Guardando fecha {fecha}")

def create_data():
    print(f"Creando Base de Datos")    

def create_table():
    print(f"Creando Tabla")        

def clear_data(self):
    self.fecha = ""

def buscar():
    print(f"buscando")        

def about():
    showinfo("Entrega Intermedia", "Cargador de Noticias\n\nGrupo:\n- Luis Carro\n- Cristian Maier")

if __name__ == "__main__":
    root = Tk()
    Noticias(root)
    root.mainloop()
