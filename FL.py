import pygame


class FL(object):
    def __init__(self, nom):
        self.nom = nom
        self.vivant = True


        if(self.nom == 'patate'):
            print('patate')
            self.sprit = pygame.image.load('sprit/patate.png')
        elif (self.nom == 'Grande noix'):
            print('Grande noix')
            self.sprit = pygame.image.load('sprit/noix.png')
        elif (self.nom == 'artichaut'):
            print('artichaut')
            self.sprit = pygame.image.load('sprit/artichaud.jpeg')
        elif (self.nom == 'avocat'):
            print('avocat')
            self.sprit = pygame.image.load('sprit/avocat.png')
        elif (self.nom == 'pastèque'):
            print('pastèque')
            self.sprit = pygame.image.load('sprit/pastéque.jpg')
        elif (self.nom == 'pomme dorée'):
            print('pomme dorée')
            self.sprit = pygame.image.load('sprit/Pomme_doree.png')
        else:
            print(1)
            self.sprit = pygame.image.load('sprit/Pomme_doree.png')

    def set_vivant(self, vivant):
        self.vivant = vivant

    def get_vivant(self):
        return self.vivant

    def get_nom(self):
        return self.nom

    def get_sprit(self):
        return self.sprit

    def __str__(self):
        return self.get_nom()
