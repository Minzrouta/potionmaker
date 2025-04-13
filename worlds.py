from functions_display import *
import pygame
from game_levels import *
import json

def world_menu(screen,world,ratio,levels):
    pygame.display.set_caption('Potion maker - World '+str(world)) #nom de la fenêtre
    bg = resize(pygame.image.load("Assets/bg/bg_menu_blank.png"),screen)            #import images
    home_img = resize(pygame.image.load("Assets/buttons/icons/home.png"),screen)
    home_pressed_img = resize(pygame.image.load("Assets/buttons/icons/home_pressed.png"),screen)
    close_img = resize(pygame.image.load("Assets/buttons/icons/close.png"),screen)
    close_pressed_img = resize(pygame.image.load("Assets/buttons/icons/close_pressed.png"),screen)
    locked_img = resize(pygame.image.load("Assets/buttons/icons/circle_empty_transparent.png"),screen)
    unlocked_img = resize(pygame.image.load("Assets/buttons/icons/circle_empty.png"),screen)
    done_img = resize(pygame.image.load("Assets/buttons/icons/circle_filled.png"),screen)
    status_dict = {"locked" : locked_img, "unlocked" : unlocked_img, "done" : done_img}
    bg_lvl_1 = resize(pygame.image.load("Assets/bg/bg_1.png"),screen)
    bg_lvl_2 = resize(pygame.image.load("Assets/bg/bg_2.png"),screen)
    bg_lvl_3 = resize(pygame.image.load("Assets/bg/bg_3.png"),screen)
    bg_lvl_4 = resize(pygame.image.load("Assets/bg/bg_4.png"),screen)
    bg_list = [bg_lvl_1,bg_lvl_2,bg_lvl_3,bg_lvl_4]

    world_menu_display=1
    while world_menu_display == 1:
        mouse = pygame.mouse.get_pos()  #position souris
        screen.blit(bg, (0, 0))         #background
        lvl_file = open("levels.json", "r") #ouvre le fichier levels.json pour récupérer les niveaux
        levels = json.load(lvl_file)
        lvl_file.close()

        for i in range(len(levels["worlds"][world-1]["levels"])):   #Affiche les icones de chaque niveaux et les lignes qui les relient
            x_pos = levels["worlds"][world-1]["levels"][i]["button"][0]//ratio
            y_pos = levels["worlds"][world-1]["levels"][i]["button"][1]//ratio
            if i != len(levels["worlds"][world-1]["levels"])-1 :
                if levels["worlds"][world-1]["levels"][i]["status"] == "unlocked" or levels["worlds"][world-1]["levels"][i]["status"] == "locked"  :
                    pygame.draw.line(screen, pygame.Color(255, 255, 255), (x_pos+32//ratio, y_pos+32//ratio), ((levels["worlds"][world-1]["levels"][i+1]["button"][0]+32)//ratio,(levels["worlds"][world-1]["levels"][i+1]["button"][1]+32)//ratio), 3)
                else :
                    pygame.draw.line(screen, pygame.Color(0, 0 , 0), (x_pos+32//ratio, y_pos+32//ratio), ((levels["worlds"][world-1]["levels"][i+1]["button"][0]+32)//ratio,(levels["worlds"][world-1]["levels"][i+1]["button"][1]+32)//ratio), 3)
            screen.blit(status_dict[levels["worlds"][world-1]["levels"][i]["status"]], (x_pos, y_pos))  


        if 1800//ratio <= mouse[0] <= 1864//ratio and 970//ratio <= mouse[1] <= 1034//ratio :  #Affichage Bouton leave
            screen.blit(home_pressed_img, (1800//ratio, 970//ratio)) 
        else : screen.blit(home_img, (1800//ratio, 970//ratio))

        if 1800//ratio <= mouse[0] <= 1864//ratio and 56//ratio <= mouse[1] <= 120//ratio :  #Affichage Bouton close
            screen.blit(close_pressed_img, (1800//ratio, 56//ratio))
        else : screen.blit(close_img, (1800//ratio, 56//ratio))



        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:  #permet de fermer la fenetre
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(levels["worlds"][world-1]["levels"])):   
                    x_but = levels["worlds"][world-1]["levels"][i]["button"][0]//ratio
                    y_but = levels["worlds"][world-1]["levels"][i]["button"][1]//ratio
                    if x_but <= mouse[0] <= x_but+64 and y_but <= mouse[1] <= y_but+64 :    #si le clic se trouve sur une des icones de niveaux
                        if levels["worlds"][world-1]["levels"][i]["status"] == "done" or levels["worlds"][world-1]["levels"][i]["status"] == "unlocked" :   #si le niveau est fait ou débloqué
                            game_lvl(screen,len(levels["worlds"][world-1]["levels"][i]["map"]),bg_list[world-1],ratio,levels,world,i)   #lance le niveau
                if 1800//ratio <= mouse[0] <= 1864//ratio and 970//ratio <= mouse[1] <= 1034//ratio :   #bouton leave
                    world_menu_display=0
                elif 1800//ratio <= mouse[0] <= 1864//ratio and 56//ratio <= mouse[1] <= 120//ratio :   #bouton close
                    pygame.quit()


        pygame.display.update()