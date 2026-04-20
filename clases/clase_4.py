# los métodos son funciones que se definen dentro de una clase y que operan sobre los objetos de esa clase.
# se definen con la palabra clave "def" seguida del nombre del método y paréntesis que pueden contener parámetros.
# el primer parámetro de un método es siempre "self", que hace referencia al objeto actual de la clase. Esto permite que el método acceda a los atributos y otros métodos del objeto.
# los métodos pueden realizar diversas operaciones, como modificar los atributos del objeto, realizar cálculos o devolver valores.
# aquí hay un ejemplo de una clase con un método:

# el sigueinte es un método vacío, es decir, no hace nada. Se utiliza como un marcador de posición para indicar que se implementará en el futuro.

# print("Ejemplo de clase con método")
# print("Ejemplo de clase con método")
# print("Ejemplo de clase con método")
# print("Ejemplo de clase con método")

# BANDERA
# def saludar():
#     print("¡Hola! Bienvenido a la clase de Python.")
#     saludar()
#     saludar()
#     saludar()
#     saludar()

# el siguiente es un método que recibe un parámetro "nombre" y lo utiliza para personalizar el saludo. Al llamar a este método con diferentes nombres, se puede obtener un saludo personalizado para cada persona.
# def saludar(nombre):
#     print("¡Hola", nombre, "! Bienvenido(a) a la clase de Python.")

# saludar("Juan")
# saludar("María")
# saludar("Carlos")
# saludar("Ana")

# el siguiente es un método que devuelve un valor. En este caso, el método "sumar" recibe dos números como parámetros y devuelve su suma. Al llamar a este método con diferentes números, se puede obtener la suma de esos números.
# def sumar(a, b):
#     return a + b
# resultado1 = sumar(5, 3)
# resultado2 = sumar(10, 7)
# resultado3 = sumar(-2, 4)
# print("La suma de 5 y 3 es:", resultado1)
# print("La suma de 10 y 7 es:", resultado2)
# print("La suma de -2 y 4 es:", resultado3)

# el siguiente es un método que utiliza una estructura de control de flujo (if-else) para determinar si una persona es mayor de edad o no. El método "es_mayor_de_edad" recibe la edad como parámetro y devuelve True si la edad es mayor o igual a 18, y False en caso contrario. Al llamar a este método con diferentes edades, se puede determinar si cada persona es mayor de edad o no.
# def es_mayor_de_edad(edad):
#     if edad >= 18:
#         return True
#     else:
#         return False
# también se puede escribir de manera más concisa utilizando una expresión booleana; los print serían los mismos, pero el método se vería así:
# return edad >= 18 entre el if y el else, ya que la expresión "edad >= 18" ya devuelve un valor booleano (True o False) dependiendo de si la condición se cumple o no.
# print("¿Es Juan mayor de edad?", es_mayor_de_edad(20))
# print("¿Es María mayor de edad?", es_mayor_de_edad(17))
# print("¿Es Carlos mayor de edad?", es_mayor_de_edad(18))
# print("¿Es Ana mayor de edad?", es_mayor_de_edad(15))

# el siguiente es un método que recibe una lista como parámetro y muestra cada elemento de la lista en una línea separada. Al llamar a este método con diferentes listas, se puede mostrar el contenido de esas listas de manera organizada.
# def mostrar_lista(lista):
#     for elemento in lista:
#         print(elemento)
# nombres = ["Juan", "María", "Carlos", "Ana"]
# mostrar_lista(nombres)
# apellidos = ["Pérez", "Gómez", "López", "Sánchez"]
# mostrar_lista(apellidos)
# telefono = [12356789, 25489256, 345678901, 456789101, 567894561]
# mostrar_lista(telefono)
# direcciones = ["Calle 123", "Avenida 456", "Plaza 789", "Camino 101"]
# mostrar_lista(direcciones)
# frutas = ["Manzana", "Banana", "Naranja", "Uva"]
# mostrar_lista(frutas)

# el siguiente es un método que recibe un texto y una palabra como parámetros y determina si la palabra está presente en el texto. El método "contiene_palabra" convierte tanto el texto como la palabra a minúsculas para hacer una comparación insensible a mayúsculas. Luego, utiliza el operador "in" para verificar si la palabra está en el texto y devuelve True o False según corresponda. Al llamar a este método con diferentes textos y palabras, se puede verificar si cada palabra está presente en su respectivo texto.

# def contiene_palabra(texto, palabra):
#     texto = texto.lower()
#     palabra = palabra.lower()
#     if palabra in texto:
#         return True
# también se puede escribir de manera más concisa utilizando una expresión booleana; los print serían los mismos, pero el método se vería así:
# return False
# return palabra in texto (este retur debe de estar a nivel del if, no dentro de él, ya que la expresión "palabra in texto" ya devuelve un valor booleano (True o False) dependiendo de si la condición se cumple o no).


# frase = "El perro está en el jardín"
# print("¿La frase contiene la palabra 'perro'?",
#       contiene_palabra(frase, "perro"))
# print("¿La frase contiene la palabra 'gato'?",
#       contiene_palabra(frase, "Mapache"))
# print("¿La frase contiene la palabra 'jardín'?",
#       contiene_palabra(frase, "jardín"))
# print("¿La frase contiene la palabra 'casa'?", contiene_palabra(frase, "CASÁ"))
# print("¿La frase contiene la palabra 'árbol'?",
#       contiene_palabra(frase, "Pimienta"))

