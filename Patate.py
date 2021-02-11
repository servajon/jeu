from FL import *


class Patate(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Patate"
        self.sprit = pygame.image.load('sprit/patate.png')

    def get_nom(self):
        return self.nom

    def action(self):
        self.log.clear()
        if not self.get_vivant():
            self.log.append("Patate : je meurs")
            print("Patate : je meurs")
            return True
        else:
            self.log.append("je passe mon tour")
            print("Patate : je passe mon tour")

    def vote(self):
        self.log.clear()
        self.log.append("Patate vote : ")
        print("Patate vote")
        self.avote = True

    def presentation(self):
        self.log.clear()
        self.log.append("Patate : ")