# # Conexión
# MONGO_URI=mongodb://localhost:27017/
# DB_NAME=empresa
# COLLECTION_NAME=clientes

# # Rutas de archivos
# PATH_DATOS=datos
# PATH_TRATADOS=tratados
# PATH_DOWNLOADS=downloads


import os
import json
import shutil
import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

# Metodo para borrar datos en coleccion

# def limpiar_coleccion():
#     load_dotenv()
#     try:
#         client = MongoClient(os.getenv("MONGO_URI"))
#         col = client[os.getenv("DB_NAME")][os.getenv("COLLECTION_NAME")]
#         col.delete_many({})
#     except Exception:
#         pass

# if __name__ == "__main__":
#     limpiar_coleccion()

# Metodo para insertar .json etl


def metodo_etl():
    load_dotenv()
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        col = client[os.getenv("DB_NAME")][os.getenv("COLLECTION_NAME")]

        origen = os.getenv("PATH_DATOS")
        destino = os.getenv("PATH_TRATADOS")

        # Crear carpetas si no existen
        if not os.path.exists(origen):
            os.makedirs(origen)
        if not os.path.exists(destino):
            os.makedirs(destino)

        # Método nuevo
        archivos = [f for f in os.listdir(origen) if f.endswith('.json')]

        # Método antiguo
        # archivos = []
        # todos_los_nombres = os.listdir(origen)
        # for nombre in todos_los_nombres:
        #     if nombre.endswith(".json"):
        #         archivos.append(nombre)

        if not archivos:
            print("--- No se encontraron archivos para procesar ---")
            return

        for f in archivos:
            # todos los archivos .json en modo lectura (r) los vas a insertar  en la carpeta datos, sí hay uno pues lo inserta y si es varios pues que lo haga

            with open(f"{origen}/{f}", 'r', encoding='utf-8') as file:
                datos = json.load(file)
                if isinstance(datos, list):
                    col.insert_many(datos)
                else:
                    col.insert_one(datos)

            # Renombrar con timestamp para evitar sobreescribir en destino o los incrementos
            fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            # vamos a cortar con el split pero por el punto (.)
            nombre_nuevo = f"{f.split('.')[0]}_{fecha}.json"
            shutil.move(f"{origen}/{f}", f"{destino}/{nombre_nuevo}")
            print(f"--- Procesado correctamente: {f} -> {nombre_nuevo} ---")

    except Exception as e:
        print(f"--- Error en proceso ETL: {e} ---")


if __name__ == "__main__":
    metodo_etl()
    print("--- Tarea finalizada ---")


# Insertar manualmente por terminal lois datos

def registro_manual():
    load_dotenv()
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        col = client[os.getenv("DB_NAME")][os.getenv("COLLECTION_NAME")]

        while True:
            print("\n--- INICIO DE REGISTRO MANUAL ---")
            doc = {
                "nombre": input("Nombre: "),
                "apellidos": input("Apellidos: "),
                "direccion": input("Direccion: "),
                "cp": input("Codigo Postal: "),
                "correo": input("Correo electronico: "),
                "telefono": input("Telefono: "),
                "estado_civil": input("Estado Civil: ")
            }
            col.insert_one(doc)
            print("--- Registro guardado con exito ---")

            op = input("¿Desea introducir otro registro? (s/n): ").lower()
            if op != 's':
                break
    except Exception as e:
        print(f"--- Error en el registro manual: {e} ---")


if __name__ == "__main__":
    registro_manual()
    print("--- Proceso de registro cerrado ---")


# Update manual

