# Script pricipal
from Village import *
from Maison import *

# Intialisation de pygame
pygame.init()
bg = pygame.image.load("sprit/bg.png")
clock = pygame.time.Clock()
village = Village(10)

# Création de la fenêtre

win = pygame.display.set_mode((1024, 768), pygame.RESIZABLE)

village.drawP(win)
village.drawM(win)
village.drawMort(win)



def redrawGameWindow():
    win.fill((0,0,0))
    win.blit(bg, (0, 0))
    village.drawM(win)
    village.drawP(win)
    if village.get_evenement() == "vote_2":
        village.drawV(win)
    village.drawMort(win)
    village.affiche_log(win)

    pygame.display.update()


# Boucle infinie qui tourne tant que le jeu tourne
is_running = True
while is_running:
    clock.tick(60)

    if village.get_evenement() == "start":
            village.gestionevent("start")

    if village.get_evenement() == "rentre":
        if not village.animationrentre():
            pygame.time.wait(1000)
            village.gestionevent("rentre_fin")

    if village.get_evenement() == "sort":
        if not village.animationsorti():
            pygame.time.wait(1000)
            village.gestionevent("sort_fin")

    if village.get_evenement() == "update_pos":
        if not village.animationsorti():
            village.gestionevent("update_pos_fin")

    if village.get_evenement() == "action_0":
        redrawGameWindow()
        village.gestionevent("action_0")

    if village.get_evenement() == "action_1":
        redrawGameWindow()
        village.gestionevent("action_1")

    if village.get_evenement() == "vote_0":
        redrawGameWindow()
        pygame.time.wait(1000)
        village.gestionevent("vote_0")

    if village.get_evenement() == "vote_1":
        redrawGameWindow()
        village.gestionevent("vote_1")

    if village.get_evenement() == "vote_2":
        redrawGameWindow()
        pygame.time.wait(1000)
        village.gestionevent("vote_2")

    if village.get_evenement() == "next":
        redrawGameWindow()
        pygame.time.wait(1000)
        village.gestionevent("null")

    if village.get_evenement() == "update_last": #cycle suivant
        redrawGameWindow()
        pygame.time.wait(1000)
        village.gestionevent("null")

    if village.get_evenement() == "null": #si aucun événement
        redrawGameWindow()
        pygame.time.wait(1000)
        village.gestionjour()


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
