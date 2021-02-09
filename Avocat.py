import pygame
from FL import *


class Avocat(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Avocat"
        self.sprit = pygame.image.load('sprit/avocat.png')

    def get_nom(self):
        return self.nom

    def action(self):
        if not self.get_vivant():
            print("Avocat : je meurs")
            return True
        else:
            print("Avocat : je passe mon tour")
