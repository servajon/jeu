import cmath
import re

from Artichaut import *
from Avocat import *
from GrandeNoix import *
from Jour import *
from Maison import *
from Pastèque import *
from Patate import *
from PommeDoree import *


class Village(object):
    def __init__(self, nbjoueur):
        self.nbjoueur = nbjoueur

        self.joueurs = []
        self.maisons = []
        self.mort = []
        self.log = []

        self.joueuract = 0

        self.nbjours = 0
        self.jour = Jour()
        self.evenement = "null"

        self.creation()

    def creation(self):

        self.addJ(Artichaut())
        self.addJ(Pasteque())
        self.addJ(PommeDoree())
        self.addJ(Grande_Noix())
        self.addJ(Avocat())
        self.addJ(Grande_Noix())

        if self.nbjoueur > len(self.joueurs):  # si plus de 8 jours il y a des personnes patate
            i = len(self.joueurs)
            while i < self.nbjoueur:
                self.addJ(Patate())
                i = i + 1
        self.joueurs.sort(reverse=True)  # tris des joueurs

        # calcule des position pour les joueurs autour du feu
        self.posjoueursapp(self.calcposjoueurs())

        self.addM(Maison(920, 300, 'Artichaut'))  # add des maisons
        self.addM(Maison(850, 650, 'Avocat'))
        self.addM(Maison(525, 635, 'Grande Noix'))
        self.addM(Maison(100, 500, 'Pastèque'))
        self.addM(Maison(425, 35, 'Pomme Dorée'))
        if self.nbjoueur > 8:  # si plus de 8 jours il y a des personnes patate alors on ajoute la maison
            self.addM(Maison(80, 200, 'Patate'))

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
        for i in range(len(self.joueurs)):
            x = int((cmath.cos((cmath.pi * 2) / self.get_nbvivant() * i) * 160).real) + 480
            y = int((cmath.sin((cmath.pi * 2) / self.get_nbvivant() * i) * 160).real) + 280
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
            if self.joueurs[i].get_vivant():
                self.joueurs[i].set_bouge(True)

    def action(self):
        i = self.joueuract
        if self.joueurs[i].get_nom() == "Pomme Dorée":
            if self.joueurs[i].get_nbvie() == 1:
                pygame.event.clear()
                clique = self.posclique()
                for j in range(len(self.mort)):
                    if j > 7:
                        xmin = 30 * (j - 8) + 750
                        xmax = 30 * (j - 8) + 750 + 128
                        ymin = 65
                        ymax = 65 + 128
                    else:
                        xmin = 30 * j + 750
                        xmax = 30 * j + 750 + 128
                        ymin = 20
                        ymax = 20 + 128

                    if clique[0] > xmin and clique[0] < xmax and clique[1] > ymin and clique[1] < ymax:
                        self.joueurs[i].actionspe(self.mort[j].get_nom())
                        self.log += self.joueurs[i].get_log()

                        self.mort[j].set_vivant(True)
                        self.joueurs.append(self.mort[j])
                        self.mort.pop(j)
                        self.joueurs.sort(reverse=True)
                        self.evenement = "update_pos"
                        break
                    else:
                        self.joueurs[i].action()
                        self.log += self.joueurs[i].get_log()
                        self.evenement = "null"
            else:
                self.joueurs[i].action()
                self.log += self.joueurs[i].get_log()
                self.evenement = "null"
        else:
            self.joueurs[i].action()
            self.log += self.joueurs[i].get_log()
            self.evenement = "null"

    def posclique(self):
        clock = pygame.time.Clock()
        is_running = True
        while is_running:
            clock.tick(40)
            if pygame.mouse.get_pressed()[0]:
                return pygame.mouse.get_pos()
            pygame.event.get()

    def vote(self):
        pygame.event.clear()
        clique = self.posclique()
        for i in range(len(self.joueurs)):
            x = self.joueurs[i].get_x()
            y = self.joueurs[i].get_y()
            if clique[0] > x and clique[0] < x + self.joueurs[i].get_spritx() and clique[1] > y and clique[1] < y + self.joueurs[i].get_sprity():
                self.joueurs[i].plusvote()
                print(self.joueurs[i].get_nom())
                self.evenement = "null"
                return 0
        self.vote()

    def tue(self, num):
        self.joueurs[num].set_vivant(False)
        if self.joueurs[num].action():
            self.mort.append(self.joueurs[num])
            self.joueurs.pop(num)

    def get_maxvote(self):
        max = 0
        pos = 0
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_nbvote() > max:
                max = self.joueurs[i].get_nbvote()
                pos = i
        return pos

    def resetvote(self):
        for i in range(len(self.joueurs)):
            self.joueurs[i].resetvote()

    def drawP(self, win):  # dessin des personnages
        for i in range(len(self.joueurs)):
            self.joueurs[i].draw(win)

    def drawM(self, win):  # dessin des maisons
        for i in range(len(self.maisons)):
            self.maisons[i].draw(win)

    def drawV(self, win):  # dessin du nombre de vote
        for i in range(len(self.joueurs)):
            if self.joueurs[i].get_nbvote() != 0:
                self.joueurs[i].drawVote(win)

    def drawMort(self, win):
        for i in range(len(self.mort)):
            if i > 7:
                win.blit(self.mort[i].get_sprit(), (30 * (i - 8) + 750, 65))
            else:
                win.blit(self.mort[i].get_sprit(), (30 * i + 750, 20))

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
        # self.set_mouvement_on()
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

    def affiche_log(self, win):

        font = pygame.font.SysFont('freesansbold.ttf', 20)
        for i in range(len(self.log)):
            text = self.log[i]
            text_surface_obj = font.render(str(text), True, RED)
            win.blit(text_surface_obj, (20, i * 15 + 650))

        return 0

    def gestionevent(self, event):
        if event == "rentre":
            self.evenement = "rentre"
            for i in range(len(self.joueurs)):  # test de la mort de la pastéque
                if self.joueurs[i].get_nom() == "Pastèque":
                    if self.joueurs[i].get_esttue():
                        self.tue(i)
                        break

            self.set_mouvement_on()

        if event == "rentre_fin":
            # print("RENTRE  --------------------")
            self.evenement = "null"

        if event == "sort":
            # print("SORT  --------------------")
            self.evenement = "sort"
            self.set_mouvement_on()

        if event == "mort":
            # print("MORT  --------------------")
            self.tue(0)

        if event == "sort_fin":
            self.evenement = "null"

        if event == "update_pos":
            self.evenement = "update_pos"
            self.set_mouvement_on()

        if event == "update_pos_fin":
            self.evenement = "null"

        if event == "action_0":
            self.evenement = "action_0"
            self.tourjoueur(0)  # début du tour de jeu pour le joueur

        if event == "action_1":
            self.evenement = "action_1"
            self.tourjoueur(1)

        if event == "vote_0":
            self.evenement = "vote_0"
            self.tourjoueur(2) # début du tour de jeu pour le joueur

        if event == "vote_1":
            self.evenement = "vote_1"
            self.tourjoueur(3)

        if event == "vote_2":
            self.evenement = "vote_2"
            self.tourjoueur(4)

        if event == "transition_0":
            self.log.clear()
            self.log.append("-------------------------------------------")
            self.log.append("")
            self.log.append("Tout le monde a joué, il est temps de voter")
            self.log.append("")
            self.log.append("-------------------------------------------")
            self.evenement = "next"

        if event == "transition_1":
            self.log.clear()
            self.log.append("-------------------------------------------")
            self.log.append("")
            self.log.append("Tout le monde a voter, l'heure du verdicte aproche !")
            self.log.append("")
            self.log.append("-------------------------------------------")
            self.evenement = "next"

        if event == "null": #plus rien a faire, on passe au cycle suivant ou au jour suivant
            self.gestionjour()

    def gestionjour(self):
        #pygame.time.wait(2500)
        self.joueuract = 0

        print("------------")
        print(self.jour.get_cycle())
        print("------------")

        self.gestionevent(self.jour.get_cycle())
        if self.evenement == "update_pos":
            self.set_mouvement_on()
        else:
            self.jour.next()

    def tourjoueur(self, a):
        if a == 0: #pour les actions P1
            #pygame.time.wait(500)
            self.log.clear()
            self.joueurs[self.joueuract].presentation()
            self.log += self.joueurs[self.joueuract].get_log()
            self.evenement = "action_1"

        if a == 1: #pour les actions P2
            #pygame.time.wait(500)
            self.action()
            if self.evenement == "null":
                self.evenement = "action_0"
            elif self.evenement == "update_pos":
                self.set_mouvement_on()

            if self.joueuract < len(self.joueurs) - 1:
                self.joueuract += 1
            else:
                self.evenement = "update_last" #fin des actions

        if a == 2: #pour les votes P1
            self.log.clear()
            self.joueurs[self.joueuract].vote()
            self.log += self.joueurs[self.joueuract].get_log()
            self.evenement = "vote_1"

        if a == 3: #pour les votes P2
            self.vote()
            self.log.append(self.joueurs[self.joueuract].get_nom() + " a fini de voter")

            if self.evenement == "null":
                self.evenement = "vote_0"

            if self.joueuract < len(self.joueurs) - 1:
                self.joueuract += 1
            else:
                self.evenement = "null"

        if a == 4: #pour les votes P3
            self.log.clear()
            self.log.append("-------------------------------------------")
            self.log.append("")
            self.log.append(self.joueurs[self.get_maxvote()].get_nom() + " a reçu le plus de vote, il est donc élimminé !")
            self.log.append("")
            self.log.append("-------------------------------------------")
            self.tue(self.get_maxvote())
            self.evenement = "null"

