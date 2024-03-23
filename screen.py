import pygame
from config import WIDTH,HEIGHT

class Screen:
    def __init__(self, couleur_ecran):
        self.couleur_ecran = couleur_ecran
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.screen.fill(self.couleur_ecran)
        pygame.display.set_caption("Snake Game")
    
    
