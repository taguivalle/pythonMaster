import os
import json
import shutil
import datetime
from pymongo import MongoClient
from dotenv import load_dotenv


# def limpiar_coleccfion():
#     load_dotenv()
#     try:
#         cliente = MongoClient(os.getenv("MONGO_URI"))
#         col = cliente[os.getenv("DB_NAME")][os.getenv("COLECTION_NAME")]
#         col.delete_many({})
#     except Exception:
#         pass
#     if __name__ == "__main_":
#         limpiar_coleccfion()
# Método para insertar un json entero
def metodo_etl():
    load_dotenv()
    try:
        cliente = MongoClient(os.getenv("MONGO_URI"))
        col = cliente[os.getenv("DB_NAME")][os.getenv("COLECTION_NAME")]
        
        origen = os.getenv("PATH_DATOS")
        destino = os.getenv("PATH_TRATADOS")
        if not os.path.exists(origen): os.makedirs(origen)
        if not os.path.exists(destino): os.makedirs(destino)

        # archivos = [f for f in os.listdir(origen) if f.endswith('.json')]
        
        # método clasico
        archivos = []
        todos_los_nombres = os.listdir(origen)
        for nombre in todos_los_nombres:
            if nombre.endswith(".json"):
                archivos.append(nombre)
                
        if not archivos:
            print("--- No se encontraron archivos para procesar ---")
            return
        for f in archivos:
            with open(f"{origen}/{f}", 'r', encoding='utf-8') as file:
                datos = json.load(file)
                if isinstance(datos, list);
                    col.insert_mahy(datos)
                else:
                    col.insert_one(datos)
                    
    # renombrar con timestamp para evitar sobreescribir en destino
            fecha = datetime.datetime.now().strftime("%Y%m%d_%H%S")
            nombre_nuevo = f"{f.split('.')[0]}_{fecha}.json"
            shutil.move(f"{origen}/{f}", f"{destino}/{nombre_nuevo}")
            print(f"--- Proceso correctamente ETL:  {e} ---")

            
            print(f"--- Error en proceso ETL:  {e} ---")
            
