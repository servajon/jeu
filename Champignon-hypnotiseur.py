from FL import *


class Champignon_hypnotiseur(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Champignon Hypnotiseur"
        self.sprit = pygame.image.load('sprit/croix.png')

    def get_nom(self):
        return self.nom

    def action(self):
        if not self.get_vivant():
            print("Champignon Hypnotiseur : je meurs")
        else:
            print("Champignon Hypnotiseur : je passe mon tour")
