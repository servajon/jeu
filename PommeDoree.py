import pygame
from FL import *


class PommeDoree(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Pomme Dorée"
        self.vie = 1
        self.utilisesur = "null"
        self.sprit = pygame.image.load('sprit/Pomme_doree.png')

    def get_nom(self):
        return self.nom

    def action(self):
        if not self.get_vivant() and self.vie == 1:
            print("Pomme Dorée : Je dois utiliser une vie pour me sauver")
            self.vie = 0
            self.set_vivant(True)
            return False
        elif not self.get_vivant() and self.vie == 0:
            print("Pomme Dorée : Je meurs")
            return True
        elif self.utilisesur != "null" and self.vie == 0:
            print("Pomme Dorée : Je ne peux pas réssuciter, je n'ai plus de vie")
        elif self.utilisesur != "null" and self.vie == 1:
            self.utilisesur.set_vivant(True)
            print("Pomme Dorée : Je ressucite " + self.utilisesur.get_nom())
            self.utilisesur = "null"
            self.vie = 0
        else:
            print("Pomme Dorée : Je passe mon tour")

