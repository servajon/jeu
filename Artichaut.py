import pygame
from FL import *


class Artichaut(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Artichaut"
        self.secache = False
        self.cache = False
        self.cache_tour_passe = False
        self.sprit = pygame.image.load('sprit/artichaud.jpeg')

    def get_nom(self):
        return self.nom

    def action(self):
        if not self.get_vivant():
            print("Artichaut : je meurs")
            return True
        elif self.secache:
            if self.cache_tour_passe == True:
                print("Artichaut : Je ne peux pas me cacher ce tour, je l'ai fais le tour d'avant")
            else:
                print("Artichaut : Je me cache")
                self.cache = True
        else:
            print("Artichaut : Je passe mon tour")

    def vote(self):
        print("Artichaut vote")
        self.avote = True