import pygame
import cmath
from FL import *
from Maison import *


class Village(object):
    def __init__(self, nbjoueur):
        self.joueurs = []
        self.maisons = []
        self.nbjoueur = nbjoueur
        self.nbjours = 0
        self.evenement = 0

        self.creation()

    def creation(self):
        self.addJ(FL('artichaut'))
        self.addJ(FL('artichaut'))
        self.addJ(FL('artichaut'))
        self.addJ(FL('artichaut'))
        self.addJ(FL('artichaut'))

        self.addJ(FL('avocat'))
        self.addJ(FL('avocat'))

        self.addJ(FL('grande noix'))

        self.addJ(FL('pasteque'))
        self.addJ(FL('pasteque'))

        self.addJ(FL('pomme dorée'))
        # self.addJ(FL('champignon hypnotiseur'))

        # self.addJ(FL('champignon zombie'))
        # self.addJ(FL('champignon parasite'))

        if self.nbjoueur > len(self.joueurs):  # si plus de 8 jours il y a des personnes patate
            i = len(self.joueurs)
            while i < self.nbjoueur + 1:
                self.addJ(FL('patate'))
                i = i + 1

        self.joueurs.sort(reverse=True)  # trix des joueurs

        self.calcposjoueurs()  # calcule des position pour les joueurs autour du feu

        self.addM(Maison(850, 300, 'artichaut'))  # add des maisons
        self.addM(Maison(600, 650, 'avocat'))
        self.addM(Maison(175, 600, 'grande noix'))
        self.addM(Maison(120, 100, 'pasteque'))
        self.addM(Maison(650, 50, 'pomme dorée'))
        if self.nbjoueur > 8:  # si plus de 8 jours il y a des personnes patate alors on ajoute la maison
            self.addM(Maison(400, 20, 'patate'))

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

    def calcposjoueurs(self):
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_vivant():
                self.joueurs[i].set_x(int((cmath.cos((cmath.pi * 2) / self.get_nbvivant() * i) * 150).real) + 500)
                self.joueurs[i].set_y(int((cmath.sin((cmath.pi * 2) / self.get_nbvivant() * i) * 150).real) + 350)

    def drawP(self, win):  # dessin des personnages
        for i in range(len(self.joueurs)):
            self.joueurs[i].draw(win)

    def drawM(self, win):  # dessin des maisons
        for i in range(len(self.maisons)):
            self.maisons[i].draw(win)

    def animation(self, win):
        i = 0
        while i < len(self.joueurs):
            if not self.joueurs[i].get_rentre():
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


                if int(trajx) < 15 and int(trajy) < 15:
                    self.joueurs[i].set_rentre(True)
            i = i + 1