# def reemplazar_palabra(texto, palabra_vieja, palabra_nueva):
#     return texto.replace(palabra_vieja, palabra_nueva, 2)  # el número 2 indica que solo se reemplazarán las primeras dos ocurrencias de la palabra vieja en el texto. Si se omite este número, se reemplazarán todas las ocurrencias de la palabra vieja en el texto.

# frase = "El mago lanza un hechizo y lanza un hechizo más"
# print(reemplazar_palabra(frase, "hechizo", "conjuro"))
# print(reemplazar_palabra(frase, "castillo", "torre"))
# print(reemplazar_palabra(frase, "hechizo", "conjuro"))
# print(reemplazar_palabra(frase, "lanza", "arroja"))
# print(reemplazar_palabra(frase, "está", "se encuentra"))

# BANDERA
# encontrar el último valor de una palabra en un texto
# def reeemplazar_ultimo(texto, vieja, nueva):
#     partes = texto.rsplit(vieja, 1)  # este método rsplit divide el texto en partes utilizando la palabra vieja como separador, pero solo lo hace una vez desde el final del texto. Esto significa que si la palabra vieja aparece varias veces en el texto, solo se dividirá en la última ocurrencia de esa palabra.
#     if len(partes) == 2:
#         return partes[0] + nueva + partes[1]
#     else:
#         return texto  # si la palabra no se encuentra en el texto, se devuelve el texto original sin cambios.
#     frase = "El mago lanza un hechizo y otro hechizo más"
#     print(reeemplazar_ultimo(frase, "hechizo", "conjuro"))

# LISTAS DINÁMICAS
# rellenar una lista con datos ingresados por el usuario utilizando un método. El método "rellenar_lista" solicita al usuario la cantidad de elementos que desea agregar a la lista y luego utiliza un bucle para pedir al usuario que ingrese cada elemento. Cada elemento ingresado se agrega a la lista utilizando el método "append". Finalmente, el método devuelve la lista completa con los elementos ingresados por el usuario.
# def rellenar_lista():
#     lista = []
#     cantidad = int(input("¿Cuántos elementos deseas agregar a la lista? "))
#     for i in range(cantidad):
#         valor = input("Elemento: ")
#         lista.append(valor)
#     return lista
# datos = rellenar_lista()
# print("Los elementos de la lista son:")
# for elemento in datos:
#     print(elemento)

# lista con el metodo "set" para eliminar elementos duplicados. El método "lista_a_set" recibe una lista como parámetro y utiliza el método "set" para convertirla en un conjunto, lo que automáticamente elimina los elementos duplicados. Al llamar a este método con una lista que contiene elementos repetidos, se obtendrá un conjunto con solo los elementos únicos de esa lista.
# def lista_a_set(lista):
#     return set(lista)  # el método "set" convierte la lista en un conjunto, lo que elimina automáticamente los elementos duplicados. Al llamar a este método con una lista que contiene elementos repetidos, se obtendrá un conjunto con solo los elementos únicos de esa lista.
# numeros = [1, 2, 3, 3, 4, 5, 2, 3, 6, 6, 7, 8, 9, 9, 10]
# numeros_unicos = lista_a_set(numeros)
# print("Números únicos:", numeros_unicos)

# Eliminar los elementos duplicados de una lista sin utilizar el método "set". El método "eliminar_duplicados" recibe una lista como parámetro y crea una nueva lista llamada "lista_sin_duplicados". Luego, utiliza un bucle para iterar sobre cada elemento de la lista original y verifica si ese elemento ya está presente en la nueva lista. Si el elemento no está presente, se agrega a la nueva lista. Finalmente, el método devuelve la lista sin duplicados.
# def eliminar_duplicados(lista):
#     lista_sin_duplicados = []
#     for elemento in lista:
#         if elemento not in lista_sin_duplicados:
#             lista_sin_duplicados.append(elemento)
#     return lista_sin_duplicados
# print("Ejemplo de lista con elementos duplicados:")
# numeros = [1, 2, 3, 3, 4, 5, 2, 3, 6, 6, 7, 8, 9, 9, 10]
# print(numeros)
# numeros_sin_duplicados = eliminar_duplicados(numeros)
# print("Lista sin elementos duplicados:")
# print(numeros_sin_duplicados)


# def limpiar_texto(texto):
# texto = texto.replace(" ", "")  # eliminar espacios
# texto = texto.replace("\n", "")  # eliminar saltos de línea
# texto = texto.replace("\t", "")  # eliminar tabulaciones
# texto = texto.strip()  # eliminar espacios al inicio y al final del texto
# texto = texto.lower()  # convertir a minúsculas
# texto = texto.upper()  # convertir a mayúsculas
#     return texto
# print(limpiar_texto("   Hola, este es un texto de ejemplo.   \n\t"))


def guardar_list_txt(lista):
    archivo = open("./archivos/datos.txt", "w")  # el método "open" se utiliza para abrir un archivo. El primer parámetro es el nombre del archivo (en este caso, "datos.txt") y el segundo parámetro es el modo de apertura ("w" para escritura, lo que significa que se creará un nuevo archivo o se sobrescribirá uno existente).

    for elemento in lista:
        archivo.write(elemento + "\n")  # el método "write" se utiliza para escribir en el archivo. En este caso, se escribe cada elemento de la lista seguido de un salto de línea ("\n") para que cada elemento aparezca en una línea separada en el archivo.
    archivo.close()  # el método "close" se utiliza para cerrar el archivo después de haber terminado de escribir en él. Es importante cerrar el archivo para liberar los recursos del sistema y asegurarse de que los datos se guarden correctamente.
guardar_list_txt(["Juan", "María", "Carlos", "Ana"])
        