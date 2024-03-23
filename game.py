import pygame
import snake
import pomme
import screen

from config import NB_CASE

couleur_ecran = (250,250,250)

class Game:
    def __init__(self):
        pygame.init()
        self.police = pygame.font.SysFont("monospace", 20) #Police d'écriture
        

        self.clock = pygame.time.Clock()
        self.screen = screen.Screen(couleur_ecran)
        self.score = 0
        self.meilleure_score = 0
        self.snake = snake.Snake()
        self.pomme = pomme.Pomme()

        self.menu_actif = True
        self.jeu_actif = False

    

    def run(self):
        """
        Gère l'exécution du jeu en alternant entre le menu principal et le jeu.
        """
        while True:
            if self.menu_actif:
                self.gerer_menu()
            elif self.jeu_actif:
                self.gerer_jeu()

            pygame.display.flip()
            self.clock.tick(10)

                



    def gerer_menu(self):
        self.score = self.snake.score
        if self.score > self.meilleure_score:
            self.meilleure_score = self.score

        
        self.screen.screen.fill((0, 0, 0)) #Menu fond noir
        self.afficher_text_centre("Menu", (255, 255, 255), -50)
        self.afficher_text_centre("Appuyez sur ESPACE pour jouer", (255, 255, 255), 50)
        self.afficher_text_centre(f"SCORE:{self.score} ", (255, 255, 255), 100)
        self.afficher_text_centre(f"MEILLEURE SCORE:{self.meilleure_score} ", (255, 255, 255), 150)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Lancement du jeux")
                    self.snake.reset_snake() # je reset le serpent
                    self.menu_actif = False
                    self.jeu_actif = True
                    return

    def gerer_jeu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu_actif = True
                    self.jeu_actif = False
                    self.gerer_menu()
                    return
                elif event.key == pygame.K_UP:
                    self.snake.changer_direction("HAUT")
                elif event.key == pygame.K_DOWN:
                    self.snake.changer_direction("BAS")
                elif event.key == pygame.K_LEFT:
                    self.snake.changer_direction("GAUCHE")
                elif event.key == pygame.K_RIGHT:
                    self.snake.changer_direction("DROITE")
                elif event.key == pygame.K_f:
                    self.snake.feed(10)

        self.screen.screen.fill(couleur_ecran) #Jeu Fond Blanc
        
        self.snake.move(self.pomme) #Bouge le serpent
        

        if self.snake.check_collision(self.screen.screen):
            image_text = self.police.render("Perdu", 1, (255, 0, 0))
            self.screen.screen.blit(image_text,(320,240))
            print("PERDU")
            self.menu_actif = True
            self.jeu_actif = False
            self.gerer_menu()
            return

        self.snake.afficher(self.screen.screen) 
        self.pomme.afficher(self.screen.screen)
        self.afficher_text_centre(f"SCORE:{self.snake.score} ", (0, 0, 0), 100)

        if len(self.snake.corp) == NB_CASE:
            # Afficher un message de victoire
            image_text = self.police.render("Victoire !", 1, (0, 255, 0))
            self.screen.screen.blit(image_text,(320,240))
            print("VICTOIRE")
            # Réinitialiser le jeu
            self.menu_actif = True
            self.jeu_actif = False
            self.gerer_menu()
            return


    def afficher_text_centre(self, texte, couleur, decalage_y=0):
        text_surface = self.police.render(texte, True, couleur)
        text_rect = text_surface.get_rect(center=(self.screen.screen.get_width() // 2, self.screen.screen.get_height() // 2 + decalage_y))
        self.screen.screen.blit(text_surface, text_rect)

    def quit_game(self):
        print("Je ferme la fenetre")
        pygame.quit()
        quit()