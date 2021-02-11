import pygame
from pygame.tests.draw_test import RED, GREEN


class FL(object):
    def __init__(self):
        self.nom = "FL"
        self.bouge = False
        self.vivant = True
        self.x = 0
        self.y = 0
        self.spritx = 128
        self.sprity = 128
        self.nbvote = 0
        self.avote = False
        self.log = []

    def get_log(self):
        return self.log

    def set_log(self, txt):
        self.log.append(txt)

    def get_nbvote(self):
        return self.nbvote

    def plusvote(self):
        self.nbvote = self.nbvote + 1

    def resetvote(self):
        self.avote = False
        self.nbvote = 0

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

    def get_spritx(self):
        return self.spritx

    def get_sprity(self):
        return self.sprity

    def get_bouge(self):
        return self.bouge

    def set_bouge(self, a):
        self.bouge = a

    def get_avote(self):
        return self.avote

    def set_avote(self, v):
        self.avote = v

    def action(self):
        print("pas d'acion pour la classe FL")

    def vote(self):
        print("pas de vote pour la classe FL")

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

    def drawVote(self, win):
        text = self.nbvote
        font = pygame.font.SysFont('freesansbold.ttf', 20)
        text = font.render(str(text), True, RED)
        win.blit(text, (self.x , self.y - 15))

