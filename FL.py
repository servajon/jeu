import pygame


class FL(object):
    def __init__(self):
        self.nom = "FL"
        self.bouge = False
        self.vivant = True
        self.vote = "null"
        self.x = 0
        self.y = 0

    def set_vivant(self, vivant):
        self.vivant = vivant

    def get_vivant(self):
        return self.vivant

    def get_nom(self):
        return self.nom

    def get_sprit(self):
        return self.sprit

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_bouge(self):
        return self.bouge

    def set_bouge(self, a):
        self.bouge = a

    def get_vote(self):
        return self.vote

    def set_vote(self):
        print("votez pour la personne a éliminer : ")
        ch = input()
        self.vote = ch

    def action(self):
        return ("pas d'acion pour la classe FL")


    def __str__(self):
        return self.get_nom()

    def __lt__(self, other):
        if self.nom < other.nom:
            return 0
        else:
            return 1

    def draw(self, win):
        if self.vivant:
            win.blit(self.sprit, (self.x, self.y))
