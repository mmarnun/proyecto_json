from funciones import *
print("Bienvenida al menú del libro de recetas.")
opcion = menu()
while opcion != 6:
    if opcion == 1:
        opcion1(recetas)
    elif opcion == 2:
        opcion2()
    elif opcion == 3:
        opcion3()
    elif opcion == 4:
        opcion4()
    elif opcion == 5:
        opcion5()
    else:
        erroropcion()
    opcion = menu()