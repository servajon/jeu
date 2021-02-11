import pygame


class Maison(object):
    def __init__(self, x, y, nom):
        self.nom = nom
        self.x = x
        self.y = y
        self.centrex = x
        self.centrey = y

        if self.nom == 'Artichaut':
            self.sprit = pygame.image.load('sprit/assets-image-maison-Fruit+Légume/maison-artichaut_gamejam2021.png')
        elif self.nom == 'Pastèque':
            self.sprit = pygame.image.load('sprit/assets-image-maison-Fruit+Légume/maison_pasteque-gamejam2021.png')
        elif self.nom == 'Grande Noix':
            self.sprit = pygame.image.load('sprit/assets-image-maison-Fruit+Légume/maison-GrandeNoix_gamejam2021.png')
        elif self.nom == 'Pomme Dorée':
            self.sprit = pygame.image.load('sprit/assets-image-maison-Fruit+Légume/maison-goldenApple_gamejam2021.png')
        elif self.nom == 'Avocat':
            self.sprit = pygame.image.load('sprit/assets-image-maison-Fruit+Légume/maison-avocat_gamejam2021.png')
        else:
            self.sprit = pygame.image.load('sprit/assets-image-maison-Fruit+Légume/maison-patate_gamejam2021.png')

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
