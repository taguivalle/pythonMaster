# bucle while

# este bucle se ejecuta mientras la condicion sea verdadera
# print("Contador con while")
# print("Contador con while")

# print("Contador con while")

# print("Contador con while")
# print("Contador con while")
# print(("Hola Contador con while") * 5)

# este bloque es la forma correcta de escribir un bucle while
# contador = 0
# while contador < 5:
#     print("Hola Contador con while")
#     # este blucle se ejecuta mientras la condicion sea verdadera, en este caso mientras el contador sea menor a 5
#     contador = contador + 1
#     # contador += 1 es lo mismo que contador = contador + 1
#     contador += 1

# este es un bucle infinito, se ejecuta para siempre
# while True:
#     print("Hola Contador con while")

# contador = 0
# while contador < 5:
#     print("Hola Contador con while")
#     contador += 1

# formateado el codigo para que sea mas legible
# contador = 0
# ejemplo = "Hola soy un Contador con while"
# while contador < 5:
#     print(f"Me voy a parar aviso numero: {contador} {ejemplo}")
#     contador += 1
#     # en este ejemplo se altera el valor de la variable ejemplo dentro del bucle, lo que hace que cada vez que se imprima el mensaje, se muestre el valor actualizado de contador
#     ejemplo = "Hola soy un Contador con while" + str(contador)
#     # con el break se sale del bucle, en este caso se sale cuando el contador es igual a 3
#     break

# este es un ejemplo de caja negra, en la que tiene una función que lleva funcionando muchos años y no se sabe como funciona por dentro, pero se sabe que funciona correctamente, entonces se puede usar esa función sin necesidad de saber como funciona por dentro

# este bloque es un while pero con marcha atrás, es decir, se va restando el valor de la variable temporizador hasta que llegue a 0, en ese momento se imprime el mensaje "¡Tiempo terminado!"
# temporizador = 5
# while temporizador > 0:
#     print(f"Temporizador: {temporizador}")
#     temporizador -= 1
# print("¡Tiempo terminado!")

# otro ejemplo de bucle while, que se va repetiendo hasta que el usuario escriba "salir", en ese momento se imprime el mensaje "¡Programa terminado!"no
# respuesta = ""
# while respuesta.lower() != "out":
#     respuesta = input("Escribe 'out' para terminar el programa: ")
#     print(f"Has escrito: {respuesta}")
# print("¡Programa terminado!")

# este bucle con numeros
# edad = -1
# while edad < 0 or edad > 100:
#     edad = int(input("Introduce tu edad: "))
#     if edad < 0:
#         print("La edad no puede ser negativa, por favor introduce un valor válido.")
#     elif edad > 100:
#         print("La edad no puede ser mayor a 100, por favor introduce un valor válido.")
# print(f"Tu edad es: {edad}")

# en el siguiente bloque se muestra un ejemplo para que el usuario introduzca el valor que debe ser (null), en este caso se pide el nombre del usuario, y se muestra un mensaje de error si el usuario no introduce un valor válido (en este caso, un valor vacío)
# nombre = ""
# while nombre == "":
#     nombre = input("Introduce tu nombre: ")
#     if nombre == "":
#         print("El nombre no puede estar vacío, por favor introduce un valor válido.")
# print(f"Tu nombre es: {nombre}") # la letra f es de formatear el mensaje, lo que permite incluir variables dentro del mensaje de forma más legible y fácil de escribir.

# en este bloque se presenta un formulario para que el usuario introduzca su nombre, email y edad, y luego se muestra un resumen de los datos introducidos, y se pide una confirmación para enviar los datos, si el usuario confirma que los datos son correctos, se muestra un mensaje de éxito, si el usuario confirma que los datos no son correctos, se muestra un mensaje de error, y si el usuario introduce una opción no válida, se muestra un mensaje de error.


# confirmacion = "no"

# while confirmacion.lower() != "si":

#     nombre = input("Nombre: ")
#     email = input("Email: ")
#     edad = input("Edad: ")

#     print("------RESUMEN---------")
#     print("Nombre:", nombre)
#     print("Email:", email)
#     print("Edad:", edad)

#     confirmacion = input("¿Está todo correcto? (si/no)")
#     print("Datos enviados correctamente")
#     print("¡Gracias por completar el formulario!")

# confirmacion = "no"

# while confirmacion.lower() != "si":

#     nombre = input("Nombre: ")
#     email = input("Email: ")
#     edad = input("Edad: ")

#     print("------RESUMEN---------")
#     print("Nombre:", nombre)
#     print("Email:", email)
#     print("Edad:", edad)

#     confirmacion = input("¿Está todo correcto? (si/no)")
#     print("Datos enviados correctamente")
#     print("¡Gracias por completar el formulario!")


# correcto = False

# while not correcto:

#     nombre = input("Nombre: ")
#     email = input("Email: ")
#     edad = input("Edad: ")

#     print("------RESUMEN---------")
#     print("Nombre:", nombre)
#     print("Email:", email)
#     print("Edad:", edad)

#     confirmacion = input("¿Está todo correcto? (si/no): ")

#     if confirmacion.lower() == "si":
#         correcto = True
#         print("Datos enviados correctamente")

# anidaciones dentro de un bucle while

# confirmacion = "no"
# while confirmacion.lower() != "si":

#     nombre = input("Nombre: ")
#     email = input("Email: ")
#     edad = input("Edad: ")

#     print("------RESUMEN---------")
#     print("Nombre:", nombre)
#     print("Email:", email)
#     print("Edad:", edad)

#     confirmacion = input("¿Está todo correcto? (si/no): ")

#     if confirmacion.lower() == "si":
#         print("Datos enviados correctamente")
#         print("¡Gracias por completar el formulario!")

# contador para utilizar en contraseñas
contador = 0
while contador < 3:
    contraseña = input("Introduce la contraseña: ")
    if contraseña == "contraseña123":
        print("Contraseña correcta, acceso concedido.")
        # break
        contador = 3
    else:
        print("Contraseña incorrecta, intenta de nuevo.")
        contador += 1
print("Has agotado tus intentos, acceso denegado.")
