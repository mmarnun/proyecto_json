import os

import json

with open('proyecto.json') as r:
    recetas = json.load(r)

def menu():
    print("Introduce un número para dirigirte a la opción deseada.")
    print("-------------------------------------------------------------------")
    print("1. Listar los nombres de las recetas y sus pasos a seguir")
    print("2. Listar los nombres de las recetas y la cantidad de ingredientes")
    print("3. Mostrar el nombre de la receta en tiempo de elaboración")
    print("4. Ingrediente, tipo y recetas en el que se usa")
    print("5. NOSE")
    print("6. Salir")
    print("-------------------------------------------------------------------")
    opcion = int(input("Opción deseada: "))
    return opcion

def erroropcion():
    os.system("cls")
    print("Error, la opción introducida no es válida, debes introducir una de las opciones existentes en el menú.")
    print()

def opcion1(recetas):
    os.system("cls")
    print("A continuación se muestran los nombres de las recetas y sus pasos a seguir:")
    for receta in recetas:
        print("Receta:", receta["name"])
        print("Pasos a seguir:")
        for i, paso in enumerate(receta["steps"], 1):
            print(i,".", paso)
        print()


