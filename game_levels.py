import pygame
import json
from functions_game import *
from functions_display import *

def game_lvl(screen,nbr_tubes,bg,ratio,levels,world,lvl_nbr):
    pygame.display.set_caption('Potion maker - niveau 1')   #définie le nom de la fenêtre
    restart_but = resize(pygame.image.load("Assets/buttons/icons/restart.png"),screen)              #import de toutes les images
    restart_but2 = resize(pygame.image.load("Assets/buttons/icons/restart_pressed.png"),screen)
    tube_img = resize(pygame.image.load("Assets/tubetest.png"),screen)
    win_img = resize(pygame.image.load("Assets/win.png"),screen)
    home_img = resize(pygame.image.load("Assets/buttons/icons/home.png"),screen)
    home_pressed_img = resize(pygame.image.load("Assets/buttons/icons/home_pressed.png"),screen)
    close_img = resize(pygame.image.load("Assets/buttons/icons/close.png"),screen)
    close_pressed_img = resize(pygame.image.load("Assets/buttons/icons/close_pressed.png"),screen)

    win = 0             #initialise les variables
    gaming=1 
    ball_select = None

    if nbr_tubes > 7: #si il y a plus de 7 tubes réduit la taille de l'image des tubes afin de faire 2 lignes
        tube_img = pygame.transform.scale(tube_img, (int(100//ratio), int(300//ratio))) #(les divisions par ratio permettent d'adapter les coordonnées à la taille de l'écran)

    list_tubes = init_jeu_level(nbr_tubes,levels["worlds"][world-1]["levels"][lvl_nbr]["map"])  #initialise le jeu en fonction du niveau choisi dans levels.json

    while gaming == 1:  #tant que le jeu est en cours
        mouse = pygame.mouse.get_pos()      #définie la position de la souris
        screen.blit(bg, (0, 0))             #affiche l'image de fond

        for i in range(nbr_tubes) :  #Affichage tubes / boules
            if nbr_tubes<8: #Affichage sur 1 ligne
                for j in range(list_tubes["tube"+str(i+1)].get_len()):  #parcours tous les tubes, puis toutes les boules de chaque tube et les affiche en fonction de leur position dans la liste et de leur couleur
                    pygame.draw.rect(screen, list_tubes["tube"+str(i+1)].elements[j].couleur, pygame.Rect((((i+1)*200+100*(8-nbr_tubes))+13)//ratio, (680-j*89)//ratio, 122//ratio, 90//ratio))
                screen.blit(tube_img, (((i+1)*200+100*(8-nbr_tubes))//ratio,350//ratio))    #affiche l'image de tube 
            elif nbr_tubes<17:  #Affichage sur 2 lignes
                for j in range(list_tubes["tube"+str(i+1)].get_len()):  #parcours tous les tubes, puis toutes les boules de chaque tube et les affiche en fonction de leur position dans la liste et de leur couleur
                    pygame.draw.rect(screen, list_tubes["tube"+str(i+1)].elements[j].couleur, pygame.Rect((((i//2+1)*150+75*(8-nbr_tubes//2))+250)//ratio, (420+(i%2)*400-j*66)//ratio, 80//ratio, 66//ratio))
                screen.blit(tube_img, (((i//2+1)*150+240+75*(8-nbr_tubes//2))//ratio,((i%2)*400+200)//ratio))   #affiche l'image de tube 
        if ball_select != None: #Affiche la boule selectionnée sur le curseur
            if nbr_tubes<8: pygame.draw.rect(screen, ball_select.couleur, pygame.Rect(mouse[0]-45,mouse[1]-31, 140//ratio, 100//ratio))
            if 7<nbr_tubes<17: pygame.draw.rect(screen, ball_select.couleur, pygame.Rect(mouse[0]-45,mouse[1]-31, 94//ratio, 66//ratio))

        if 30//ratio <= mouse[0] <= 94//ratio and 970//ratio <= mouse[1] <= 1034//ratio :  #Bouton restart
            screen.blit(restart_but2, (30//ratio, 970//ratio))  #Si la souris est placée sur le bouton affiche l'image du bouton pressé
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:               #si il y a clic, réinitialise le jeu et réinitialise les variables
                    list_tubes = init_jeu_level(nbr_tubes,levels["worlds"][world-1]["levels"][lvl_nbr]["map"])
                    win = 0
                    ball_select = None
        else : screen.blit(restart_but, (30//ratio, 970//ratio))    #Si la souris n'est pas placée sur le bouton, affiche le bouton non pressé
        
        if 1800//ratio <= mouse[0] <= 1864//ratio and 970//ratio <= mouse[1] <= 1034//ratio :  #Bouton leave
            screen.blit(home_pressed_img, (1800//ratio, 970//ratio))    
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:       #si il y a clic, définie le jeu comme arreté = retour au menu
                    gaming=0
        else : screen.blit(home_img, (1800//ratio, 970//ratio))

        if 1800//ratio <= mouse[0] <= 1864//ratio and 56//ratio <= mouse[1] <= 120//ratio :  #Bouton close
            screen.blit(close_pressed_img, (1800//ratio, 56//ratio)) 
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:   #si il y a clic, ferme la fenêtre
                    pygame.quit()
        else : screen.blit(close_img, (1800//ratio, 56//ratio))
    


        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if nbr_tubes<8:
                    if (200+100*(8-nbr_tubes))//ratio <= mouse[0] <= (200*nbr_tubes+200+100*(8-nbr_tubes))//ratio and 350//ratio <= mouse[1] <= 800//ratio and win == 0 : #Si la souris est sur les tubes et que le jeu n'est pas gagné
                        tube_selec = int((mouse[0]-((200+100*(8-nbr_tubes))//ratio))/(200//ratio))+1    #définie le tube cliqué avec des calculs de coordonées très embettants à expliquer
                        if ball_select == None :    #Si aucune balle n'est selectionnée, selectionne celle du haut du tube
                            if len(list_tubes["tube"+str(tube_selec)].elements) > 0:    #Si le tube n'est pas vide
                                ball_select = select(tube_selec, ball_select)
                        else :  #Si une balle est selectionnée 
                            if possible_move(tube_selec, ball_select) == True : #Si le placement est possible
                                ball_select=drop(tube_selec, ball_select)   #place la balle au sommet et définie ball_select = None
                                if check_all(nbr_tubes) == True :   #Vérifie si le jeu et gagné
                                    win = 1
                elif nbr_tubes<17:
                    if (400+75*(8-nbr_tubes//2))//ratio <= mouse[0] <= (150*(nbr_tubes//2)+350+75*(8-nbr_tubes//2))//ratio and 200//ratio <= mouse[1] <= 886//ratio and win == 0 : #Si la souris est sur les tubes et que le jeu n'est pas gagné
                        if 200//ratio <= mouse[1] <= 542//ratio:    #ligne 1
                            tube_selec = int((mouse[0]-(200+75*(8-nbr_tubes//2))//ratio)/(150//ratio))*2-1  #définie le tube cliqué avec des calculs de coordonées très embettants à expliquer
                        if 543//ratio <= mouse[1] <= 886//ratio:    #ligne 2
                            tube_selec = int((mouse[0]-(200+75*(8-nbr_tubes//2))//ratio)/(150//ratio))*2    #définie le tube cliqué avec des calculs de coordonées très embettants à expliquer
                        if ball_select == None :    #Si aucune balle n'est selectionnée, selectionne celle du haut du tube
                            if len(list_tubes["tube"+str(tube_selec)].elements) > 0:    #Si le tube n'est pas vide
                                ball_select = select(tube_selec, ball_select)
                        else :  #si une balle est selectionnée
                            if possible_move(tube_selec, ball_select) == True : #Si le placement est possible
                                ball_select=drop(tube_selec, ball_select)   #place la balle au sommet et définie ball_select = None
                                if check_all(nbr_tubes) == True :   #Vérifie si le jeu et gagné
                                    win = 1
                                    

            if ev.type == pygame.QUIT:  #permet de alt f4/de fermer la fenêtre
                pygame.quit()


        if win == 1 : #Si le niveau est gagné
            screen.blit(win_img, (560//ratio,240//ratio))   #affiche l'écran de fin
            lvl_file = open("levels.json", "r")             #ouvre le fichier levels.json
            json_object = json.load(lvl_file)               #crée une copie du fichier
            lvl_file.close()
            if len(levels["worlds"][world-1]["levels"]) == lvl_nbr+1 :  #si dernier niveau du monde, débloque le monde suivant et définie le niveau comme "done"
                json_object["worlds"][world-1]["levels"][lvl_nbr]["status"] = "done"
                json_object["worlds"][world-1]["status"] = "done"
                json_object["worlds"][world]["status"] = "unlocked"
            elif levels["worlds"][world-1]["levels"][lvl_nbr+1]["status"] == "locked" : #sinon si le niveau suivant n'est pas débloqué, définie le niveau fait comme "done" et le suivant comme "unlocked"
                json_object["worlds"][world-1]["levels"][lvl_nbr]["status"] = "done"
                json_object["worlds"][world-1]["levels"][lvl_nbr+1]["status"] = "unlocked"
            lvl_file = open("levels.json", "w")
            json.dump(json_object, lvl_file)                #remplace le fichier par la copie modifiée
            lvl_file.close()                                #ferme le fichier levels.json


        pygame.display.update()