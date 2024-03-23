import pygame
import random
from config import TAILLE_RECTANGLE, WIDTH,HEIGHT



class Pomme:
    def __init__(self):
        self.image_pomme = pygame.image.load('img\pomme.png')
        self.image_pomme = pygame.transform.scale(self.image_pomme, (TAILLE_RECTANGLE, TAILLE_RECTANGLE))
        self.position = [random.randrange(1, int(WIDTH / TAILLE_RECTANGLE)) * TAILLE_RECTANGLE, random.randrange(1, int(HEIGHT / TAILLE_RECTANGLE)) * TAILLE_RECTANGLE]
        self.couleur = (0, 0, 255)

    def afficher(self, screen):
        screen.blit(self.image_pomme, (self.position[0], self.position[1]))

    def nouvelle_pomme(self, snake):
        while True:
            x = random.randrange(1, int(WIDTH / TAILLE_RECTANGLE)) * TAILLE_RECTANGLE
            y = random.randrange(1, int(HEIGHT / TAILLE_RECTANGLE)) * TAILLE_RECTANGLE
            self.position = [x, y]
            print("Nouvelle position de la pomme:", self.position)

            # Vérifier si la nouvelle position de la pomme n'est pas dans le corps du serpent
            if self.position not in snake.corp:
                break
