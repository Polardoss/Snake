import pygame
from config import TAILLE_RECTANGLE, WIDTH, HEIGHT

class Snake:
    def __init__(self):
        self.position = [100, 100]
        self.vitesse = TAILLE_RECTANGLE
        self.couleur = (255, 0, 0)
        self.corp = [[100, 100], [100-TAILLE_RECTANGLE, 100]]
        self.direction = "DROITE"
        self.score = 0
        
    def reset_snake(self):
        self.position = [100, 100]
        self.corp = [[100, 100], [100-TAILLE_RECTANGLE, 100]]
        self.direction = "DROITE"
        self.score = 0

    def afficher(self, screen):
        for segment in self.corp:
            pygame.draw.rect(screen, self.couleur, pygame.Rect(segment[0], segment[1], TAILLE_RECTANGLE, TAILLE_RECTANGLE))


    def move(self, pomme):
        tete = list(self.position)

        if self.direction == 'DROITE':
            self.position[0] += self.vitesse
        elif self.direction == 'GAUCHE':
            self.position[0] -= self.vitesse
        elif self.direction == 'HAUT':
            self.position[1] -= self.vitesse
        elif self.direction == 'BAS':
            self.position[1] += self.vitesse

        self.corp.insert(0, tete)

        if tete[0] == pomme.position[0] and tete[1] == pomme.position[1]:
            self.manger_pomme()
            pomme.nouvelle_pomme(self)
        else:
            self.corp.pop() #Suprime les element en double


    def changer_direction(self, direction):
        if self.direction == "DROITE" and direction == "GAUCHE":
            return
        elif self.direction == "GAUCHE" and direction == "DROITE":
            return
        elif self.direction == "HAUT" and direction == "BAS":
            return
        elif self.direction == "BAS" and direction == "HAUT":
            return
        self.direction = direction

    def check_collision(self, screen):
        if (
            self.position[0] < 0 or
            self.position[0] >= screen.get_width() or 
            self.position[1] < 0 or
            self.position[1] >= screen.get_height()
        ):
            return True #Il y a collision avec l'écrant
        
        for segment in self.corp[1:]:
            if self.position == segment:
                return True #Il y a collision avec son corp
            
        return False #Aucune collision


    def manger_pomme(self):
        self.corp.append([10000,100000])
        self.score += 1
    
    def feed(self, nombres_pomme):
        for i in range(nombres_pomme):
            self.manger_pomme()

