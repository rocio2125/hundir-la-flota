import pygame
import nunpy

pygame.mixer.init()

sonido_agua = pygame.mixer.Sound('sonidos\splash.mp3')
sonido_agua.play()
pygame.time.delay(int(sonido_agua.get_length() * 1000))

explosion = pygame.mixer.Sound('sonidos\explosion.mp3')

tablero = np.full((5,5),"x")
