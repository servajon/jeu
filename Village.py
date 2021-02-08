import pygame
import cmath
from FL import *


class Village(object):
    def __init__(self, nbjoueur):
        self.joueurs = []
        self.maison = []
        self.nbjoueur = nbjoueur
        self.nbjours = 0
        self.evenement = 0

        self.creation()

    def creation(self):
        self.add(FL('artichaut'))
        self.add(FL('Grande noix'))
        self.add(FL('pastèque'))
        self.add(FL('pomme dorée'))
        self.add(FL('champignon hypnotiseur'))
        self.add(FL('avocat'))
        self.add(FL('champignon zombie'))
        self.add(FL('champignon parasite'))
        if self.nbjoueur > 8:
            i = 9
            while i < self.nbjoueur + 1:
                self.add(FL('patate'))
                i = i + 1

        self.joueurs.sort(key=lambda x: x.nom)





    def add(self, fl):
        self.joueurs.append(fl)

    def get_joueurs(self): #toute la liste de joueurs
        return self.joueurs

    def get_joueur(self, nom): #la liste avec les joueurs ayant un 'nom'
        temp = []
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_nom() == nom:
                temp.append(self.joueurs[i])

        return temp

    def get_nbvivant(self):
        nb = 0
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_vivant():
                nb = nb + 1
        return nb



    def draw(self, win):
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_vivant():
                win.blit(self.joueurs[i].get_sprit(), (int((cmath.cos((cmath.pi*2)/self.get_nbvivant()*i)*150).real) + 500, int((cmath.sin((cmath.pi*2)/self.get_nbvivant()*i)*150).real) + 350))