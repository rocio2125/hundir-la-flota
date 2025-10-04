from funciones import tableros as t
import random
import pygame
pygame.mixer.init()
sonido_agua = pygame.mixer.Sound('sonidos\splash.mp3')
explosion = pygame.mixer.Sound('sonidos\explosion.mp3')

def disparo(tablero_1, tablero_2, coordenada):
    if tablero_1[coordenada] == "O":
        tablero_1[coordenada] = "X"
        tablero_2[coordenada] = "X"
        explosion.play()
        pygame.time.delay(int(explosion.get_length() * 1000))
        print("Tocado. ¡Le has dado de lleno!")
    elif tablero_1[coordenada] == "X" or tablero_1[coordenada] == "~":
        print("ya has disparado a esa posición, dispara a otro sitio")
    else:
        tablero_1[coordenada] = "~"
        tablero_2[coordenada] = "~"
        sonido_agua.play()
        pygame.time.delay(int(sonido_agua.get_length() * 1000))
        print("Agua")

def disparo_aleatorio(tablero_1,tablero_2):
    num_max_filas = tablero_1.shape[0]
    num_max_columnas = tablero_1.shape[1]
    while True:
        coordenada = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1)) 
        if tablero_1[coordenada] == "O":
            tablero_1[coordenada] = "X"
            tablero_2[coordenada] = "X"
            explosion.play()
            pygame.time.delay(int(explosion.get_length() * 1000))
            print("¡Oh no! Uno de tus barcos ha sido tocado.\n El rival volverá a disparar")
            
        elif tablero_1[coordenada] == "X" or tablero_1[coordenada] == "~":
            continue
        else:
            tablero_1[coordenada] = "~"
            tablero_2[coordenada] = "~"
            sonido_agua.play()
            pygame.time.delay(int(sonido_agua.get_length() * 1000))
            print("El rival ha disparado a agua")
            break