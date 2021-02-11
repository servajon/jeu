from FL import *


class Pasteque(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Pastèque"
        self.esttue = False
        self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/Pasteque_gamejam2021.png')
        self.spritMort = pygame.image.load('sprit/gamejam-image-fruit&légume/Pasteque_gamejam2021.png')
        self.spritMort = pygame.transform.scale(self.spritMort, (40, 40))

    def get_nom(self):
        return self.nom

    def get_esttue(self):
        return self.esttue

    def action(self):
        self.log.clear()
        if self.get_vivant() == False and self.esttue == False:
            self.set_vivant(True)
            self.esttue = True
            self.log.append("Pastèque : j'ai été tué, je vais mourir cette nuit")
            return False
        elif self.get_vivant() == False and self.esttue == True:
            self.set_vivant(True)

            self.log.append("Pastèque : je meurs")
            return True
        else:
            self.log.append("je passe mon tour")

    def vote(self):
        self.log.clear()
        self.log.append("pastéque vote : ")
        self.avote = True

    def presentation(self):
        self.log.clear()
        self.log.append("pastéque : ")