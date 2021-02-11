import random

from FL import *


class Hypnotiseur(FL):
    def __init__(self):
        FL.__init__(self)
        self.nomVrai = "Champignon Hypnotiseur"
        self.nom = "null"
        self.spritVrai = pygame.image.load('sprit/gameJam-image-champi/champi_hypno.png')
        self.sprit = "null"
        self.spritMort = pygame.image.load('sprit/gameJam-image-champi/champi_hypno.png')
        self.spritMort = pygame.transform.scale(self.spritMort, (40, 40))
        self.esttue = False
        self.spritRandom()

    def get_nom(self):
        return self.nom

    def get_nomVrai(self):
        return self.nomVrai

    def get_esttue(self):
        return self.esttue

    def action(self):
        self.log.clear()
        if not self.get_vivant():
            self.log.append("Champignon Hypnotiseur : je meurs")
            return True
        else:
            self.log.append("je passe mon tour")

    def spritRandom(self):
        nb = random.randint(0, 5)
        if nb == 0:
            self.nom = "Avocat"
            self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/avocat_gamejam2021.png')

        elif nb == 1:
            self.nom = "Pastèque"
            self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/Pasteque_gamejam2021.png')

        elif nb == 2:
            self.nom = "Artichaut"
            self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/artichaut_gamejam2021.png')

        elif nb == 3:
            self.nom = "Pomme Dorée"
            self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/GodenApple_gamejam2021.png')

        elif nb == 4:
            self.nom = "Grande Noix"
            self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/GrandeNoix_gamejam2021.png')

        elif nb == 5:
            self.nom = "Patate"
            self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/patate_gamejam2021.png')



    def vote(self):
        self.log.clear()
        self.log.append(self.nom + " vote : ")
        self.avote = True

    def presentation(self):
        self.log.clear()
        self.log.append(self.nom + " : ")
