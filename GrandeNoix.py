import pygame
from FL import *


class Grande_Noix(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Grande Noix"
        self.tue_un = False
        self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/GrandeNoix_gamejam2021.png')
        self.spritMort = pygame.image.load('sprit/gamejam-image-fruit&légume/GrandeNoix_gamejam2021.png')
        self.spritMort = pygame.transform.scale(self.spritMort, (40, 40))

    def get_nom(self):
        return self.nom

    def action(self):
        self.log.clear()
        if self.get_vivant() == False and self.tue_un == False:
            self.set_vivant(True)
            self.tue_un = True
            self.log.append("Grande Noix : j'ai survécu une fois")
            print("Grande Noix : j'ai survécu une fois")
            return False
        elif self.vivant == False and self.tue_un == True:
            self.log.append("Grande Noix : je meurs")
            print("Grande Noix : je meurs")
            return True
        else:
            self.log.append("je passe mon tour")
            print("Grande Noix : je passe")

    def vote(self):
        self.log.clear()
        self.log.append("Grande Noix vote : ")
        print("Grande Noix vote")
        self.avote = True

    def presentation(self):
        self.log.clear()
        self.log.append("Grande Noix : ")