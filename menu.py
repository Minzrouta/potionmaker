import pygame
import json
import random
from functions_display import *
from game_rand import *
from game_levels import *
from worlds import *


pygame.init()   #initialise la fenêtre
pygame.display.set_caption('Potion maker - Menu')   #change le nom de la fenetre
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)     #Met la fenetre en fullscreen
if screen.get_size()[0]>1920 or screen.get_size()[1] > 1080:    #Si l'écran est plus grand que 1920x1080 : mode fenetré 1920:1080
    screen = pygame.display.set_mode((1920, 1080))
ratio = get_ratio(screen)   #permet d'obtenir le ratio pour adapter la fenetre à la taille de l'écran

bg = resize(pygame.image.load("Assets/bg/bg_menu_blank.png"),screen)    #Import des images
bg_lvl_1 = resize(pygame.image.load("Assets/bg/bg_1.png"),screen)
bg_lvl_2 = resize(pygame.image.load("Assets/bg/bg_2.png"),screen)
bg_lvl_3 = resize(pygame.image.load("Assets/bg/bg_3.png"),screen)
bg_lvl_4 = resize(pygame.image.load("Assets/bg/bg_4.png"),screen)
bg_list = [bg_lvl_1,bg_lvl_2,bg_lvl_3,bg_lvl_4]     
settings_img = resize(pygame.image.load("Assets/buttons/icons/settings.png"),screen)
settings_pressed_img = resize(pygame.image.load("Assets/buttons/icons/settings_pressed.png"),screen)
close_img = resize(pygame.image.load("Assets/buttons/icons/close.png"),screen)
close_pressed_img = resize(pygame.image.load("Assets/buttons/icons/close_pressed.png"),screen)
menu_settings_img = resize(pygame.image.load("Assets/buttons/icons/menu_settings.png"),screen)
menu_settings_pressed_img = resize(pygame.image.load("Assets/buttons/icons/menu_settings_pressed.png"),screen)
ranking_img = resize(pygame.image.load("Assets/buttons/icons/ranking.png"),screen)
ranking_pressed_img = resize(pygame.image.load("Assets/buttons/icons/ranking_pressed.png"),screen)
about_img = resize(pygame.image.load("Assets/buttons/icons/about.png"),screen)
about_pressed_img = resize(pygame.image.load("Assets/buttons/icons/about_pressed.png"),screen)
randomlevel_img = resize(pygame.image.load("Assets/buttons/random_level.png"),screen)
randomlevel_pressed_img = resize(pygame.image.load("Assets/buttons/random_level_pressed.png"),screen)
worldcake_logo = resize(pygame.image.load("Assets/menu/world_cake.png"),screen)
worldcake_logo_small = resize(pygame.transform.scale(pygame.image.load("Assets/menu/world_cake.png"),(300,240)),screen) 

menu_settings = False


