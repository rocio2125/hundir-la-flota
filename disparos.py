import tableros as t
import barcos
import random

def disparo(tablero_1, tablero_2, coordenada):
    if tablero_1[coordenada] == "O":
        tablero_1[coordenada] = "X"
        tablero_2[coordenada] = "X"
        print("Tocado")
    elif tablero_1[coordenada] == "X" or tablero_1[coordenada] == "~":
        print("ya has disparado a esa posición, dispara a otro sitio")
    else:
        tablero_1[coordenada] = "~"
        tablero_2[coordenada] = "~"
        print("Agua")

def disparo_aleatorio(tablero_1,tablero_2):
    num_max_filas = tablero_1.shape[0]
    num_max_columnas = tablero_1.shape[1]
    while True:
        coordenada = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1)) 
        if tablero_1[coordenada] == "O":
            tablero_1[coordenada] = "X"
            tablero_2[coordenada] = "X"
            print("¡Oh no! Uno de tus barcos ha sido tocado")
            break
        elif tablero_1[coordenada] == "X" or tablero_1[coordenada] == "~":
            continue
        else:
            tablero_1[coordenada] = "~"
            tablero_2[coordenada] = "~"
            print("El rival ha disparado a agua")
            break

# tablero_prueba = t.crea_tablero()
# disparo(tablero_prueba,(1,0))
# print(tablero_prueba)