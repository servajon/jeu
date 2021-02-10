import pygame
from FL import *


class Grande_Noix(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Grande Noix"
        self.tue_un = False
        self.sprit = pygame.image.load('sprit/noix.png')

    def get_nom(self):
        return self.nom

    def action(self):
        if self.get_vivant() == False and self.tue_un == False:
            self.set_vivant(True)
            self.tue_un = True
            print("Grande Noix : j'ai survécu une fois")
            return False
        elif self.vivant == False and self.tue_un == True:
            print("Grande Noix : je meurs")
            return True
        else:
            print("Grande Noix : je passe")

    def vote(self):
        print("Grande Noix vote")
        self.avote = True