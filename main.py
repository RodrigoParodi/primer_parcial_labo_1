from funciones import *

lista_peliculas = []

menu = ["\n          *** MENU DE OPCIONES ***\n","1)Cargar archivo csv","2)Imprimir lista",
        "3)Asignar Rating","4)Asignar Genero","5)Filtrar por genero","6)Ordenar Peliculas","7)Informar mejor rating",
        "8)Guardar Peliculas","9)Salir"]

generos = ["Accion","Drama","Comedia","Terror"]

bandera = False
bandera_dos = False
bandera_tres = False

try:
    while True:
        match mostrar_menu(menu):
            case "1":
                nombre_archivo = ingrese_nombre_archivo("Ingrese el nombre del archivo (sin el .csv) : ")
                lista_peliculas = cargar_csv(obtener_path(nombre_archivo,"csv"))
                bandera = True
            case "2":
                if bandera == True:
                    mostrar_datos(lista_peliculas)
                else:
                    mostrar_mensajes("Error , Primero debes cargar los datos del archivo CSV!!!")
            case "3":
                if bandera == True:
                    agregar_rating(lista_peliculas,cargar_flotante_random)
                    bandera_tres = True
                else:
                    mostrar_mensajes("Error , Primero debes cargar los datos del archivo CSV!!!")
            case "4":
                if bandera == True:
                    agregar_genero(lista_peliculas,generos,cargar_enteros_random)
                    bandera_dos = True
                else:
                    mostrar_mensajes("Error , Primero debes cargar los datos del archivo CSV!!!")
            case "5":
                if bandera_dos == True:
                    valor_genero = pedir_genero(lista_peliculas)
                    crear_csv_genero(obtener_path(valor_genero,"csv"),lista_peliculas,valor_genero)
                else:
                    mostrar_mensajes("Error , Primero debes cargar los generos de las peliculas!!!")
            case "6":
                if bandera_dos == True and bandera_tres == True:
                    ordenar_peliculas(lista_peliculas,"genero")
                    mostrar_datos(lista_peliculas)
                else:
                    mostrar_mensajes("Error , Primero debes cargar los generos de las peliculas y sus Rating!!!")
            case "7":
                if bandera_tres == True:
                    obtener_mejor_rating(lista_peliculas)
                else:
                    mostrar_mensajes("Error , Primero debes cargar los Rating de las peliculas!!!")
            case "8":
                if bandera_dos == True and bandera_tres == True:
                    ordenar_peliculas(lista_peliculas,"genero")
                    guardar_json(obtener_path("movies","json"),lista_peliculas)
                else:
                    mostrar_mensajes("Error , Primero debes cargar los generos de las peliculas y sus Rating!!!")
            case "9":
                break
            case other:
                mostrar_mensajes("Opcion Invalida!!!")
except FileNotFoundError:
    print("ARCHIVO NO ENCONTRADO!!!")
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)

print("FIN DEL PROGRAMA!!")

