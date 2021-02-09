import cmath

from Artichaut import *
from Avocat import *
from GrandeNoix import *
from Maison import *
from Pastèque import *
from Patate import *
from PommeDoree import *


class Village(object):
    def __init__(self, nbjoueur):
        self.joueurs = []
        self.maisons = []
        self.mort = []
        self.nbjoueur = nbjoueur
        self.nbjours = 0
        self.evenement = "null"

        self.creation()

    def creation(self):

        self.addJ(Artichaut())
        self.addJ(PommeDoree())
        self.addJ(PommeDoree())
        self.addJ(PommeDoree())
        self.addJ(PommeDoree())
        self.addJ(PommeDoree())
        self.addJ(PommeDoree())
        self.addJ(PommeDoree())
        self.addJ(PommeDoree())
        self.addJ(PommeDoree())

        if self.nbjoueur > len(self.joueurs):  # si plus de 8 jours il y a des personnes patate
            i = len(self.joueurs)
            while i < self.nbjoueur:
                self.addJ(Patate())
                i = i + 1
        self.joueurs.sort(reverse=True)  # tris des joueurs

        # calcule des position pour les joueurs autour du feu
        self.posjoueursapp(self.calcposjoueurs())

        self.addM(Maison(850, 300, 'Artichaut'))  # add des maisons
        self.addM(Maison(600, 650, 'Avocat'))
        self.addM(Maison(175, 600, 'Grande Noix'))
        self.addM(Maison(120, 100, 'Pastèque'))
        self.addM(Maison(650, 50, 'Pomme Dorée'))
        if self.nbjoueur > 8:  # si plus de 8 jours il y a des personnes patate alors on ajoute la maison
            self.addM(Maison(400, 20, 'Patate'))

    def addJ(self, fl):
        self.joueurs.append(fl)

    def addM(self, m):
        self.maisons.append(m)

    def get_joueurs(self):  # toute la liste de joueurs
        return self.joueurs

    def get_joueur(self, nom):  # la liste avec les joueurs ayant un 'nom'
        temp = []
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_nom() == nom:
                temp.append(self.joueurs[i])
        return temp

    def get_nbjoueur(self):
        return self.nbjoueur

    def get_evenement(self):
        return self.evenement

    def set_evenement(self, evenement):
        self.evenement = evenement

    def get_maison(self, nom):  # retourne la maison avec le 'nom'
        for i in range(len(self.maisons)):
            if self.maisons[i].get_nom() == nom:
                return self.maisons[i]
        return -1

    def get_nbvivant(self):  # si le joueur est vivant
        nb = 0
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_vivant():
                nb = nb + 1
        return nb

    def nbbouge(self):
        a = 0
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_bouge():
                a = a + 1
        return a

    def calcposjoueurs(self):
        array = []
        i = 0
        for i in range(len(self.joueurs)):
            x = int((cmath.cos((cmath.pi * 2) / self.get_nbvivant() * i) * 150).real) + 500
            y = int((cmath.sin((cmath.pi * 2) / self.get_nbvivant() * i) * 150).real) + 350
            array.append(x)
            array.append(y)
        return array

    def posjoueursapp(self, array):
        j = 0
        for i in range(self.nbjoueur):
            if self.joueurs[i].get_vivant():
                self.joueurs[i].set_x(array[j])
                j = j + 1
                self.joueurs[i].set_y(array[j])
                j = j + 1

    def set_mouvement_on(self):
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_vivant() == True:
                self.joueurs[i].set_bouge(True)

    def action(self):
        for i in range(len(self.joueurs)):
            self.joueurs[i].action()

    def tue(self, num):
        self.joueurs[num].set_vivant(False)
        if self.joueurs[num].action():
            self.mort.append(self.joueurs[num])
            self.joueurs.pop(num)

    def drawP(self, win):  # dessin des personnages
        for i in range(len(self.joueurs)):
            self.joueurs[i].draw(win)

    def drawM(self, win):  # dessin des maisons
        for i in range(len(self.maisons)):
            self.maisons[i].draw(win)

    def animationrentre(self):
        i = 0
        while i < self.get_nbvivant():
            if self.joueurs[i].get_bouge():
                vel = 10
                nom = self.joueurs[i].get_nom()

                xM = self.get_maison(nom).get_centrex()
                yM = self.get_maison(nom).get_centrey()

                x = self.joueurs[i].get_x()
                y = self.joueurs[i].get_y()

                trajx = abs(xM - x)
                trajy = abs(yM - y)

                if trajx == 0:
                    dir = trajy
                elif trajy == 0:
                    dir = trajx
                elif trajx < trajy:
                    dir = trajy / trajx
                else:
                    dir = trajx / trajy

                nb = int(vel / dir) + 1

                if trajx < trajy:
                    velx = nb
                    vely = dir * nb
                else:
                    vely = nb
                    velx = dir * nb

                if velx > vel:
                    velx = vel
                if vely > vel:
                    vely = vel

                if x >= xM and y >= yM:
                    self.joueurs[i].set_x(x - velx)
                    self.joueurs[i].set_y(y - vely)
                elif x > xM and y < yM:
                    self.joueurs[i].set_x(x - velx)
                    self.joueurs[i].set_y(y + vely)
                elif x <= xM and y >= yM:
                    self.joueurs[i].set_x(x + velx)
                    self.joueurs[i].set_y(y - vely)
                else:
                    self.joueurs[i].set_x(x + velx)
                    self.joueurs[i].set_y(y + vely)

                if int(trajx) < 10 and int(trajy) < 10:
                    self.joueurs[i].set_bouge(False)
            i = i + 1
        if self.nbbouge() != 0:
            return True
        else:
            return False

    def animationsorti(self):
        i = 0
        while i < self.get_nbvivant():
            if self.joueurs[i].get_vivant():
                array = self.calcposjoueurs()
                vel = 10
                j = i
                xM = array[j * 2]
                yM = array[j * 2 + 1]
                x = self.joueurs[i].get_x()
                y = self.joueurs[i].get_y()

                trajx = abs(xM - x)
                trajy = abs(yM - y)

                if trajx == 0 and trajy == 0:
                    dir = 1
                elif trajx == 0:
                    dir = trajy
                elif trajy == 0:
                    dir = trajx
                elif trajx < trajy:
                    dir = trajy / trajx
                else:
                    dir = trajx / trajy

                nb = int(vel / dir) + 1

                if trajx < trajy:
                    velx = nb
                    vely = dir * nb
                else:
                    vely = nb
                    velx = dir * nb

                if velx > vel:
                    velx = vel
                if vely > vel:
                    vely = vel

                if x >= xM and y >= yM:
                    self.joueurs[i].set_x(x - velx)
                    self.joueurs[i].set_y(y - vely)
                elif x > xM and y < yM:
                    self.joueurs[i].set_x(x - velx)
                    self.joueurs[i].set_y(y + vely)
                elif x <= xM and y >= yM:
                    self.joueurs[i].set_x(x + velx)
                    self.joueurs[i].set_y(y - vely)
                else:
                    self.joueurs[i].set_x(x + velx)
                    self.joueurs[i].set_y(y + vely)

                if int(trajx) < 10 and int(trajy) < 10:
                    self.joueurs[i].set_x(xM)
                    self.joueurs[i].set_y(yM)
                    self.joueurs[i].set_bouge(False)
            i = i + 1
        if self.nbbouge() != 0:
            return True
        else:
            return False

    def gestionjour(self, event):
        if event == "rentre":
            for i in range(len(self.joueurs)): #test de la mort de la pastéque
                if self.joueurs[i].get_nom() == "Pastèque":
                    if self.joueurs[i].get_esttue():
                        self.tue(i)
                        break

            self.set_mouvement_on()
            self.evenement = "rentre"

        if event == "sort":
            self.set_mouvement_on()
            self.tue(0)
            self.evenement = "sort"
            print(len(self.joueurs))

        if event == "action":
            self.action()

        if event == "vote":
            return 0
