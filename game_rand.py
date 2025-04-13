import pygame
from functions_game import *
from functions_display import *


def game_rand(screen,couleur_choisie,nbr_tubes,bg,ratio):   #voir annotations de game_levels.py car similaire
    pygame.display.set_caption('Potion maker - niveau 1')   
    restart_but = resize(pygame.image.load("Assets/buttons/icons/restart.png"),screen)
    restart_but2 = resize(pygame.image.load("Assets/buttons/icons/restart_pressed.png"),screen)
    tube_img = resize(pygame.image.load("Assets/tubetest.png"),screen)
    win_img = resize(pygame.image.load("Assets/win.png"),screen)
    home_img = resize(pygame.image.load("Assets/buttons/icons/home.png"),screen)
    home_pressed_img = resize(pygame.image.load("Assets/buttons/icons/home_pressed.png"),screen)
    close_img = resize(pygame.image.load("Assets/buttons/icons/close.png"),screen)
    close_pressed_img = resize(pygame.image.load("Assets/buttons/icons/close_pressed.png"),screen)

    list_couleur=[]

    for i in range(couleur_choisie,couleur_choisie+1+(nbr_tubes-3)*25,25):
        c = pygame.Color(0, 0, 0)
        c.hsla = (i%360, 95, 70, 0)
        list_couleur.append(c)

    win = 0
    gaming=1

    if nbr_tubes > 7:
        tube_img = pygame.transform.scale(tube_img, (int(100//ratio), int(300//ratio)))

    list_tubes = init_jeu_rand(nbr_tubes, list_couleur)
    print(list_tubes)
    ball_select = None

    while gaming == 1:
        mouse = pygame.mouse.get_pos()
        screen.blit(bg, (0, 0))

        for i in range(nbr_tubes) :  #Affichage tubes / boules
            if nbr_tubes<8:
                for j in range(list_tubes["tube"+str(i+1)].get_len()):
                    pygame.draw.rect(screen, list_tubes["tube"+str(i+1)].elements[j].couleur, pygame.Rect((((i+1)*200+100*(8-nbr_tubes))+13)//ratio, (680-j*89)//ratio, 122//ratio, 90//ratio))
                screen.blit(tube_img, (((i+1)*200+100*(8-nbr_tubes))//ratio,350//ratio))
            elif nbr_tubes<17:
                for j in range(list_tubes["tube"+str(i+1)].get_len()):
                    pygame.draw.rect(screen, list_tubes["tube"+str(i+1)].elements[j].couleur, pygame.Rect((((i//2+1)*150+75*(8-nbr_tubes//2))+250)//ratio, (420+(i%2)*400-j*66)//ratio, 80//ratio, 66//ratio))
                screen.blit(tube_img, (((i//2+1)*150+240+75*(8-nbr_tubes//2))//ratio,((i%2)*400+200)//ratio))
        if ball_select != None:
            if nbr_tubes<8: pygame.draw.rect(screen, ball_select.couleur, pygame.Rect(mouse[0]-45,mouse[1]-31, 140//ratio, 100//ratio))
            if 7<nbr_tubes<17: pygame.draw.rect(screen, ball_select.couleur, pygame.Rect(mouse[0]-45,mouse[1]-31, 94//ratio, 66//ratio))

        if 30//ratio <= mouse[0] <= 94//ratio and 970//ratio <= mouse[1] <= 1034//ratio :  #Bouton restart
            screen.blit(restart_but2, (30//ratio, 970//ratio)) 
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    list_tubes = init_jeu_rand(nbr_tubes, list_couleur)
                    win = 0
                    ball_select = None
        else : screen.blit(restart_but, (30//ratio, 970//ratio))
        
        if 1800//ratio <= mouse[0] <= 1864//ratio and 970//ratio <= mouse[1] <= 1034//ratio :  #Bouton leave
            screen.blit(home_pressed_img, (1800//ratio, 970//ratio)) 
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    gaming=0
        else : screen.blit(home_img, (1800//ratio, 970//ratio))

        if 1800//ratio <= mouse[0] <= 1864//ratio and 56//ratio <= mouse[1] <= 120//ratio :  #Bouton close
            screen.blit(close_pressed_img, (1800//ratio, 56//ratio)) 
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
        else : screen.blit(close_img, (1800//ratio, 56//ratio))
    


        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if nbr_tubes<8:
                    if (200+100*(8-nbr_tubes))//ratio <= mouse[0] <= (200*nbr_tubes+200+100*(8-nbr_tubes))//ratio and 350//ratio <= mouse[1] <= 800//ratio and win == 0 : 
                        tube_selec = int((mouse[0]-((200+100*(8-nbr_tubes))//ratio))/(200//ratio))+1
                        print("tube"+str(tube_selec))
                        if ball_select == None :
                            if len(list_tubes["tube"+str(tube_selec)].elements) > 0:
                                ball_select = select(tube_selec, ball_select)
                        else :
                            if possible_move(tube_selec, ball_select) == True :
                                ball_select=drop(tube_selec, ball_select)
                                if check_all(nbr_tubes) == True :
                                    win = 1
                elif nbr_tubes<17:
                    if (400+75*(8-nbr_tubes//2))//ratio <= mouse[0] <= (150*(nbr_tubes//2)+350+75*(8-nbr_tubes//2))//ratio and 200//ratio <= mouse[1] <= 886//ratio and win == 0 : 
                        if 200//ratio <= mouse[1] <= 542//ratio:
                            tube_selec = int((mouse[0]-(200+75*(8-nbr_tubes//2))//ratio)/(150//ratio))*2-1
                        if 543//ratio <= mouse[1] <= 886//ratio:
                            tube_selec = int((mouse[0]-(200+75*(8-nbr_tubes//2))//ratio)/(150//ratio))*2
                        print("tube"+str(tube_selec))
                        if ball_select == None :
                            if len(list_tubes["tube"+str(tube_selec)].elements) > 0:
                                ball_select = select(tube_selec, ball_select)
                        else :
                            if possible_move(tube_selec, ball_select) == True :
                                ball_select=drop(tube_selec, ball_select)
                                if check_all(nbr_tubes) == True :
                                    win = 1

            if ev.type == pygame.QUIT:  
                pygame.quit()


        if win == 1 : #Affichage fin
            screen.blit(win_img, (560//ratio,240//ratio))

        pygame.display.update()

