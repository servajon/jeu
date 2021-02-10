import pygame
from pip._vendor.distlib.compat import raw_input

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

    def get_utilsateur(self):
        return self.utilisesur

    def set_utilisateur(self, user):
        self.utilisesur = user

    def action(self):
        if not self.get_vivant() and self.vie == 1:
            print("Pomme Dorée : Je dois utiliser une vie pour me sauver")
            self.vie = 0
            self.set_vivant(True)
            return False
        elif not self.get_vivant() and self.vie == 0:
            print("Pomme Dorée : Je meurs")
            return True
        elif self.vie == 1:
            reanime = raw_input("choisir quelqu'un a réanimer (null personne) : ")
            if reanime == "null":
                print("Pomme Dorée : Je passe mon tour")
            else:
                self.vie = 0
            return reanime
        else:
            print("Pomme Dorée : Je ne peux réanimer personne")
            return "null"

    def vote(self):
        print("Pomme Dorée vote")