from FL import *


class Champi_zombie(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Champi-zombie"
        self.sprit = pygame.image.load('sprit/gameJam-image-champi/champi_zombie.png')

    def get_nom(self):
        return self.nom

    def action(self):
        if not self.get_vivant():
            print("Champi-zombie : je meurs")
        else:
            print("Champi-zombie : je passe mon tour")