def buscar_y_editar():
    load_dotenv()
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        col = client[os.getenv("DB_NAME")][os.getenv("COLLECTION_NAME")]

        print("\n--- BUSQUEDA PARA EDICION ---")
        campo_busqueda = input("Campo para filtrar (ej: nombre, correo): ")
        valor_busqueda = input(f"Valor de {campo_busqueda}: ")

        doc = col.find_one({campo_busqueda: valor_busqueda})

        if doc:
            while True:
                print(f"\n--- Registro seleccionado: {doc['_id']} ---")
                print("Valores actuales:")
                for k, v in doc.items():
                    if k != "_id":
                        print(f"- {k}: {v}")

                print(
                    "\nIndique que campo desea modificar o 'salir' para terminar este registro")
                campo_a_cambiar = input("Campo a editar: ")

                if campo_a_cambiar.lower() == 'salir':
                    break

                if campo_a_cambiar in doc and campo_a_cambiar != "_id":
                    nuevo_valor = input(
                        f"Nuevo valor para {campo_a_cambiar}: ")
                    col.update_one({"_id": doc["_id"]}, {
                                   "$set": {campo_a_cambiar: nuevo_valor}})
                    # Actualizamos la variable local para mostrar los cambios
                    doc[campo_a_cambiar] = nuevo_valor
                    print("--- Campo actualizado local y remotamente ---")
                else:
                    print("--- El campo indicado no existe ---")

                continuar = input(
                    "¿Desea modificar otro campo de este registro? (s/n): ").lower()
                if continuar != 's':
                    break
        else:
            print("--- No se encontro ningun registro coincidente ---")

    except Exception as e:
        print(f"--- Error en edicion: {e} ---")


if __name__ == "__main__":
    buscar_y_editar()
    print("--- Salida del editor ---")

# Escaner duplicados


def scanner_duplicados():
    load_dotenv()
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        col = client[os.getenv("DB_NAME")][os.getenv("COLLECTION_NAME")]

        print("\n--- INICIANDO ESCANEO DE DUPLICADOS EXACTOS ---")

        # Agrupamos por todos los campos del JSON para identificar clones reales
        pipeline = [
            {
                "$group": {
                    "_id": {
                        "nombre": "$nombre",
                        "apellidos": "$apellidos",
                        "direccion": "$direccion",
                        "cp": "$cp",
                        "correo": "$correo",
                        "telefono": "$telefono",
                        "estado_civil": "$estado_civil"
                    },
                    "ids": {"$push": "$_id"},
                    "total": {"$sum": 1}
                }
            },
            {
                "$match": {"total": {"$gt": 1}}
            }
        ]

        duplicados = list(col.aggregate(pipeline))

        if not duplicados:
            print("--- No se detectaron duplicados exactos en la base de datos ---")
            return

        for grupo in duplicados:
            print(
                f"--- Detectados {grupo['total']} registros identicos para: {grupo['_id']['nombre']} {grupo['_id']['apellidos']} ---")
            # Dejamos el primer ID de la lista y preparamos el resto para borrar
            sobrantes = grupo['ids'][1:]
            col.delete_many({"_id": {"$in": sobrantes}})
            print(
                f"--- Se han eliminado {len(sobrantes)} copias sobrantes ---")

    except Exception as e:
        print(f"--- Error en el scanner: {e} ---")


if __name__ == "__main__":
    scanner_duplicados()
    print("--- Escaneo y limpieza finalizados ---")

# Proyecto final


# --- CONFIGURACION INICIAL Y CONEXION ---
load_dotenv()
try:
    CLIENT = MongoClient(os.getenv("MONGO_URI"))
    DB = CLIENT[os.getenv("DB_NAME")]
    COL = DB[os.getenv("COLLECTION_NAME")]
except Exception as e:
    print(f"--- Error critico de conexion: {e} ---")
    exit()

# --- LOGICA DE CONTROL DE FLUJO ---


def flujo_control(funcion_ejecutada):
    while True:
        print("\n" + "-"*30)
        print("1. Repetir ultima accion")
        print("2. Volver al menu principal")
        print("3. Salir del programa")
        op = input("Seleccione una opcion (1/2/3): ")

        if op == "1":
            print("\n--- Repitiendo accion ---")
            funcion_ejecutada()
            continue
        elif op == "2":
            return
        elif op == "3":
            print("\n--- Cerrando servicios y finalizando programa ---")
            print("--- Gracias por su visita, hasta pronto ---")
            exit()
        else:
            print("--- Opcion no valida, intente de nuevo ---")

