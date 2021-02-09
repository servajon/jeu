import pygame


class FL(object):
    def __init__(self, nom):
        self.nom = nom
        self.rentre = False
        self.vivant = True
        self.x = 0
        self.y = 0

        if (self.nom == 'patate'):
            self.sprit = pygame.image.load('sprit/patate.png')
        elif (self.nom == 'grande noix'):
            self.sprit = pygame.image.load('sprit/noix.png')
        elif (self.nom == 'artichaut'):
            self.sprit = pygame.image.load('sprit/artichaud.jpeg')
        elif (self.nom == 'avocat'):
            self.sprit = pygame.image.load('sprit/avocat.png')
        elif (self.nom == 'pasteque'):
            self.sprit = pygame.image.load('sprit/pastéque.jpg')
        elif (self.nom == 'pomme dorée'):
            self.sprit = pygame.image.load('sprit/Pomme_doree.png')
        else:
            self.sprit = pygame.image.load('sprit/croix.png')

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

    def get_rentre(self):
        return self.rentre

    def set_rentre(self, a):
        self.rentre = a

    def __str__(self):
        return self.get_nom()

    def __lt__(self, other):
        if self.nom < other.nom:
            return 0
        else:
            return 1

    def draw(self, win):
        win.blit(self.sprit, (self.x, self.y))
