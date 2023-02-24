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

def opcion2(recetas):
    os.system("cls")
    print("A continuación se muestran los nombres de las recetas y cuanto ingredientes tienen:")
    for receta in recetas:
        print("Receta:", receta["name"])
        print("Cantidad de ingredientes:", len(receta["ingredients"]))
        print()

def opcion3(recetas):
    print()
    tiempo1 = int(input("Introduce un primer valor mínimo (en minutos): "))
    tiempo2 = int(input("Introduce un segundo valor máximo (en minutos): "))
    flag = True
    for receta in recetas:
        duracion = sum(receta["timers"])
        if tiempo1 <= duracion <= tiempo2:
            print(receta["name"])
            flag = True
        else:
            flag = False
    if flag == False:
        print("No hay recetas que duren entre el intervalo de tiempo intro")


def opcion4(recetas):
    print()
    ingrediente = input("Introduce un ingrediente (en inglés): ")
    recetas_con_ingrediente = []
    for receta in recetas:
        for i in receta["ingredients"]:
            if i["name"].lower() == ingrediente.lower():
                if ingrediente.lower() not in recetas_con_ingrediente:
                    recetas_con_ingrediente.append(receta["name"])
                print("-",ingrediente,"es un ingrediente de tipo",i['type'],"y se utiliza en la receta:",receta['name'])
    if not recetas_con_ingrediente:
        print("No se encontraron recetas con el ingrediente:",ingrediente)
    print()


