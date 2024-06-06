def ingrese_nombre_archivo(mensaje:str)->str:
    """Nos pide ingresar una cadena que sera el nombre de un archivo

    Args:
        mensaje (str): Mensaje para mostrar por consola
    Returns:
        str: nombre del archivo
    """
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
    """Nos pide que ingresemos una cadena , la valida y le establece un formato especifico

    Args:
        mensaje (str): mensaje de lo que queremos pedir

    Returns:
        str: cadena validada
    """
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
    """Valida que una cadena sea de tipo string y le aplica un formato

    Args:
        dato (str): cadena a validar

    Raises:
        TypeError: Si hay error lanzara una excepcion

    Returns:
        str: dato validado
    """
    if type(dato) == str:
        if len(dato) > 0:
            dato = dato.lower().capitalize()
        else:
            dato = "No Tiene"
    else:
        raise TypeError("Esto no es un String!!!")
    return dato

def validar_int(dato:str)->int:
    """Valida que una cadena sea un numero de tipo entero y lo convierte en uno

    Args:
        dato (str): dato a validar

    Raises:
        TypeError: si hay un error lanzara uan excepcion

    Returns:
        int: dato validado
    """
    if type(dato) != int:
        if dato.isdigit():
            dato = int(dato)
        else:
            raise TypeError("Esto no es un numero entero!!!")
    return dato


def validar_float(dato:str)->float:
    """Valida que una cadena sea un numero de tipo flotante y lo convierte en uno

    Args:
        dato (str): dato a validar

    Raises:
        TypeError: si hay un error lanzara uan excepcion

    Returns:
        int: dato validado
    """
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
    """Muestra los datos cargados en la lista de peliculas

    Args:
        lista (list): lista con los datos de las peliculas
    """
    from os import system
    mostrar_tabla("LISTA PELICUAS")
    for dato in lista:
        print(f"{dato['id']:<5} {dato['titulo']:<30} {dato['genero']:<20} {dato['rating']:0.1f}")
    system("pause")
    system("cls")


def cargar_flotante_random(desde,hasta)->float:
    """Genera un numero flotante random entre cierto rango 

    Args:
        desde (_type_): rango minimo
        hasta (bool): rango maximo
    Returns:
        _type_: numero entero random
    """
    from random import uniform
    numero = uniform(desde,hasta)
    return float(f"{numero:0.1f}")

def cargar_enteros_random(desde,hasta)->int:
    """Genera un numero entero random entre cierto rango 

    Args:
        desde (_type_): rango minimo
        hasta (bool): rango maximo
    Returns:
        _type_: numero entero random
    """
    from random import randint
    return randint(desde,hasta)


def agregar_rating(lista:list,funcion):
    """Agrega el rating a las peliculas de la lista de forma aleatoria

    Args:
        lista (list): lista de peliculas
        funcion (_type_): funcion para agregar numeros random flotantes

    Raises:
        ValueError: si la lista se encuentra vacia lanzara una excepcion
    """
    if len(lista) > 0:
        for dato in lista:
            dato['rating'] = funcion(1,10)
        mostrar_mensajes("Rating Cargado con exito!!!")
    else:
        raise ValueError("Lista Vacia!!!")

def agregar_genero(lista:list,generos:list,funcion):
    """Agrega el genero a las peliculas de la lista de forma aleatoria

    Args:
        lista (list): lista de peliculas
        generos (list): Lista de generos
        funcion (_type_): funcion para agregar numeros random enteros

    Raises:
        ValueError: si la lista se encuentra vacia lanzara una excepcion
    """
    if len(lista) > 0:
        for dato in lista:
            valor = funcion(0,3)
            dato["genero"] = generos[valor]
        mostrar_mensajes("Generos Cargado con exito!!!")
    else:
        raise ValueError("Lista Vacia!!!")

def crear_csv_genero(path:str,lista:list,genero:str):
    """Crea un archivo csv que contiene solo las pelicuas de un genero en especifico

    Args:
        path (str): direccion donde se guardara el archivo
        lista (list): lista de peliculas
        genero (str): genero de las peliculas que vamos a guardar
    """
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
    """Pide que ingresemos un genero y valida que ese genero exista en la lista de peliculas

    Args:
        lista (list): lista de peliculas

    Returns:
        _type_: retorna el genero que escribio el usuario
    """
    while True:
        valor = ingrese_cadena("Ingrese Genero : ")
        for dato in lista:
            if dato["genero"] == valor:
                return valor
        mostrar_mensajes("Este genero no existe!!!!")


def ordenar_peliculas(lista:list,clave:str):
    """Ordena la lista de peliculas por un campo y si su campo es igual las ordena por rating de forma descendente

    Args:
        lista (list): lista de peliculas
        clave (str): campo por el cual queremos ordenar
    """
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
    """Busca un valor maximo dentro de una lista de diccionarios

    Args:
        lista (list): lista de peliculas
        clave (str): campo por el cual queremos buscar el maximo

    Returns:
        _type_: valor maximo encontrado
    """
    bandera = True
    for dato in lista:
        if bandera == True or dato[clave] > valor_maximo:
            valor_maximo = dato[clave]
            bandera = False
    return valor_maximo

def obtener_mejor_rating(lista:list):
    """Busca la o las peliculas con mayor rating y las muestra por consola

    Args:
        lista (list): lista de peliculas
    """
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
    """Guarda un archivo .Json que contendra la lista de peliculas ordenada por genero y rating

    Args:
        path (str): direccion donde se guardara el archivo
        lista (list): lista de peliculas
    """
    import json
    with open(path,"w",encoding="utf-8") as archivo:
        json.dump(lista,archivo,indent=4)
    mostrar_mensajes("Archivo generado con exito!!!")


