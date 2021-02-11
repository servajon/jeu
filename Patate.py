from FL import *


class Patate(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Patate"
        self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/patate_gamejam2021.png')
        self.spritMort = pygame.image.load('sprit/gamejam-image-fruit&légume/patate_gamejam2021.png')
        self.spritMort = pygame.transform.scale(self.spritMort, (40, 40))

    def get_nom(self):
        return self.nom

    def action(self):
        self.log.clear()
        if not self.get_vivant():
            self.log.append("Patate : je meurs")
            return True
        else:
            self.log.append("je passe mon tour")

    def vote(self):
        self.log.clear()
        self.log.append("Patate vote : ")
        self.avote = True

    def presentation(self):
        self.log.clear()
        self.log.append("Patate : ")