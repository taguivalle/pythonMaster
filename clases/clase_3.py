# para ver el for debemos ver las listas y los diccionarios
# los set y las tuplas no se pueden recorrer con un for, pero si con un while

# listas
# una lista es una colección de elementos ordenados y mutables, que pueden ser de cualquier tipo de dato, y se representan con corchetes [].

# numeros = [1, 2, 3, 4, 5]
# nombres = ["Juan", "María", "Pedro", "Ana"]
# mezcla = [1, "Hola", 3.14, True]
# print(numeros)
# print(numeros[0])  # accedemos al primer elemento de la lista
# print(numeros[1])  # accedemos al segundo elemento de la lista
# print(numeros[-1])  # accedemos al último elemento de la lista
# print(numeros[-2])  # accedemos al penúltimo elemento de la lista
# print(numeros[0:3])  # accedemos a los primeros tres elementos de la lista
# # accedemos a los elementos a partir del tercer elemento de la lista
# print(numeros[2:])
# print(numeros[:3])  # accedemos a los primeros tres elementos de la lista
# print(numeros[::2])  # accedemos a los elementos de la lista
# print(nombres)
# print(mezcla)

# añadir objetos a una lista con el método append()
# numeros = [1, 2, 3, 4, 5]
# numeros.append(6)
# print(numeros)
# numeros.append(7)
# print(numeros)
# numeros.append(8)
# print(numeros)

# el insert() permite insertar un elemento en una posición específica de la lista, y desplaza los elementos a la derecha para hacer espacio para el nuevo elemento.
# numeros.insert(0, 0)  # insertamos el número 0 en la posición 0 de la lista
# print(numeros)
# numeros.insert(3, 2.5)  # insertamos el número 2.5 en la posición 3 de la lista
# print(numeros)
# # insertamos el número 9 en la posición 10 de la lista, pero como la lista tiene solo 9 elementos, el número 9 se inserta al final de la lista
# numeros.insert(10, 9)
# print(numeros)

# eliminar objetos de una lista con el método remove()
# numeros = [1, 2, 3, 4, 5]
# numeros.remove(3)  # eliminamos el número 3 de la lista
# print(numeros)
# numeros.remove(1)  # eliminamos el número 1 de la lista
# print(numeros)
# numeros.remove(5)  # eliminamos el número 5 de la lista
# print(numeros)

# numeros = [1, 2, 3, 4, 5]
# eliminar objetos de una lista con el método pop()
# el método pop() elimina el último elemento de la lista y lo devuelve, pero también se puede especificar un índice para eliminar un elemento específico de la lista.
# print(numeros.pop())  # eliminamos el último elemento de la lista y lo imprimimos
# print(numeros)
# print(numeros.pop(0))  # eliminamos el primer elemento de la lista y lo imprimimos
# print(numeros)
# print(numeros.pop(2))  # eliminamos el tercer elemento de la lista y lo imprimimos
# print(numeros)

# elimminar
# eliminar objetos de una lista con el método clear()
# el método clear() elimina todos los elementos de la lista, dejando una lista vacía.
# numeros = [1, 2, 3, 4, 5]
# numeros.clear()
# print(numeros)

# cambiar el valor de un elemento de una lista
# nombres = ["ana", "maría", "pedro", "ana"]
# # cambiamos el valor del primer elemento de la lista a "juana"
# nombres[0] = "juana"
# print(nombres)
# # cambiamos el valor del tercer elemento de la lista a "luis"
# nombres[2] = "luis"
# print(nombres)
# # cambiamos el valor del último elemento de la lista a "sofía"
# nombres[-1] = "sofía"
# print(nombres)

# las tuplas
# una tupla es una colección de elementos ordenados e inmutables, que pueden ser de cualquier tipo de dato, y se representan con paréntesis ().
# numeros = (1, 2, 3, 4, 5)
# nombres = ("Juan", "María", "Pedro", "Ana")
# mezcla = (1, "Hola", 3.14, True)
# print(numeros)
# print(numeros[0])  # accedemos al primer elemento de la tupla
# print(numeros[1])  # accedemos al segundo elemento de la tupla
# print(numeros[-1])  # accedemos al último elemento de la tupla
# print(numeros[-2])  # accedemos al penúltimo elemento de la tupla
# print(numeros[0:3])  # accedemos a los primeros tres elementos de la tupla
# # accedemos a los elementos a partir del tercer elemento de la tupla
# print(numeros[2:])
# print(numeros[:3])  # accedemos a los primeros tres elementos de la tupla
# print(numeros[::2])  # accedemos a los elementos de la tupla
# print(nombres)
# print(mezcla)

# el set
# un set es una colección de elementos no ordenados, mutables e inmutables, que pueden ser de cualquier tipo de dato, y se representan con llaves {}.
# numeros = {1, 2, 3, 4, 5}
# numeros.add(6)  # añadimos el número 6 al set
# numeros.add(7)  # añadimos el número 7 al set
# numeros.add(8)  # añadimos el número 8 al set
# nombres = {"Juan", "María", "Pedro", "Ana"}
# nombres.add("Luis")  # añadimos el nombre "Luis" al set
# nombres.add("Sofía")  # añadimos el nombre "Sofía" al set
# nombres.add("Carlos")  # añadimos el nombre "Carlos" al set
# mezcla = {1, "Hola", 3.14, True}
# mezcla.add("Adiós")  # añadimos el string "Adiós" al set
# mezcla.add(2.718)  # añadimos el número 2.718 al set
# mezcla.add(False)  # añadimos el booleano False al set
# print(numeros)
# print(nombres)
# print(mezcla)

