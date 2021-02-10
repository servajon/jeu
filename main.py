# Script pricipal
from Village import *
from Maison import *

# Intialisation de pygame
pygame.init()
clock = pygame.time.Clock()
village = Village(10)

# Création de la fenêtre

win = pygame.display.set_mode((1024, 768), pygame.RESIZABLE)

village.drawP(win)
village.drawM(win)


def redrawGameWindow():
    win.fill((0, 0, 0))
    village.drawM(win)
    village.drawP(win)
    if village.get_evenement() == "vote":
        village.drawV(win)

    pygame.display.update()


# Boucle infinie qui tourne tant que le jeu tourne
is_running = True
while is_running:
    clock.tick(40)
    if village.get_evenement() == "rentre":
        if not village.animationrentre():
            village.gestionevent("rentre_fin")

    if village.get_evenement() == "sort":
        if not village.animationsorti():
            village.gestionevent("sort_fin")

    if village.get_evenement() == "vote":
        redrawGameWindow()
        village.gestionevent("vote")

    if village.get_evenement() == "affiche_vote":
        redrawGameWindow()

    if village.get_evenement() == "action":
        village.gestionevent("action")

    if village.get_evenement() == "null": #si aucun événement
        village.gestionjour()

        keys = pygame.key.get_pressed()


    # Liste des événements ayant lieu durant cette frame
    events = pygame.event.get()
    # Quand le joueur ferme la fenêtre on arrête le jeu
    for event in events:
        if event.type == pygame.QUIT:
            is_running = False
    keys = pygame.key.get_pressed()

    # Mise à jour de la fenêtre
    redrawGameWindow()

# Arrêt de pygame
pygame.quit()
