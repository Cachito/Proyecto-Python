import tkinter
import mysql.connector
import sys
import re
import datetime
from tkinter import *
from tkinter.messagebox import *

def create_data():
    db_cacho = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )

    try:
        csr_cacho = db_cacho.cursor()

        sql_drop = "DROP DATABASE IF EXISTS carro_maier"
        sql_create = "CREATE DATABASE carro_maier"

        csr_cacho.execute(sql_drop)
        csr_cacho.execute(sql_create)

        db_cacho.commit()
        db_cacho.close()
        showinfo("Carro-Maier", "Base de datos carro_meier creada con éxto")

    except:
        db_cacho.rollback()
        db_cacho.close()
        showinfo("Carro-Maier", f"error al crear base de datos: {sys.exc_info()[0]}")

def create_table():
    try:
        db_cacho = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="carro_maier"
        )
        try:
            csr_cacho = db_cacho.cursor()

            sql_drop = "DROP TABLE IF EXISTS `Noticias`"
            sql_create = """
                CREATE TABLE `Noticias`(
                    Id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    Fecha DATE,
                    Medio VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                    Seccion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                    Titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL,
                    Cuerpo TEXT COLLATE utf8_spanish2_ci NOT NULL
                    )
                """
            csr_cacho.execute(sql_drop)
            csr_cacho.execute(sql_create)
            db_cacho.commit()
            db_cacho.close()
            showinfo("Carro-Maier", "Tabla `Noticias` creada con éxito")

        except Exception as e:
            db_cacho.rollback()
            db_cacho.close()
            showinfo("Carro-Maier", f"error al crear tabla `Noticias`: {str(e)}")

    except Exception as e:
        showinfo("Carro-Maier", f"error al abrir base de datos carro_maier: {str(e)}")

def get_datos(search_id, self):
    if not search_id:
        showinfo("Carro-Maier", f"Debe seleccionar algo")
        return
        
    try:
        db_cacho = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="carro_maier"
        )

        try:
            csr_cacho = db_cacho.cursor()
            sql_get = f"""
                SELECT
                    Id
                    , Fecha
                    , Medio
                    , Seccion
                    , Titulo
                    , Cuerpo
                FROM Noticias
                WHERE Id = {search_id}
                """

            csr_cacho.execute(sql_get)
            resultado = csr_cacho.fetchone()

            clear_data(self)

            if resultado is None:
                showinfo("Carro-Maier", f"registro com id {search_id} no encontradores")
            else:
                self.id = resultado[0]
                self.fecha = resultado[1]
                self.medio = resultado[2]
                self.seccion = resultado[3]
                self.titulo = resultado[4]

                self.ent_fecha.insert(0, resultado[1])
                self.ent_medio.insert(0, resultado[2])
                self.ent_seccion.insert(0, resultado[3])
                self.ent_titulo.insert(0, resultado[4])
                self.ent_cuerpo.insert("1.0", resultado[5])

            db_cacho.close()

        except Exception as e:
            db_cacho.close()
            showinfo("Carro-Maier", f"error al leer registros en tabla Noticias: {str(e)}")

    except Exception as e:
        showinfo("Carro-Maier", f"error al abrir base de datos carro_maier: {str(e)}")

def refresh(self):
    # limpieza de tabla
    records = self.tree.get_children()
    for element in records:
        self.tree.delete(element)

    try:
        db_cacho = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="carro_maier"
        )

        try:
            csr_cacho = db_cacho.cursor()
            sql_get = """
                SELECT
                    Id
                    , Fecha
                    , Medio
                    , Seccion
                    , Titulo
                    , Cuerpo
                FROM Noticias
                ORDER BY Fecha DESC
                """

            csr_cacho.execute(sql_get)
            resultado = csr_cacho.fetchall()

            for fila in resultado:
                self.tree.insert('', 0, text = fila[0], values = (fila[1],fila[2],fila[3],fila[4]))

            db_cacho.close()

        except Exception as e:
            db_cacho.close()
            showinfo("Carro-Maier", f"error al leer registros en tabla Noticias: {str(e)}")

    except Exception as e:
        showinfo("Carro-Maier", f"error al abrir base de datos carro_maier: {str(e)}")

