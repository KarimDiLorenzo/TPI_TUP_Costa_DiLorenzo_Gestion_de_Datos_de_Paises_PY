import csv
def menu():
    print('''
    1) Agregar país
    2) Actualizar datos de un país
    3) Buscar pais
    4) Filtrar países
    5) Ordenar paises 
    6) Mostrar estadísticas
    7) Salir 
    ''')

def validar_num(valor): #Función validadora de la opción del menú (que sea un número > 0)
    while True:
        try:
            num = int(input(valor))
            if num >0:
                return num
            else:
                print("ERROR: Ingresa un número positivo \n")
        except ValueError:
            print("ERROR: Ingresa un número \n")

def validar_str(mensaje): #Función validadora de strings (verifica que el nómbre sea válido)
    while True: 
        try:
            cadena = input(mensaje).strip().capitalize()
            if cadena.isalpha():
                return cadena
            else:
                print("ERROR - No puede ser vacío \n")
        except TypeError:
            print("ERROR - Ingresa solo texto \n")



def actualizar_pais(paises): 
    buscado = validar_str("Qué país querés modificar?: ")
    with open(paises, "r", encoding = "utf-8", newline = "") as archivo:
        lector = csv.DictReader(archivo) 
        datos = list(lector)
        encabezados = lector.fieldnames
    for p in datos:
        if p["nombre"] == buscado:
            p["poblacion"] = validar_num("Ingresá la población actualiada: ")
            p["superficie"] = validar_num("Ingresa la superficie actualizada:")
    
    with open(paises, "r+", encoding = "utf-8", newline = "") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(datos)
    for p in datos:
        if p["nombre"] == buscado:
            print(f"País actualizado - {buscado}  Población - {p['poblacion']}  Superficie - {p['superficie']}")