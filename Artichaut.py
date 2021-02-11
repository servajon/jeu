from FL import *


class Artichaut(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Artichaut"
        self.secache = False
        self.cache = False
        self.cache_tour_passe = False
        self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/artichaut_gamejam2021.png')
        self.spritMort = pygame.image.load('sprit/gamejam-image-fruit&légume/artichaut_gamejam2021.png')
        self.spritMort = pygame.transform.scale(self.spritMort, (40, 40))

    def get_nom(self):
        return self.nom

    def action(self):
        self.log.clear()
        if not self.get_vivant():
            self.log.append("Artichaut : je meurs")
            return True
        elif self.secache:
            if self.cache_tour_passe == True:
                self.log.append("Artichaut : Je ne peux pas me cacher ce tour, je l'ai fais le tour d'avant")
            else:
                self.log.append("Artichaut : Je me cache")
                self.cache = True
        else:
            self.log.append("Je passe mon tour")

    def vote(self):
        self.log.clear()
        self.log.append("Artichaut vote : ")
        self.avote = True


    def presentation(self):
        self.log.clear()
        self.log.append("Artichaut : ")