# Dicionarios
# # un diccionario es una colección de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor correspondiente, y se representan con llaves {}.
# persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
# print(persona)
# # accedemos al valor de la clave "nombre" del diccionario
# print(persona["nombre"])
# print(persona["edad"])  # accedemos al valor de la clave "edad" del diccionario
# # accedemos al valor de la clave "ciudad" del diccionario
# print(persona["ciudad"])
# persona["nombre"] = "María"  # cambiamos el valor de la clave "nombre"
# print(persona)
# persona["edad"] = 25  # cambiamos el valor de la clave "edad"
# print(persona)
# persona["ciudad"] = "Barcelona"  # cambiamos el valor de la clave "ciudad"
# print(persona)

# añadir un nuevo par clave-valor al diccionario
# añadimos el par clave-valor "profesión": "Ingeniero" al diccionario
# persona["profesión"] = "Ingeniero"
# print(persona)
# # añadimos el par clave-valor "hobby": "Fútbol" al diccionario
# persona["hobby"] = "Fútbol"
# print(persona)
# # añadimos el par clave-valor "idioma": "Español" al diccionario
# persona["idioma"] = "Español"
# print(persona)
# # añadimos el par clave-valor "email": "maria@example.com" al diccionario
# persona["email"] = "maria@example.com"
# print(persona)

# for con listas
# los for con listas se utilizan para recorrer cada elemento de una lista y realizar una acción con cada uno de ellos. La sintaxis básica de un for con listas es la siguiente:
# nombres = ["Juan", "María", "Pedro", "Ana"]
# for nombre in nombres:
#     print(nombre)

# for con condicionales
# los for con condicionales se utilizan para recorrer cada elemento de una lista y realizar una acción solo si se cumple una condición específica. La sintaxis básica de un for con condicionales es la siguiente:
# nombres = ["Juan", "María", "Pedro", "Ana"]
# for nombre in nombres:
#     if nombre != "Pedro":
#         print(nombre)

# for con diccionarios
# los for con diccionarios se utilizan para recorrer cada par clave-valor de un diccionario y realizar una acción con cada uno de ellos. La sintaxis básica de un for con diccionarios es la siguiente:
# persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
# for clave, valor in persona.items():
#     print(clave, valor)
# for clave in persona:#el for recorre las claves del diccionario
#     print(persona[clave])
# for valor in persona.values():  # el for recorre los valores del diccionario
#     print(valor)

# for each con set
# los for each con set se utilizan para recorrer cada elemento de un set y realizar una acción con cada uno de ellos. La sintaxis básica de un for each con set es la siguiente:
# numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# for numero in numeros:
#     if numero % 2 == 0:  # si el número es par, lo imprimimos
#         print(numero)

# for con while
# los for con while se utilizan para recorrer cada elemento de una lista o un diccionario utilizando un índice o una clave, y realizar una acción con cada uno de ellos. La sintaxis básica de un for con while es la siguiente:
# numeros = [1, 2, 3, 4, 5]
# i = 0
# while i < len(numeros):
#     print(numeros[i])
#     i += 1
# persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
# # obtenemos una lista de las claves del diccionario
# claves = list(persona.keys())
# i = 0
# while i < len(claves):
#     clave = claves[i]  # obtenemos la clave actual
#     valor = persona[clave]  # obtenemos el valor correspondiente a la clave
#     print(clave, valor)  # imprimimos la clave y su valor
#     i += 1

# for con tuplas
# los for con tuplas se utilizan para recorrer cada elemento de una tupla y realizar una acción con cada uno de ellos. La sintaxis básica de un for con tuplas es la siguiente:
# numeros = (1, 2, 3, 4, 5)
# for numero in numeros:
#     print(numero)

# ocntrol de flujo con for
# los for con control de flujo se utilizan para recorrer cada elemento de una lista o un diccionario y realizar una acción solo si se cumple una condición específica, utilizando las palabras clave if, elif y else. La sintaxis básica de un for con control de flujo es la siguiente:
# numeros = [1, 2, 3, 4, 5]
# for numero in numeros:
#     if numero % 2 == 0:  # si el número es par, lo imprimimos
#         print(f"{numero} es par")
#     else:  # si el número es impar, lo imprimimos
#         print(f"{numero} es impar")

# ejercicio: crear una lista de invitados para una fiesta, donde el usuario ingrese la cantidad de invitados y luego ingrese el nombre de cada invitado, y al final se imprima la lista de invitados.
cantidad = int(input("Ingrese la cantidad de invitados que desea ingresar: "))
invitados = []
# el range(cantidad) genera una secuencia de números desde 0 hasta cantidad-1, que se utiliza para iterar el número de veces que el usuario ha especificado.
# for i in range(cantidad):
#     nombre = input(f"Ingrese el nombre del invitado {i + 1}: ")
#     invitados.append(nombre)
# print("La lista de invitados es:")
# revisar = input("¿Desea revisar la lista de invitados? (s/n): ")
# if revisar.lower() == "s":
#     for nombre in invitados:
#         print(nombre)
# decision = input("¿Enviar lista o repasar lista? (enviar/repasar): ").lower()
# if decision == "enviar":
#     print("La lista de invitados ha sido enviada.")
# elif decision == "repasar":
#     print("Repasando la lista de invitados:")
#     for nombre in invitados:
#         print(nombre)
# else:
#     print("Opción no válida. No se ha enviado ni repasado la lista de invitados.")
