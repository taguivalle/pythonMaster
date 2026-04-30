from datetime import datetime
# se utiliza para mover archivos de manera local, que pueda acceder para tratar mis archivos como (borrer, mover, load, etc.)
import shutil
import json  # para hacer el json load
import shutil
from dotenv import load_dotenv
import time
import numpy as np
import matplotlib.pyplot as plt  # <-- IMPORTANTE: agregar .pyplot
import sys
import os
import random
import math
import datetime
import json
import csv
import faker


# vamos trabajar con listas
# inicio = time.time()
# lista = list(range(1000000))
# lista = [x**2 for x in lista]  # ejemplo de operación con listas
# fin = time.time()
# print("Tiempo de lista:", fin - inicio, "segundos")

# ahora con numpy
# inicio = time.time()
# num_array = np.arange(1000000)
# num_array = num_array ** 2  # ejemplo de operación con arrays de numpy
# fin = time.time()
# print("Tiempo de array de numpy:", fin - inicio, "segundos")

# vamos a hacer unas variables de entorno
# from dotenv import load_dotenv
# con esta librería se manejan las variables de entorno externas al código, como rutas, claves, etc.
# import os

# load_dotenv()

# ruta_json = os.getenv("RUTA_JSON")
# ruta_csv = os.getenv("RUTA_CSV")
# procesados = os.getenv("CARPETA_PROCESADOS")
# tratados = os.getenv("CARPETA_TRATADOS")
# datos = os.getenv("CARPETA_DATOS")

# print("Ruta del JSON desde variable de entorno:", ruta_json)
# print("Ruta del CSV desde variable de entorno:", ruta_csv)
# print("Ruta de los archivos procesados desde variable de entorno:", procesados)
# print("Ruta de los archivos tratados desde variable de entorno:", tratados)

'''
en el siguiente bloque de código utilizamos las lineas 25 a la 33 de este archvio
'''
# asegurarnos cuando trabajemos con carpetas que las claves sean únicas


# def asegurar_carpeta(ruta):
#     try:
#         if not os.path.exists(ruta):
#             os.mkdir(ruta)
#             print(f"Carpeta creada: {ruta}")
#         else:
#             print(f"La carpeta ya existe: {ruta}")
#     except Exception as e:
#         print(f"Error al crear la carpeta '{ruta}': {e}")


# asegurar_carpeta(procesados)  # Intentar nuevamente
# asegurar_carpeta(tratados)  # Intentar nuevamente

# la librería faker es una herramienta útil para generar datos de prueba, como nombres, direcciones, correos electrónicos, etc. Esto es especialmente útil para pruebas y desarrollo cuando no se dispone de datos reales o se desea evitar el uso de datos sensibles.
# from faker import Faker
# import faker.providers
# faker.providers.BaseProvider

# fake = Faker()
# print("Nombre falso:", fake.name())
# print("Dirección falsa:", fake.address())
# print("Correo electrónico falso:", fake.email())

# vamos a ver json
# import json
# def leer_json(ruta):
#     try:
#         with open(ruta, 'r') as archivo:
#             datos = json.load(archivo)
#             print(f"Datos leídos correctamente del archivo JSON '{ruta}': {datos}")
#             return datos
#     except Exception as e:
#         print(f"Error al leer el archivo JSON '{ruta}': {e}")
#         return None
# datos_ejemplo = leer_json("datos/clientes.json")
# datos_ejemplo = leer_json(ruta_json)

# BANDERA siendo las 1:24 horas

'''vamos a ver un flaper o aplanar es un comienzo muy clásico de las SQL, las: SQL Y LAS NOSQL, o sea las que funcionan de manera secuenciales o cerradas y las que no funiconan de manera secuencial las nos permiten más libertad (oracle, SQL con más secuenciales) tienen que darnos si o si las columnas, las filas etc. Pero si nos agrega un JSON estas no entienden de ese tipo de formato. Por lo tanto JSON es uno de los archivos màs utilizados, por comodidad, visual y por lógistica.
'''


# def aplanar_json(data):
#     try:
#         filas = []
#         for clave in data:
#             fila = data[clave]
#             # fila['id'] = clave  # Agregar la clave como un campo en la fila
#             filas.append([clave, data[clave]])