def clear_data(self):
    self.id = "0"
    self.fecha = ""
    self.medio = ""
    self.seccion = ""
    self.titulo = ""
    self.cuerpo = ""
    #self.archivo = ""
    self.cuerpo = ""
    self.busqueda = ""

    self.ent_fecha.delete(0, END)
    self.ent_medio.delete(0, END)
    self.ent_seccion.delete(0, END)
    self.ent_titulo.delete(0, END)
    #self.ent_archivo.delete(0, END)
    self.ent_cuerpo.delete("1.0", END)
    self.ent_fecha.delete(0, END)
    self.ent_busqueda.delete(0, END)

def save_data(id, fecha, medio, seccion, titulo, cuerpo, self):
    if not valida(fecha, medio, seccion, titulo, cuerpo):
        return

    try:
        db_cacho = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="carro_maier"
        )

        try:
            csr_cacho = db_cacho.cursor()

            medio = re.sub("[\"']", r"", medio)
            seccion = re.sub("[\"']", r"", seccion)
            titulo = re.sub("[\"']", r"", titulo)
            cuerpo = re.sub("[\"']", r"", cuerpo)

            if id == "0":
                sql_insert = """
                    INSERT INTO Noticias (Fecha, Medio, Seccion, Titulo, Cuerpo)
                        VALUES (%s, %s, %s, %s, %s)
                    """
                datos = (fecha, medio, seccion, titulo, cuerpo)

                csr_cacho.execute(sql_insert, datos)
            else:
                sql_update = f"""
                    UPDATE Noticias SET
                        Fecha = '{fecha}',
                        Medio = '{medio}',
                        Seccion = '{seccion}',
                        Titulo = '{titulo}',
                        Cuerpo = '{cuerpo}'
                    WHERE Id = {id}
                    """
                csr_cacho.execute(sql_update)

            db_cacho.commit()
            db_cacho.close()
            showinfo("Carro-Maier", f"registro {'insertado' if id == '0' else 'actualizado'} con éxito")
            refresh(self)
            clear_data(self)

        except Exception as e:
            db_cacho.rollback()
            db_cacho.close()
            showinfo("Carro-Maier", f"error al {'insertar' if id == '0' else 'actualizar'} registro en tabla Noticias: {str(e)}")

    except Exception as e:
        showinfo("Carro-Maier", f"error al abrir base de datos carro_maier: {str(e)}")

def delete_data(self):
    if self.id == "0":
        showinfo("Carro-Maier", "debe selccionar algún registro")
        return

    try:
        db_cacho = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="carro_maier"
        )

        try:
            csr_cacho = db_cacho.cursor()
            sql_delete = f"""
                DELETE FROM Noticias
                WHERE Id = {self.id}
                """
            csr_cacho.execute(sql_delete)
            db_cacho.commit()
            db_cacho.close()
            showinfo("Carro-Maier", f"registro id {self.id} eliminado")
            refresh(self)
            clear_data(self)

        except Exception as e:
            db_cacho.rollback()
            db_cacho.close()
            showinfo("Carro-Maier", f"error al eliminar registro en tabla Noticias: {str(e)}")

    except Exception as e:
        showinfo("Carro-Maier", f"error al abrir base de datos carro_maier: {str(e)}")

def valida(fecha, medio, seccion, titulo, cuerpo):
    msj_error = ""

    if not fecha:
        msj_error = " fecha "
    else:
        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            msj_error = " el formato de la fecha debe ser YYYY/MM/dd"

    if not medio:
        msj_error = f"{msj_error} medio "

    if not seccion:
        msj_error = f"{msj_error} seccion "

    if not titulo:
        msj_error = f"{msj_error} título "

    if not cuerpo:
        msj_error = f"{msj_error} cuerpo "

    if msj_error:
        showinfo("Carro-Maier", f"debe ingresar: {msj_error}")
        return False
    else:
        return True

def buscar(search_id, self):
    if not search_id:
        showinfo("Carro-Maier", "debe ingresar un id de noticia")
        return

    if not re.match(r'^(\d+)$', search_id):
        showinfo("Carro-Maier", "debe ingresar sólo números")
        return

    get_datos(search_id, self)

def about():
    showinfo("Entrega Final", "Cargador de Noticias\n\nGrupo:\n- Luis Carro\n- Cristian Maier")