# --- FUNCIONES DEL SISTEMA ---


def metodo_etl():
    try:
        origen = os.getenv("PATH_DATOS")
        destino = os.getenv("PATH_TRATADOS")

        if not os.path.exists(origen):
            os.makedirs(origen)
        if not os.path.exists(destino):
            os.makedirs(destino)

        archivos = [f for f in os.listdir(origen) if f.endswith('.json')]
        if not archivos:
            print("--- No hay archivos pendientes de procesar en /datos ---")
            return

        for f in archivos:
            with open(f"{origen}/{f}", 'r', encoding='utf-8') as file:
                datos = json.load(file)
                if isinstance(datos, list):
                    COL.insert_many(datos)
                else:
                    COL.insert_one(datos)

            fecha = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_nuevo = f"{f.split('.')[0]}_{fecha}.json"
            shutil.move(f"{origen}/{f}", f"{destino}/{nombre_nuevo}")
            print(f"--- Archivo procesado y movido: {nombre_nuevo} ---")
    except Exception as e:
        print(f"--- Error en proceso ETL: {e} ---")


def listar_clientes():
    try:
        print("\n--- LISTADO COMPLETO DE CLIENTES ---")
        cursor = COL.find()
        hay_datos = False
        for d in cursor:
            hay_datos = True
            print("-" * 25)
            # Listado dinámico de todos los campos que contenga el documento
            for k, v in d.items():
                print(f"{k}: {v}")
        if not hay_datos:
            print("--- La base de datos esta actualmente vacia ---")
    except Exception as e:
        print(f"--- Error al listar: {e} ---")


def registro_manual():
    try:
        print("\n--- NUEVO REGISTRO MANUAL (7 CAMPOS) ---")
        doc = {
            "nombre": input("Nombre: "),
            "apellidos": input("Apellidos: "),
            "direccion": input("Direccion: "),
            "cp": input("CP: "),
            "correo": input("Correo: "),
            "telefono": input("Telefono: "),
            "estado_civil": input("Estado Civil: ")
        }
        COL.insert_one(doc)
        print("--- Registro guardado correctamente en MongoDB ---")
    except Exception as e:
        print(f"--- Error en el registro: {e} ---")


def buscar_y_editar():
    try:
        print("\n--- BUSQUEDA PARA EDICION ---")
        campo_busqueda = input("Campo de busqueda (nombre/correo/telefono): ")
        valor_busqueda = input(f"Valor de {campo_busqueda}: ")
        doc = COL.find_one({campo_busqueda: valor_busqueda})

        if doc:
            while True:
                print(f"\n--- Registro actual: {doc['_id']} ---")
                for k, v in doc.items():
                    if k != "_id":
                        print(f"  {k}: {v}")

                campo_a_cambiar = input(
                    "\nNombre del campo a editar (o 'salir'): ")
                if campo_a_cambiar.lower() == 'salir':
                    break

                if campo_a_cambiar in doc and campo_a_cambiar != "_id":
                    nuevo_valor = input(
                        f"Nuevo valor para {campo_a_cambiar}: ")
                    COL.update_one({"_id": doc["_id"]}, {
                                   "$set": {campo_a_cambiar: nuevo_valor}})
                    doc[campo_a_cambiar] = nuevo_valor
                    print("--- Valor actualizado ---")
                else:
                    print("--- El campo indicado no es valido ---")

                if input("¿Modificar otro campo de este cliente? (s/n): ").lower() != 's':
                    break
        else:
            print("--- No se encontro ningun registro coincidente ---")
    except Exception as e:
        print(f"--- Error en edicion: {e} ---")


