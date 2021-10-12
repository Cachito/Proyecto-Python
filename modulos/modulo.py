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
        showinfo("Carro-Meier", f"error al crear base de datos: {sys.exc_info()[0]}")

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
            showinfo("Carro-Meier", "Tabla `Noticias` creada con éxito")

        except Exception as e:
            db_cacho.rollback()
            db_cacho.close()
            showinfo("Carro-Meier", f"error al crear tabla `Noticias`: {str(e)}")

    except Exception as e:
        showinfo("Carro-Meier", f"error al abrir base de datos carro_maier: {str(e)}")

def clear_data(self):
    self.fecha = ""
    self.medio = ""
    self.seccion = ""
    self.titulo = ""
    self.cuerpo = ""
    self.archivo = ""
    self.ent_cuerpo.delete("1.0", END)

def save_data(fecha, medio, seccion, titulo, cuerpo):
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

            sql_insert = """
                INSERT INTO Noticias (Fecha, Medio, Seccion, Titulo, Cuerpo)
                    VALUES (%s, %s, %s, %s, %s)
            """
            datos = (fecha, medio, seccion, titulo, cuerpo)

            csr_cacho.execute(sql_insert, datos)

            db_cacho.commit()
            db_cacho.close()
            showinfo("Carro-Meier", "registro insertado con éxito")

        except Exception as e:
            db_cacho.rollback()
            db_cacho.close()
            showinfo("Carro-Meier", f"error al insertar registro en tabla Noticias: {str(e)}")

    except Exception as e:
        showinfo("Carro-Meier", f"error al abrir base de datos carro_maier: {str(e)}")

def valida(fecha, medio, seccion, titulo, cuerpo):
    msj_error = ""

    if not fecha:
        msj_error = " fecha "
    else:
        try:
            datetime.datetime.strptime(fecha, '%Y/%m/%d')
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
        showinfo("Carro-Meier", f"debe ingresar: {msj_error}")
        return False
    else:
        return True

def delete_data():
    print(f"Borrando")

def buscar():
    print(f"Buscando")

def about():
    showinfo("Entrega Intermedia", "Cargador de Noticias\n\nGrupo:\n- Luis Carro\n- Cristian Maier")