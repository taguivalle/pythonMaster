
# print("Bienvenido")
# print("Bienvenido")
# print("Bienvenido")

# '''
# Estamos repitiendo código
# Esto no es eficiente
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Primera función

# def saludar():
#     print("Bienvenido")

# saludar()
# saludar()
# saludar()

# '''
# def crea una función

# La función no se ejecuta sola
# Hay que llamarla
# '''

# "-------------------------------------------------------------------------------------------------------"
# #Parámetros

# def saludar(nombre):
#     print("Bienvenido", nombre)

# saludar("Ana")
# saludar("Luis")

# '''
# nombre es un parámetro
# Permite reutilizar la función con distintos valores
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Return

# def sumar(a, b):
#     return a + b

# resultado = sumar(5, 3)

# print(resultado)

# '''
# return devuelve el valor
# Permite guardar el resultado en una variable
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Función con if

# def es_mayor(edad):

#     if edad >= 18:
#         return True
#     else:
#         return False

# print(es_mayor(20))

# '''
# La función devuelve True o False
# '''


# "-------------------------------------------------------------------------------------------------------"

# #Funcion con for

# def mostrar_lista(lista):

#     for elemento in lista:
#         print(elemento)

# nombres = ["Ana", "Luis", "Mario"]

# mostrar_lista(nombres)

# '''
# Recorre la lista y muestra cada elemento
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Buscar palabra en texto

# def contiene_palabra(texto, palabra):

#     texto = texto.lower()
#     palabra = palabra.lower()

#     if palabra in texto:
#         return True
#     else:
#         return False


# frase = "El tesoro está escondido"

# print(contiene_palabra(frase, "TESORO"))

# '''
# Busca una palabra dentro de un texto
# No importa mayúsculas/minúsculas
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Replace en texto

# def reemplazar(texto, vieja, nueva):

#     return texto.replace(vieja, nueva)


# frase = "El mago lanza un hechizo y otro hechizo más"

# print(reemplazar(frase, "hechizo", "conjuro"))

# '''
# Reemplaza TODAS las apariciones de una palabra

# Resultado:
# El mago lanza un conjuro y otro conjuro más
# '''

# #Reemplazamos solo el primer valor hallado

# def reemplazar_primero(texto, vieja, nueva):

#     return texto.replace(vieja, nueva, 1)


# frase = "El mago lanza un hechizo y luego otro hechizo final"

# print(reemplazar_primero(frase, "hechizo", "conjuro"))

# '''
# El tercer parámetro (1) indica cuántas veces reemplazar

# Solo reemplaza la PRIMERA aparición

# Resultado:
# El mago lanza un conjuro y luego otro hechizo final
# '''

# #Reemplazamos solo el último valor

# def reemplazar_ultimo(texto, vieja, nueva):

#     partes = texto.rsplit(vieja, 1)

#     if len(partes) == 2:
#         return partes[0] + nueva + partes[1]
#     else:
#         return texto


# frase = "El mago lanza un hechizo y luego otro hechizo final"

# print(reemplazar_ultimo(frase, "hechizo", "conjuro"))

# '''
# rsplit divide el texto empezando por la derecha

# 1 → solo divide una vez (desde el final)

# Divide el texto en dos partes:
# ANTES del último "hechizo"
# DESPUÉS del último "hechizo"

# Luego reconstruimos el texto manualmente

# Resultado:
# El mago lanza un hechizo y luego otro conjuro final
# '''

# #Reemplazar posiciones específicas

# def reemplazar_posiciones(texto, vieja, nueva, posiciones):

#     palabras = texto.split()

#     contador = 0

#     for i in range(len(palabras)):

#         if palabras[i] == vieja:

#             if contador in posiciones:
#                 palabras[i] = nueva

#             contador += 1

#     return " ".join(palabras)


# frase = "hechizo fuego hechizo hielo hechizo rayo hechizo"

# print(reemplazar_posiciones(frase, "hechizo", "conjuro", [0, 2]))
# #print(reemplazar_posiciones(frase, "hechizo", "conjuro", range(0, 3)))

# '''
# split convierte el texto en lista de palabras

# contador cuenta CUÁNTAS VECES aparece la palabra buscada

# OJO:
# No usamos la posición en la frase,
# sino el número de aparición de la palabra

# Ejemplo:
# hechizo(0) fuego hechizo(1) hielo hechizo(2)...

# [0,2] → cambia el primero y el tercero

# Resultado:
# conjuro fuego hechizo hielo conjuro rayo hechizo
# '''

# "-------------------------------------------------------------------------------------------------------"
# #Rellenar lista

# def rellenar_lista():

#     lista = []

#     cantidad = int(input("Cuantos elementos quieres: "))

#     for i in range(cantidad):
#         valor = input("Elemento: ")
#         lista.append(valor)

#     return lista


# datos = rellenar_lista()

# print(datos)

# '''
# Crea una lista dinámica con input
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Lista → Set

# def lista_a_set(lista):

#     return set(lista)


# numeros = [1,2,2,3,3,4]

# print(lista_a_set(numeros))

# '''
# Convierte lista en set
# Elimina duplicados
# '''