def buscar_eliminar():
    try:
        print("\n--- ELIMINACION DISCRIMINADA DE REGISTRO ---")
        campo = input("Campo de busqueda: ")
        valor = input(f"Valor de {campo}: ")

        # Buscamos todos los registros que coincidan para permitir seleccion manual
        resultados = list(COL.find({campo: valor}))

        if not resultados:
            print("--- No se han encontrado registros coincidentes ---")
            return

        print(f"\nSe han encontrado {len(resultados)} coincidencias:")
        for i, doc in enumerate(resultados):
            print(f"\n[{i}] " + "-"*20)
            for k, v in doc.items():
                print(f"    {k}: {v}")

        seleccion = input(
            "\nIndique el NUMERO del registro que desea eliminar (o ENTER para cancelar): ")

        if seleccion.isdigit():
            idx = int(seleccion)
            if 0 <= idx < len(resultados):
                doc_a_borrar = resultados[idx]
                confirmar = input(
                    f"¿Seguro que desea borrar a {doc_a_borrar.get('nombre')}? (s/n): ").lower()
                if confirmar == 's':
                    COL.delete_one({"_id": doc_a_borrar["_id"]})
                    print("--- Registro borrado con exito ---")
                else:
                    print("--- Operacion cancelada ---")
            else:
                print("--- Numero fuera de rango ---")
        else:
            print("--- Operacion cancelada ---")

    except Exception as e:
        print(f"--- Error al eliminar: {e} ---")


def scanner_duplicados():
    try:
        print("\n--- ESCANEANDO DUPLICADOS CLONICOS (1:1) ---")
        pipeline = [
            {"$group": {
                "_id": {
                    "nombre": "$nombre", "apellidos": "$apellidos", "direccion": "$direccion",
                    "cp": "$cp", "correo": "$correo", "telefono": "$telefono", "estado_civil": "$estado_civil"
                },
                "ids": {"$push": "$_id"},
                "total": {"$sum": 1}
            }},
            {"$match": {"total": {"$gt": 1}}}
        ]
        dups = list(COL.aggregate(pipeline))
        if not dups:
            print("--- No hay duplicados exactos ---")
            return

        for g in dups:
            print(
                f"--- Grupo duplicado: {g['_id']['nombre']} {g['_id']['apellidos']} ({g['total']} veces) ---")
            COL.delete_many({"_id": {"$in": g['ids'][1:]}})
            print(
                f"--- Limpieza realizada: se mantuvo 1 y se borraron {g['total'] - 1} ---")
    except Exception as e:
        print(f"--- Error en el scanner: {e} ---")


def exportar_backup():
    try:
        ruta = os.getenv("PATH_DOWNLOADS")
        if not os.path.exists(ruta):
            os.makedirs(ruta)
        datos = list(COL.find())
        for d in datos:
            d["_id"] = str(d["_id"])
        with open(f"{ruta}/backup_clientes.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"--- Backup generado en: {ruta}/backup_clientes.json ---")
    except Exception as e:
        print(f"--- Error al exportar: {e} ---")

# --- MENU PRINCIPAL ---


def main():
    while True:
        print("\n" + "="*40)
        print("   GESTOR DE BASE DE DATOS EMPRESA")
        print("="*40)
        print("1. Procesar /datos (ETL)")
        print("2. Listar Clientes")
        print("3. Registro Manual")
        print("4. Buscar y Editar")
        print("5. Buscar y Eliminar")
        print("6. Scanner de Duplicados")
        print("7. Exportar a /downloads")
        print("0. Salir")

        opcion = input("\nSeleccione una opcion: ")

        acciones = {
            "1": metodo_etl, "2": listar_clientes, "3": registro_manual,
            "4": buscar_y_editar, "5": buscar_eliminar, "6": scanner_duplicados,
            "7": exportar_backup
        }

        if opcion == "0":
            print("\n--- Finalizando programa ---")
            print("--- Servicios cerrados ---")
            break
        elif opcion in acciones:
            acciones[opcion]()
            flujo_control(acciones[opcion])
        else:
            print("--- Opcion no valida ---")


if __name__ == "__main__":
    main()
