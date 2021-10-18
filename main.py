
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from modulos.modulo import *

class Noticias:
    def __init__(self, parent=None, **configs):
        # Defino variables por defecto
        self.id = StringVar()
        self.fecha = StringVar()
        self.medio = StringVar()
        self.seccion = StringVar()
        self.titulo = StringVar()
        self.cuerpo = StringVar()
        #self.archivo = StringVar()
        self.busqueda = StringVar()

        # Ventana principal
        self.my_parent = parent
        self.my_parent.geometry("500x600")
        self.my_parent.title("Carga de Noticias")
        self.my_parent.iconbitmap("./imagenes/noticias.ico")

        # Contenedor
        self.frm_contenedor = Frame(self.my_parent, height=600, borderwidth=1)

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
        self.btn_guardar = Button(master=self.frm_controles, text="Guardar", image=self.img_guardar, width=30, command=lambda: save_data(self.id, self.ent_fecha.get(), self.ent_medio.get(), self.ent_seccion.get(), self.ent_titulo.get(), self.ent_cuerpo.get("1.0", END), self))
        self.btn_guardar.place(x=120, y=2)

        self.img_borrar = PhotoImage(file = r"./imagenes/iconDelete.png")
        self.btn_borrar = Button(master=self.frm_controles, text="Eliminar", image=self.img_borrar, width=30, command=lambda: delete_data(self))
        self.btn_borrar.place(x=155, y=2)

        self.img_refresh = PhotoImage(file = r"./imagenes/iconRefresh.png")
        self.btn_refresh = Button(master=self.frm_controles, text="Actualizar", image=self.img_refresh, width=30, command=lambda: refresh(self))
        self.btn_refresh.place(x=190, y=2)

        self.ent_busqueda = Entry(master=self.frm_controles, textvariable=self.busqueda, width=3)
        self.ent_busqueda.place(x=235, y=7)

        self.img_buscar = PhotoImage(file = r"./imagenes/iconSearch.png")
        self.btn_buscar = Button(master=self.frm_controles, text="Buscar", image=self.img_buscar, width=30, command=lambda: buscar(self.ent_busqueda.get(), self))
        self.btn_buscar.place(x=260, y=2)

        self.frm_controles.pack(side=TOP, expand=NO, fill=X) #place(x=5,y=400)

        self.frm_datos = Frame(master=self.frm_contenedor, height=300, borderwidth=1, relief=SOLID)

        self.lbl_fecha=Label(master=self.frm_datos, text="Fecha", width=50, anchor=W)
        self.lbl_fecha.place(x=5, y=5)
        self.ent_fecha=Entry(master=self.frm_datos, textvariable=self.fecha, width=50)
        self.ent_fecha.place(x=60, y=5)

        self.lbl_medio=Label(master=self.frm_datos, text="Medio", width=50, anchor=W)
        self.lbl_medio.place(x=5, y=35)
        self.ent_medio=Entry(master=self.frm_datos, textvariable=self.medio, width=50)
        self.ent_medio.place(x=60, y=35)

        self.lbl_seccion=Label(master=self.frm_datos, text="Sección", width=50, anchor=W)
        self.lbl_seccion.place(x=5, y=65)
        self.ent_seccion=Entry(master=self.frm_datos, textvariable=self.seccion, width=50)
        self.ent_seccion.place(x=60, y=65)

        self.lbl_titulo=Label(master=self.frm_datos, text="Título", width=50, anchor=W)
        self.lbl_titulo.place(x=5, y=95)
        self.ent_titulo=Entry(master=self.frm_datos, textvariable=self.titulo, width=50)
        self.ent_titulo.place(x=60, y=95)

        self.lbl_cuerpo=Label(master=self.frm_datos, text="Cuerpo", width=50, anchor=W)
        self.lbl_cuerpo.place(x=5, y=125)
        self.ent_cuerpo=Text(master=self.frm_datos, width=50, height=10)
        self.ent_cuerpo.place(x=60, y=125)

        self.frm_datos.pack(side=TOP, expand=NO, fill=X) #place(x=5,y=400)

        self.frm_grilla = Frame(master=self.frm_contenedor, height=100, borderwidth=1, relief=RAISED)

        self.tree = Treeview(master=self.frm_grilla)
        self.tree["columns"] = ("Fecha", "Medio", "Seccion", "Titulo")
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("Fecha", width=80, minwidth=80)
        self.tree.column("Medio", width=80, minwidth=80)
        self.tree.column("Seccion", width=80, minwidth=80)
        self.tree.column("Titulo", width=100, minwidth=100)
        self.tree.heading('#0', text='', anchor=CENTER)
        self.tree.heading('Fecha', text='Fecha', anchor=CENTER)
        self.tree.heading('Medio', text='Medio', anchor=CENTER)
        self.tree.heading('Seccion', text='Sección', anchor=CENTER)
        self.tree.heading('Titulo', text='Título', anchor=CENTER)
        self.tree.place(x=5, y=5)
        self.tree.bind("<Double-1>", self.on_double_click)

        self.frm_grilla.pack(side=TOP, expand=YES, fill=BOTH) #place(x=5,y=400)

        self.frm_contenedor.pack(expand=YES, fill=BOTH)

        self.menu_bar = Menu(root)
        self.menu_archivo = Menu(self.menu_bar, tearoff=0)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Acerca de..", command=about)
        self.menu_archivo.add_command(label="Salir", command=root.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.menu_archivo)

        root.config(menu=self.menu_bar)

        clear_data(self)

    def on_double_click(self, event):
        cur_item = self.tree.item(self.tree.focus())
        get_datos(cur_item["text"], self)

if __name__ == "__main__":
    root = Tk()
    Noticias(root)
    root.mainloop()