#         print(
#             f"Transofrmación completada: Se han procesado {len(filas)} campos.")
#         return filas
#     except Exception as e:
#         print(f"Error al aplanar los datos: {e}")
#         # return None


# # ejemplo sencillo de un cliente
# cliente_ejemplo = {"cliente1": {"nombre": "Juan", "edad": 30},
#                    "cliente2": {"nombre": "María", "edad": 25}}
# print(f"entrada (Diccionario): {cliente_ejemplo}")
# resultado = aplanar_json(cliente_ejemplo)
# print(f"salida (Lista de listas): {resultado}")

# vamos a ver el dotenv en la 1:40 horas; primero se importan las librerías

# se tienen las variables de entorno cargadas
load_dotenv()
ruta_json = os.getenv("RUTA_JSON")
ruta_csv = os.getenv("RUTA_CSV")
procesados = os.getenv("CARPETA_PROCESADOS")
tratados = os.getenv("CARPETA_TRATADOS")
datos = os.getenv("CARPETA_DATOS")


# Primero un método para asegurarnos que la carpeta existe

def asegurar_carpeta(ruta):
    if not os.path.exists(ruta):
        os.mkdir(ruta)  # mkdir para crear

# Segundo un método para asegurarnos la ruta del archivo


def asegurar_ruta_archivo(ruta):
    carpeta = os.path.dirname(ruta)  # dirname es el nombre del directorio
    if carpeta != "" and not os.path.exists(carpeta):
        os.makedirs(carpeta)

# Tercero: método para definir el JSON


def leer_json(ruta):
    try:
        with open(ruta, 'r') as archivo:
            # datos = json.load(archivo)
            # print(
            #     f"Datos leídos correctamente del archivo JSON '{ruta}': {datos}")
            return json.load(archivo)  # solamente para que lea el archivo
    except FileNotFoundError:  # otro método de excepción
        print("No existe el archivo JSOn, no se realiza el tratamiento")
        return None
    # otra excepción en caso de que la encuentre
    except:
        print("Error leyendo JSON")
        return None

# Cuarto método, generar el nombre al CSV


def generar_nombre_csv(ruta_base):
    # el datetime recupera el momento exacto de la ejecución, en este caso con un formato en concreto (año, mes, día)
    fecha = datetime.datetime.now().strftime("%Y%m%d")
    # con el rsplit se busca el punto y se hace un corte
    nombre, extension = ruta_base.rsplit('.', 1)
    return f"{nombre}_{fecha}.{extension}"


# Quinto método, coger el JSON y convertirlo en CSV, utilizando las buenas prácticas de crearnos un nombre de archivo; para qué? para evitar equivocaciones (por así decirlo) para eso invoca la librería datetime
# Quinto método: aplanar JSON
def aplanar_json(data):
    filas = []
    for cliente in data:
        for clave in cliente:
            filas.append([clave, cliente[clave]])
    return filas  # ✅ Fuera de ambos bucles


# Sexto método: guardar CSV
def guardar_csv(filas, ruta):
    with open(ruta, "w") as archivo:
        archivo.write("columna, valor\n")  # Cabecera, solo una vez
        for fila in filas:
            archivo.write(f"{fila[0]}, {fila[1]}\n")  # ✅ Un solo bucle


# Séptimo método: procesar todo
def procesar():
    asegurar_carpeta(procesados)
    asegurar_carpeta(tratados)
    asegurar_ruta_archivo(ruta_json)
    asegurar_ruta_archivo(ruta_csv)

    data = leer_json(ruta_json)
    if data is None:
        return

    ruta_csv_fecha = generar_nombre_csv(ruta_csv)
    filas = aplanar_json(data)
    guardar_csv(filas, ruta_csv_fecha)

    shutil.move(ruta_json, f"{tratados}/clientes.json")
    shutil.move(ruta_csv_fecha,  # Dentro de la función
                # Con paréntesis
                f"{procesados}/{os.path.basename(ruta_csv_fecha)}")
    print("Proceso completado")


# Ejecutar
procesar()