while True:
    lvl_file = open("levels.json", "r") #ouvre le levels.json pour récupérer les maps des niveaux
    levels = json.load(lvl_file)
    lvl_file.close()
    mouse = pygame.mouse.get_pos()  #position de la souris
    screen.blit(bg, (0, 0))         #affichage du fond

    if 100//ratio <= mouse[0] <= 400//ratio and 60//ratio <= mouse[1] <= 300//ratio :  #Affichage bouton Monde 1
        screen.blit(worldcake_logo, (50//ratio, 20//ratio))
    else :
        screen.blit(worldcake_logo_small, (100//ratio, 60//ratio))

    if 580//ratio <= mouse[0] <= 980//ratio and 100//ratio <= mouse[1] <= 420//ratio :  #Affichage bouton Monde 2
        worldtree_logo = resize(pygame.image.load("Assets/menu/world_tree.png"),screen)
        if levels["worlds"][1]["status"]=="locked": #si le niveau n'est pas débloqué
            worldtree_logo.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT) #rend le bouton transparent
        screen.blit(worldtree_logo, (530//ratio, 60//ratio))
    else :
        worldtree_logo_small = resize(pygame.transform.scale(pygame.image.load("Assets/menu/world_tree.png"),(300,240)),screen) 
        if levels["worlds"][1]["status"]=="locked": #si le niveau n'est pas débloqué
            worldtree_logo_small.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)   #rend le bouton transparent
        screen.blit(worldtree_logo_small, (580//ratio, 100//ratio))

    if 350//ratio <= mouse[0] <= 650//ratio and 500//ratio <= mouse[1] <= 740//ratio :  #Affichage bouton Monde 3
        worldskycastle_logo = resize(pygame.image.load("Assets/menu/world_skycastle.png"),screen)
        if levels["worlds"][2]["status"]=="locked": #si le niveau n'est pas débloqué
            worldskycastle_logo.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)    #rend le bouton transparent
        screen.blit(worldskycastle_logo, (300//ratio, 460//ratio)) 
    else :
        worldskycastle_logo_small = resize(pygame.transform.scale(pygame.image.load("Assets/menu/world_skycastle.png"),(300,240)),screen) 
        if levels["worlds"][2]["status"]=="locked": #si le niveau n'est pas débloqué
            worldskycastle_logo_small.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)  #rend le bouton transparent
        screen.blit(worldskycastle_logo_small, (350//ratio, 500//ratio))
    

    if 750//ratio <= mouse[0] <= 1150//ratio and 600//ratio <= mouse[1] <= 1000//ratio :  #Affichage bouton Monde 4
        worldcastle_logo = resize(pygame.image.load("Assets/menu/world_castle.png"),screen)
        if levels["worlds"][3]["status"]=="locked": #si le niveau n'est pas débloqué
            worldcastle_logo.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)   #rend le bouton transparent
        screen.blit(worldcastle_logo, (700//ratio, 550//ratio)) 
    else :
        worldcastle_logo_small = resize(pygame.transform.scale(pygame.image.load("Assets/menu/world_castle.png"),(300,240)),screen) 
        if levels["worlds"][3]["status"]=="locked": #si le niveau n'est pas débloqué
            worldcastle_logo_small.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT) #rend le bouton transparent
        screen.blit(worldcastle_logo_small, (750//ratio, 600//ratio))

    if 1800//ratio <= mouse[0] <= 1864//ratio and 970//ratio <= mouse[1] <= 1034//ratio :  #Affichage Bouton menu_settings
        screen.blit(menu_settings_pressed_img, (1800//ratio, 970//ratio)) 
    else : screen.blit(menu_settings_img, (1800//ratio, 970//ratio))

    if menu_settings == True :
        if 1700//ratio <= mouse[0] <= 1764//ratio and 970//ratio <= mouse[1] <= 1034//ratio :  #Affichage Bouton settings
            screen.blit(settings_pressed_img, (1700//ratio, 970//ratio)) 
        else : screen.blit(settings_img, (1700//ratio, 970//ratio))

        if 1600//ratio <= mouse[0] <= 1664//ratio and 970//ratio <= mouse[1] <= 1034//ratio :  #Affichage Bouton ranking
            screen.blit(ranking_pressed_img, (1600//ratio, 970//ratio)) 
        else : screen.blit(ranking_img, (1600//ratio, 970//ratio))

        if 1500//ratio <= mouse[0] <= 1564//ratio and 970//ratio <= mouse[1] <= 1034//ratio :  #Affichage Bouton about
            screen.blit(about_pressed_img, (1500//ratio, 970//ratio)) 
        else : screen.blit(about_img, (1500//ratio, 970//ratio))

    if 1800//ratio <= mouse[0] <= 1864//ratio and 56//ratio <= mouse[1] <= 120//ratio :  #Affichage Bouton close
        screen.blit(close_pressed_img, (1800//ratio, 56//ratio)) 
    else : screen.blit(close_img, (1800//ratio, 56//ratio))

    if 50//ratio <= mouse[0] <= 350//ratio and 946//ratio <= mouse[1] <= 1030//ratio :  #Affichage Bouton random level
        screen.blit(randomlevel_pressed_img, (50//ratio, 946//ratio)) 
    else : screen.blit(randomlevel_img, (50//ratio, 946//ratio))


    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 100//ratio <= mouse[0] <= 400//ratio and 60//ratio <= mouse[1] <= 300//ratio :       #fonctionnement bouton monde 1
                world_menu(screen,1,ratio,levels)
            elif 580//ratio <= mouse[0] <= 980//ratio and 100//ratio <= mouse[1] <= 420//ratio :    #fonctionnement bouton monde 2
                if levels["worlds"][1]["status"]!="locked":
                    world_menu(screen,2,ratio,levels)
            elif 350//ratio <= mouse[0] <= 650//ratio and 500//ratio <= mouse[1] <= 740//ratio :    #fonctionnement bouton monde 3
                if levels["worlds"][2]["status"]!="locked":
                    world_menu(screen,3,ratio,levels)
            elif 750//ratio <= mouse[0] <= 1150//ratio and 600//ratio <= mouse[1] <= 1000//ratio :  #fonctionnement bouton monde 4
                if levels["worlds"][3]["status"]!="locked":
                    world_menu(screen,4,ratio,levels)
            elif 1800//ratio <= mouse[0] <= 1864//ratio and 970//ratio <= mouse[1] <= 1034//ratio : #fonctionnement bouton settings
                menu_settings = not menu_settings
            elif 50//ratio <= mouse[0] <= 350//ratio and 946//ratio <= mouse[1] <= 1030//ratio :    #fonctionnement bouton niveau random
                game_rand(screen,random.randint(0,360),random.randint(2,7)*2,random.choice(bg_list),ratio)
            elif 1800//ratio <= mouse[0] <= 1864//ratio and 56//ratio <= mouse[1] <= 120//ratio :   #fonctionnement bouton close
                pygame.quit()
            elif menu_settings == True :    #fonctionnement boutons settings/ranking/about
                if 1700//ratio <= mouse[0] <= 1764//ratio and 970//ratio <= mouse[1] <= 1034//ratio :
                    print("settings")
                if 1600//ratio <= mouse[0] <= 1664//ratio and 970//ratio <= mouse[1] <= 1034//ratio :
                    print("ranking")
                if 1500//ratio <= mouse[0] <= 1564//ratio and 970//ratio <= mouse[1] <= 1034//ratio :
                    print("about")

    for ev in pygame.event.get(): #permet de alt f4
        if ev.type == pygame.QUIT:  
            pygame.quit()
    pygame.display.update()