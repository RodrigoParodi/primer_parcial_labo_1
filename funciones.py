def ingrese_nombre_archivo(mensaje:str)->str:
    from os import system
    system("cls")

    while True:
        entrada = input(mensaje)
        if entrada.isalpha():
            cadena = entrada
            break
        else:
            mostrar_mensajes("Error, Cadena invalida!!!")
    return cadena

def ingrese_cadena(mensaje:str)->str:
    from os import system
    system("cls")

    while True:
        entrada = input(mensaje)
        if entrada.isalpha():
            cadena = entrada.lower().capitalize()
            break
        else:
            mostrar_mensajes("Error, Cadena invalida!!!")
    return cadena


def mostrar_mensajes(mensaje):
    """limpia la consola y muestra un mensaje especifico

    Args:
        mensaje (_type_): Mensaje que quiero mostrar
    """
    from os import system
    system("cls")
    print(mensaje)
    system("pause")


def mostrar_menu(lista_menu:list)->list:
    """Imprimira por consola un menu de opciones

    Args:
        lista_menu (list): Lista que debe contener las opciones a mostrar del menu

    Returns:
        _type_: Devuelve la opcion escogida por el usuario
    """
    from os import system
    for opcion in lista_menu:
        print(opcion)
    opcion = input("Ingrese una opcion : ")
    system("cls")
    return opcion


def obtener_path(nombre_archivo:str,dominio:str)->str:
    """Obtiene la ruta actual donde se encuentra la carpeta principal

    Args:
        nombre_archivo (str): Nombre del archivo

    Returns:
        _type_: devuelve un string con el path completo
    """
    import os
    path_acutal = os.path.dirname(__file__)
    nombre_archivo = f"archivos/{nombre_archivo}.{dominio}"
    return os.path.join(path_acutal, nombre_archivo)


def cargar_csv(path:str)->list:
    """carga los datos guardados en un archivo csv y los guarda en una lista.

    Args:
        path (str): Direccion donde se encuentra el archivo

    Returns:
        list: lista con los datos del archivo
    """
    with open(path,"r",encoding="utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")

        for linea in archivo.readlines():
            pelicula = {}
            linea = linea.strip("\n").split(",")
            
            id,titulo,genero,rating = linea

            pelicula["id"] = validar_int(id)
            pelicula["titulo"] = validar_str(titulo)
            pelicula["genero"] = validar_str(genero)
            pelicula["rating"] = validar_float(rating)
            lista.append(pelicula)
    return lista

def validar_str(dato:str)->str:
    if type(dato) == str:
        if len(dato) > 0:
            dato = dato.lower().capitalize()
        else:
            dato = "No Tiene"
    else:
        raise TypeError("Esto no es un String!!!")
    return dato

def validar_int(dato:str)->int:
    if type(dato) != int:
        if dato.isdigit():
            dato = int(dato)
        else:
            raise TypeError("Esto no es un numero entero!!!")
    return dato


def validar_float(dato:str)->float:
    if type(dato) != float:
        if dato.replace('.', '').isdigit() == True:
            dato = float(dato)
        else:
            raise TypeError("Esto no es un numero flotante!!!")
    return dato

def mostrar_tabla(titulo:str):
    """Muestra una tabla

    Args:
        titulo (str): encabezado de la tabla
    """
    print(f"                           ***{titulo}***\n")
    print(" id     titulo                      Genero               Rating  ")
    print("-------------------------------------------------------------------")

def mostrar_datos(lista:list):
    from os import system
    mostrar_tabla("DATOS LISTA")
    for dato in lista:
        print(f"{dato['id']:<5} {dato['titulo']:<30} {dato['genero']:<20} {dato['rating']:0.1f}")
    system("pause")
    system("cls")


def cargar_flotante_random(desde,hasta):
    from random import uniform
    return  uniform(desde,hasta)

def cargar_enteros_random(desde,hasta):
    from random import randint
    return randint(desde,hasta)


def agregar_rating(lista:list,funcion):
    if len(lista) > 0:
        for dato in lista:
            dato['rating'] = funcion(1,10)
        mostrar_mensajes("Rating Cargado con exito!!!")
    else:
        raise ValueError("Lista Vacia!!!")

def agregar_genero(lista:list,generos:list,funcion):
    if len(lista) > 0:
        for dato in lista:
            valor = funcion(0,3)
            dato["genero"] = generos[valor]
        mostrar_mensajes("Generos Cargado con exito!!!")
    else:
        raise ValueError("Lista Vacia!!!")

def crear_csv_genero(path:str,lista:list,genero:str):
    with open(path,"w",encoding="utf-8") as archivo:
        keys = list(lista[0].keys())
        encabezado = ",".join(keys) + "\n"
        archivo.write(encabezado)

        for dato in lista:
            if dato["genero"] == genero:
                mensaje = f"{dato['id']},{dato['titulo']},{dato['genero']},{dato['rating']:0.1f}\n"
                archivo.write(mensaje)
    mostrar_mensajes("Archivo generado con exito!!!")

def pedir_genero(lista:list):

    while True:
        valor = ingrese_cadena("Ingrese Genero : ")
        for dato in lista:
            if dato["genero"] == valor:
                return valor
        mostrar_mensajes("Este genero no existe!!!!")



def ordenar_peliculas(lista:list,clave:str)->list:
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][clave] > lista[j][clave] :
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            elif lista[i][clave] == lista[j][clave]:
                if lista[i]["rating"] < lista[j]["rating"]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

def buscar_maximo(lista:list,clave:str):
    bandera = True
    for dato in lista:
        if bandera == True or dato[clave] > valor_maximo:
            valor_maximo = dato[clave]
            bandera = False
    return valor_maximo

def obtener_mejor_rating(lista:list):
    from os import system
    mejor_rating = buscar_maximo(lista,"rating")
    print("\n        *** PELICULA MEJOR RATING ***\n")
    print(" NOMBRE                      RATING")
    for dato in lista:
        if dato["rating"] == mejor_rating:
            print(f"{dato['titulo']:<30} {dato['rating']:0.1f}")
    system("pause")
    system("cls")

def guardar_json(path:str,lista:list):
    import json
    with open(path,"w",encoding="utf-8") as archivo:
        json.dump(lista,archivo,indent=4)
    mostrar_mensajes("Archivo generado con exito!!!")




