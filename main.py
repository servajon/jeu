# Script pricipal
import pygame
from FL import *
from Village import *

# Intialisation de pygame
pygame.init()


village = Village(8)



# Création de la fenêtre

win = pygame.display.set_mode((1024, 768), pygame.RESIZABLE)

village.draw(win)



# Boucle infinie qui tourne tant que le jeu tourne
is_running = True
while is_running:

    # Liste des événements ayant lieu durant cette frame
    events = pygame.event.get()
    # Quand le joueur ferme la fenêtre on arrête le jeu
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False

    # Mise à jour de la fenêtre
    pygame.display.flip()

# Arrêt de pygame
pygame.quit()