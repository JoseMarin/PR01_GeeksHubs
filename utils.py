# Entorno de variables

def presentacion():
    saludo = "Bienvenido al curso de Python >>>>>>>>>>>>>>>>>>>>>>>>>>>>>--------------------------"
    print(saludo)

    nombre = input("¿Como te llamas?")
    print("Encantado de conocerte " + nombre)

    edad = input("¿Que edad tienes?")

    if int(edad) >= 18:
        print("Ya te puesdes sacar el carnet de conducir")
    else:
        print("Aun no puedes conducir")