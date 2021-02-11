# Script pricipal
from Village import *
from Maison import *

# Intialisation de pygame
pygame.init()
bgJour = pygame.image.load("sprit/decorJour_gamejam2021V2.png")
bgNuit = pygame.image.load("sprit/decorNuit_gamejam2021V2.png")
clock = pygame.time.Clock()
village = Village(12)

# Création de la fenêtre

win = pygame.display.set_mode((1024, 768), pygame.RESIZABLE)

village.drawP(win)
village.drawM(win)
village.drawMort(win)



def redrawGameWindow():
    win.fill((0,0,0))
    if village.get_evenement() == "nuit":
        win.blit(bgNuit, (0, 0))
    else:
        win.blit(bgJour, (0, 0))

    village.drawM(win)

    if village.get_evenement() != "nuit":
        village.drawP(win)

    if village.get_evenement() == "affiche_vote":
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

    if village.get_evenement() == "affiche_vote": #cycle suivant
        redrawGameWindow()
        pygame.time.wait(1000)
        village.gestionevent("null")

    if village.get_evenement() == "nuit": #cycle suivant
        pygame.time.wait(3000)
        redrawGameWindow()

        village.gestionevent("null")

    if village.get_evenement() == "fin_du_jeu":
        redrawGameWindow()
        pygame.time.wait(1000)
        village.gestionevent("fin_du_jeu")



    if village.get_evenement() == "null": #si aucun événement
        redrawGameWindow()
        pygame.time.wait(2000)
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
