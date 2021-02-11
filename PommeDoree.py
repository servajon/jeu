from pip._vendor.distlib.compat import raw_input

from FL import *


class PommeDoree(FL):
    def __init__(self):
        FL.__init__(self)
        self.nom = "Pomme Dorée"
        self.vie = 1
        self.utilisesur = "null"
        self.sprit = pygame.image.load('sprit/gamejam-image-fruit&légume/goldenApple-Gamejam2021.png')
        self.spritMort = pygame.image.load('sprit/gamejam-image-fruit&légume/goldenApple-Gamejam2021.png')
        self.spritMort = pygame.transform.scale(self.spritMort, (40, 40))


    def get_nom(self):
        return self.nom

    def get_utilsateur(self):
        return self.utilisesur

    def set_utilisateur(self, user):
        self.utilisesur = user

    def get_nbvie(self):
        return self.vie

    def set_nbvie(self, nb):
        self.vie = nb

    def action(self):
        self.log.clear() #a chaque action
        if not self.get_vivant() and self.vie == 1:
            self.log.append("Pomme Dorée : Je dois utiliser une vie pour me sauver")
            print("Pomme Dorée : Je dois utiliser une vie pour me sauver")
            self.vie = 0
            self.set_vivant(True)
            return False

        elif not self.get_vivant() and self.vie == 0:
            self.log.append("Pomme Dorée : Je meurs")
            print("Pomme Dorée : Je meurs")
            return True
        else:
            self.log.append("Pomme Dorée : je passe mon tour")
            print("Pomme Dorée : je passe mon tour")

    def vote(self):
        self.log.clear()
        self.log.append("Pomme Dorée vote : ")
        print("Pomme Dorée vote")
        self.avote = True

    def actionspe(self, cible):
        self.log.clear()  # a chaque action
        self.log.append("Je réssussite " + cible + " !")
        self.vie = 0


    def presentation(self):
        self.log.clear()
        self.log.append("Pomme Dorée : ")
        if self.vie == 1:
            self.log.append("Il me reste une vie, je peux m'en servire")
        else:
            self.log.append("Il ne me reste plus de vie")