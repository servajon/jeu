from FL import *


class Patate(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Patate"
        self.sprit = pygame.image.load('sprit/patate.png')

    def get_nom(self):
        return self.nom

    def action(self):
        if not self.get_vivant():
            print("Patate : je meurs")
            return True
        else:
            print("Patate : je passe mon tour")

    def vote(self):
        print("Patate vote")