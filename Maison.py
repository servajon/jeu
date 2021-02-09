import pygame


class Maison(object):
    def __init__(self, x, y, nom):
        self.nom = nom
        self.x = x
        self.y = y
        self.centrex = x + 64/2
        self.centrey = y + 92/2

        if self.nom == 'Artichaut':
            self.sprit = pygame.image.load('sprit/maisonartichaut.png')
        elif self.nom == 'Pastèque':
            self.sprit = pygame.image.load('sprit/maisonPastéque.png')
        elif self.nom == 'Grande Noix':
            self.sprit = pygame.image.load('sprit/maisonnoix.png')
        elif self.nom == 'Pomme Dorée':
            self.sprit = pygame.image.load('sprit/maisonpomme.png')
        elif self.nom == 'Avocat':
            self.sprit = pygame.image.load('sprit/maisonavocat.png')
        else:
            self.sprit = pygame.image.load('sprit/maisonpatate.png')

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_centrex(self):
        return self.centrex

    def get_centrey(self):
        return self.centrey

    def get_nom(self):
        return self.nom

    def draw(self, win):
        win.blit(self.sprit, (self.x, self.y))

    def __str__(self):
        return self.get_nom()
