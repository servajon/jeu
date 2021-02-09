from FL import *


class Champi_parasite(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Champi_parasite"
        self.sprit = pygame.image.load('sprit/croix.png')

    def get_nom(self):
        return self.nom

    def action(self):
        if not self.get_vivant():
            print("Champi_parasite : je meurs")
        else:
            print("Champi_parasite : je tue quelqu'un")
            return 0