# #Variante sin set

# def eliminar_duplicados_manual(lista):

#     nueva = []

#     for elemento in lista:

#         if elemento not in nueva:
#             nueva.append(elemento)

#     return nueva


# print(eliminar_duplicados_manual([1,2,2,3,3,4]))

# '''
# Recorre la lista

# Solo añade el elemento si no está ya en la nueva lista

# Esto enseña lógica pura (mejor que usar set directamente)
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Set → Lista

# def set_a_lista(conjunto):

#     return list(conjunto)


# datos = {1,2,3}

# print(set_a_lista(datos))

# '''
# Convierte set en lista
# '''


# "-------------------------------------------------------------------------------------------------------"

# #Lista → Diccionario (índice automático)

# def lista_a_diccionario(lista):

#     dic = {}

#     for i in range(len(lista)):
#         dic[i] = lista[i]

#     return dic


# nombres = ["Ana", "Luis", "Mario"]

# print(lista_a_diccionario(nombres))

# '''
# range(len(lista)) genera números desde 0 hasta tamaño-1

# i → será la clave
# lista[i] → será el valor

# Resultado:
# 0 → Ana
# 1 → Luis
# 2 → Mario

# Se usa cuando queremos relacionar posición con valor
# '''

# #Variante

# def lista_a_diccionario_1(lista):

#     dic = {}

#     for i in range(len(lista)):
#         dic[i + 1] = lista[i]

#     return dic


# print(lista_a_diccionario_1(["Ana", "Luis", "Mario"]))

# '''
# i empieza en 0
# i + 1 hace que las claves empiecen en 1

# Resultado:
# 1 → Ana
# 2 → Luis
# 3 → Mario
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Lista → Diccionario (lista como claves)

# def lista_a_diccionario_claves(lista):

#     dic = {}

#     for elemento in lista:
#         dic[elemento] = True
#         #dic[elemento] = ""

#     return dic


# print(lista_a_diccionario_claves(["Ana", "Luis"]))

# '''
# Cada elemento de la lista se convierte en clave

# El valor es True (puede ser cualquier cosa)

# Resultado:
# "Ana": True
# "Luis": True

# Esto se usa para búsquedas rápidas
# (simula un set)

# En caso de optar por elemento = "", lo que hara el metodo es asignar como valor un campo vacio
# a cada clave
# '''


# "-------------------------------------------------------------------------------------------------------"

# #Diccionario → Lista (valores)

# def diccionario_a_lista_valores(dic):

#     lista = []

#     for clave in dic:
#         lista.append(dic[clave])

#     return lista


# persona = {
#     "nombre": "Ana",
#     "edad": 25
# }

# print(diccionario_a_lista_valores(persona))

# '''
# dic[clave] accede al valor

# Resultado:
# ["Ana", 25]
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Diccionario → Lista (claves)

# def diccionario_a_lista_claves(dic):

#     lista = []

#     for clave in dic:
#         lista.append(clave)

#     return lista

# persona = {
#     "nombre": "Ana",
#     "edad": 25
# }

# print(diccionario_a_lista_claves(persona))

# '''
# El for recorre directamente las claves

# Resultado:
# ["nombre", "edad"]
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Diccionario → Lista (clave + valor)

# def diccionario_a_lista_completa(dic):

#     lista = []

#     for clave in dic:
#         lista.append([clave, dic[clave]])

#     return lista

# persona = {
#     "nombre": "Ana",
#     "edad": 25
# }

# print(diccionario_a_lista_completa(persona))

# '''
# Crea una lista de listas

# Cada elemento tiene:
# [clave, valor]

# Resultado:
# [["nombre", "Ana"], ["edad", 25]]

# Muy útil para trabajar datos estructurados
# '''


# "-------------------------------------------------------------------------------------------------------"

# #Invertir lista

# def invertir_lista(lista):

#     nueva = []

#     for i in range(len(lista)-1, -1, -1):
#         nueva.append(lista[i])

#     return nueva


# print(invertir_lista([1,2,3,4]))

# '''
# range(inicio, fin, salto)

# len(lista)-1 → último índice
# Ejemplo: [1,2,3,4] → índices 0,1,2,3 → último es 3

# range(3, -1, -1) significa:
# empieza en 3
# termina en -1 (no incluido)
# va hacia atrás de 1 en 1

# Recorrido:
# 3 → 2 → 1 → 0

# lista[i] irá cogiendo:
# 4 → 3 → 2 → 1

# Por eso se invierte la lista
# '''

# #Variante

# def invertir_lista_simple(lista):

#     return lista[::-1]


# print(invertir_lista_simple([1,2,3,4]))

# '''
# [::-1] es un "slice"

# Empieza al final
# y recorre hacia atrás

# Es una forma corta de invertir listas
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Contar cuántas veces aparece algo

# def contar_repeticiones(lista, valor):

#     contador = 0

#     for elemento in lista:

#         if elemento == valor:
#             contador += 1

#     return contador


# print(contar_repeticiones([1,2,2,3,2], 2))

# '''
# Cuenta cuántas veces aparece un valor en la lista
# '''

# #Contar ocurrencias

# def contar_ocurrencias(texto, palabra):

