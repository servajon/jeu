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
    pygame.display.update()


# Boucle infinie qui tourne tant que le jeu tourne
is_running = True
while is_running:
    clock.tick(40)

    if village.get_evenement() == "rentre":
        if not village.animationrentre():
            village.set_evenement("null")

    if village.get_evenement() == "sort":
        if not village.animationsorti():
            village.set_evenement("null")

    if village.get_evenement() == "null":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            village.gestionjour("sort")
        elif keys[pygame.K_RIGHT]:
            village.gestionjour("rentre")
        elif keys[pygame.K_SPACE]:
            village.gestionjour("action")

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
