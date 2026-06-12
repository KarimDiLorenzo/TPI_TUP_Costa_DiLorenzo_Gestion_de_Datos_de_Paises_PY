from fn import * 
import csv
while True:
    menu()
    opcion = validar_num("Selecciona una opción del menú: ")

    match opcion:
        case 1 | "1":
            pass
        case 2 | "2":
            archivo = "paises.csv"
            actualizar_pais(archivo)
        case 3 | "3":
            pass
        case 4 | "4":
            pass
        case 5 | "5":
            pass
        case 6 | "6":
            pass
        case 7 | "7":
            print("Gracias por usar el sistema!")
            break
        case _:
            print("Ingresa un número del menú")
    