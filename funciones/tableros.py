#Importamos las librerias numpy y random
import numpy as np
import random

#Generar tablero cuadrado
def crea_tablero(lado = 10):
    tablero = np.full((lado,lado)," ")
    return tablero
