from FL import *


class Pasteque(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Pastèque"
        self.esttue = False
        self.sprit = pygame.image.load('sprit/pastéque.jpg')

    def get_nom(self):
        return self.nom

    def get_esttue(self):
        return self.esttue

    def action(self):
        if self.get_vivant() == False and self.esttue == False:
            self.set_vivant(True)
            self.esttue = True
            print("Pastèque : j'ai été tué, je vais mourir cette nuit")
            return False
        elif self.get_vivant() == False and self.esttue == True:
            self.set_vivant(True)
            print("Pastèque : je meurs")
            return True
        else:
            print("Pastèque : je passe")
