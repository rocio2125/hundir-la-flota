import pygame
pygame.mixer.init()

sonido_agua = pygame.mixer.Sound('sonidos\splash.mp3')
sonido_agua.play()
pygame.time.delay(int(sonido_agua.get_length() * 1000))

explosion = pygame.mixer.Sound('sonidos\explosion.mp3')
explosion.play()
pygame.time.delay(int(explosion.get_length() * 1000))