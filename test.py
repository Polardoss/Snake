import unittest
from game import Game

class TestVictoryCondition(unittest.TestCase):
    def test_victory_condition(self):
        game = Game()
        # Remplir le serpent avec le nombre de segments nécessaire pour gagner
        game.snake.feed(500)
        # Exécuter la fonction qui vérifie la condition de victoire
        game.gerer_jeu()
        # Vérifier si le jeu est passé en mode menu après la victoire
        self.assertTrue(game.menu_actif)
        self.assertFalse(game.jeu_actif)

def test_lose_condition(self):
        game = Game()
        # Ajouter suffisamment de segments pour que le serpent entre en collision avec lui-même
        game.snake.corp = [[100, 100]] * 500
        # Exécuter la fonction qui vérifie la condition de défaite
        game.gerer_jeu()
        # Vérifier si le jeu est passé en mode menu après la défaite
        self.assertTrue(game.menu_actif)
        self.assertFalse(game.jeu_actif)

if __name__ == '__main__':
    unittest.main()
