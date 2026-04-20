
# nombre = "Ana"# esto es una variable con un string
# edad = 25  # esto es una variable con un valor entero
# print(nombre)
# print(edad)

# el INPUT es un método por defecto de pyhton
# nombre = input("Escribe tu nombre: ")
# edad = input("escribe tu edad: ")
# #gustavo edad = int(edad)
# print("el nombre tuyo es: " + " " + nombre)

# edad = int(input("Escribe tu edad: "))
# print(edad + 5)

# Los CONDICIONALES
# if
# edad = 10
# if edad >= 18:
#     print("Eres Mayor de Edad: ")
# else:
#     print("Eres menor de edad")

'''
El if se presenta una instrucción, en el elif se presenta una condicón y en el else sino se cumplen las dos primeras condiciones pasa a la última (else)
'''

# edad = int(input("Escribre tu edad: "))  # variable con el valor edad
# if edad > 18:
#     print("Eres mayor de edad")
# elif edad == 18:
#     print("Tienes justo años")
# else:
#     print("Eres menor de edad")

'''
Operador        Significado
==              igual
!=              distinto
>               mayor que
<               menor que
>=              mayor o igual a que
<=              menor o igual a que

'''
# nombre = "harry"
# if nombre == "Harry":
#     print("¡Harry querido! No te había visto, 30 punto para griffindor")
# elif nombre == "Ron":
#     print("Tu eres...")
# else:
#     print("Troll en las masmorras")
#     print("Harry" == "harry")  # Ojo es key sensitive

# Key sensitive
# nombre = "ron"
# if nombre.upper == "HARRY":
#     print("¡Harry querido! No te había visto, 30 punto para griffindor")
# elif nombre.upper == "RON":
#     print(" Y Tu eres...")
# else:
#     print("Troll en las masmorras")

# Key sensitive la que más se utiliza (LOWER)
# nombre = "HaRrY"
# if nombre.lower == "harry":
#     print("¡Harry querido! No te había visto, 30 punto para griffindor")
# elif nombre.lower == "ron":
#     print(" Y Tu eres...")
# else:
#     print("Troll en las masmorras")

# edad = 20
# tiene_entrada = True
# if edad >= 18 and tiene_entrada:
#     print("Puedes entrar al concierto")
# elif edad >= 18 and not tiene_entrada:
#     print("Eres mayor de edad, pero ")

nombre = input("Nombre: ")
email = input("Email: ")
edad = input("Edad: ")
print("------RESUMEN---------")
print("Nombre:", nombre)
print("Email:", email)
print("Edad:", edad)
confirmacion = input("¿Está todo correcto? (si/no)")
if confirmacion.lower() == "si":
    print("Datos enviados correctamente")
elif confirmacion.lower == "no":
    print("Vuelva a intentarlo")
else:
    print("Lea mejor las opciones, por favor")