#     return texto.count(palabra)


# frase = "El oro cuando es oro de verdad es oro puro"

# print(contar_ocurrencias(frase, "oro"))

# '''
# count cuenta cuántas veces aparece una palabra
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Filtrar números pares

# def numeros_pares(lista):

#     resultado = []

#     for n in lista:
#         if n % 2 == 0:
#             resultado.append(n)

#     return resultado


# print(numeros_pares([1,2,3,4,5,6]))

# '''
# Devuelve solo los números pares
# '''


# "-------------------------------------------------------------------------------------------------------"

# #Contar elementos

# def contar_elementos(lista):

#     contador = 0

#     for _ in lista:
#         contador += 1

#     return contador


# print(contar_elementos([1,2,3,4]))

# '''
# Cuenta elementos sin usar len()
# '''


# "-------------------------------------------------------------------------------------------------------"

# #Limpiar texto

# def limpiar_texto(texto):

#     texto = texto.strip()
#     texto = texto.lower()

#     return texto


# print(limpiar_texto("   HOLA MUNDO   "))

# '''
# Quita espacios y pasa a minúsculas
# '''

# #Separar texto en lista

# def texto_a_lista(texto):

#     return texto.split()


# print(texto_a_lista("Hola mundo Python"))

# '''
# split separa texto por espacios

# Resultado:
# ["Hola", "mundo", "Python"]
# '''

# #Unir lista en texto

# def lista_a_texto(lista):

#     texto = ""

#     for elemento in lista:
#         texto += elemento + " "

#     return texto


# print(lista_a_texto(["Hola", "mundo"]))

# '''
# Concatena todos los elementos en un string

# Resultado:
# "Hola mundo "
# '''

# "-------------------------------------------------------------------------------------------------------"

# #Contar vocales

# def contar_vocales(texto):

#     contador = 0

#     for letra in texto.lower():

#         if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#             contador += 1

#     return contador


# print(contar_vocales("Programacion"))

# '''
# Cuenta vocales en un texto
# '''


# "-------------------------------------------------------------------------------------------------------"

# #Buscar elemento en lista

# def buscar_elemento(lista, valor):

#     for elemento in lista:

#         if elemento == valor:
#             return True

#     return False


# print(buscar_elemento([1,2,3], 2))

# '''
# Devuelve True si el elemento existe
# '''


# "-------------------------------------------------------------------------------------------------------"

# #Concatenacion de metodos

# def pedir_numero():

#     numero = -1

#     while numero < 0:
#         numero = int(input("Numero positivo: "))

#     return numero


# def crear_lista():

#     lista = []

#     cantidad = pedir_numero()

#     for i in range(cantidad):
#         lista.append(pedir_numero())

#     return lista


# print(crear_lista())

# '''
# Una función reutiliza otra
# Esto es programación real
# '''


# "-------------------------------------------------------------------------------------------------------"

# #Guardar lista en txt

# def guardar_lista_txt(lista):

#     archivo = open("datos.txt", "w")

#     for elemento in lista:
#         archivo.write(elemento + "\n")

#     archivo.close()


# guardar_lista_txt(["Ana", "Luis", "Mario"])

# '''
# Crea un archivo txt
# Guarda cada elemento en una línea

# "w" → escribe (borra lo anterior)
# '''


# #Leer TXT y convertir en lista

# def leer_txt():

#     archivo = open("datos.txt", "r")

#     lista = []

#     for linea in archivo:
#         lista.append(linea.strip())

#     archivo.close()

#     return lista


# print(leer_txt())

# '''
# Lee archivo txt
# Convierte cada línea en elemento de lista
# '''

# #Variante con texto amplio

# def leer_palabras_txt():
#     lista_palabras = []

#     with open("datos.txt", "r", encoding="utf-8") as archivo:
#         for linea in archivo:

#             palabras = linea.strip().split()

#             lista_palabras.extend(palabras)

#     return lista_palabras

# print(leer_palabras_txt())

# '''
# Usar 'with' cierra el archivo automáticamente al terminar

# Limpiamos espacios/saltos con strip()
# Dividimos la línea en palabras con split()
# Agregamos esas palabras a nuestra lista principal

# '''

# #Version PRO y rapida

# def leer_todo_el_txt():

#     with open("datos.txt", "r", encoding="utf-8") as archivo:

#         lista_palabras = archivo.read().split()

#     return lista_palabras

# print(leer_todo_el_txt())

# "-------------------------------------------------------------------------------------------------------"

# #Ejemplo final combinando metodos para una lista limpia

# def limpiar_nombres(lista):

#     nueva = []

#     for nombre in lista:
#         nueva.append(nombre.lower())

#     return nueva


# def eliminar_duplicados(lista):

#     return list(set(lista))


# def preparar_tripulacion():

#     nombres = rellenar_lista()

#     nombres = limpiar_nombres(nombres)

#     nombres = eliminar_duplicados(nombres)

#     return nombres


# tripulacion = preparar_tripulacion()

# print(tripulacion)

# '''
# Ejemplo completo real:

# input → lista
# limpieza → datos correctos
# set → eliminar duplicados
# '''
