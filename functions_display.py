import pygame

def resize(image, screen):                  #Adapte la taille d'une image pour qu'elle corresponde à la résolution de l'écran
    ratio = get_ratio(screen)
    image_x=image.get_width()
    image_y=image.get_height()
    image = pygame.transform.scale(image, (int(image_x//ratio), int(image_y//ratio)))
    return image

def get_ratio(screen):                      #Renvoie le ratio entre la résolution de l'écran de l'utilisateur et une résolution 1920/1080
    ratio = 1920/screen.get_size()[0]
    return ratio
