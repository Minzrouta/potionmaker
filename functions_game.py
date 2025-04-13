import random
import pygame

class ball:                         #Crée une classe ball prenant comme attribut une couleur
    def __init__(self, couleur):
        self.couleur = couleur

class tube:                         #Crée une classe tube prenant comme attribut une liste de d'instances de la classe ball
    def __init__(self, elements):
        self.elements = elements

    def empiler(self, x):           #empile
        self.elements.append(x)
    
    def depiler(self):              #dépile
        self.elements.pop()

    def get_len(self):              #renvoie le nombre de boules que contient le tube
        return len(self.elements)

    def check(self):                #Vérifie si le tube est plein avec des boules de même couleur (renvoie True ou False en fonction)
        if self.get_len() == 4 and self.elements[0].couleur == self.elements[1].couleur == self.elements[2].couleur == self.elements[3].couleur :
            return True
        return False
 
def check_all(nbr_tubes):           #Vérifie si tous les tubes sont remplis d'une meme couleur
    x=0
    for i in range(nbr_tubes):
        if list_tubes["tube"+str(i+1)].check() == True : x+=1   #Parcours tous les tubes et rajoute 1 à x si le tube est validé
    if x == nbr_tubes-2 :           #si x est égal au nombre de couleurs renvoie True
        return True


def select(tube, ball_select):      #retire la ball au sommet du tube et la définie comme balle selectionée et la renvoie
    global last_tube
    last_tube = list_tubes["tube"+str(tube)]
    top_ball = list_tubes["tube"+str(tube)].elements[-1]
    list_tubes["tube"+str(tube)].depiler()
    ball_select = top_ball
    return ball_select
    
def drop(tube, ball_select):        #place la ball_select au sommet du tube choisi
    list_tubes["tube"+str(tube)].empiler(ball_select)
    ball_select = None
    return ball_select
    
def possible_move(tube, ball_select):   #Vérifie si la balle peut etre placée sur le tube selectioné
    if list_tubes["tube"+str(tube)] == last_tube:   #Si le tube selectioné est le tube d'origine de la ball renvoie true
        return True
    if list_tubes["tube"+str(tube)].get_len() == 4 :    #Si le tube est plein renvoie False
        return False
    elif list_tubes["tube"+str(tube)].get_len() != 0 and ball_select.couleur != list_tubes["tube"+str(tube)].elements[-1].couleur :     #Si le tube n'est pas vide et que la couleur au sommet ne correspond pas renvoie False
        return False
    return True     #Si les conditions ne sont pas remplies renvoie True

def init_jeu_rand(nbr_tubes,color_list) :   #Initialise un niveau random
    global list_tubes
    global list_boules
    random.shuffle(color_list)  #mélange la liste des couleurs
    list_tubes = {}
    list_boules = {}
    for i in range(1,nbr_tubes+1):  #Crée autant d'instances de la classe tube que nbr_tubes
        list_tubes["tube{0}".format(i)] = tube([])
    for i in range(len(color_list)):    #Crée 4 instances de boules pour chaque couleurs
        for j in range(1,5):
            list_boules[f"boule{str(i)+str(j)}"] = ball(color_list[i])
    deja_eu = []
    for i in range(1,len(list_tubes)-1):    #Parcours tous les tubes-2 et place 4 boules aléatoires dans chacun
        for j in range(4):
            valide = 0
            while valide == 0:  #tant que la boule choisie aléatoirement fait partie des boules "deja eu", en choisit une autre aléatoirement
                boule_rand = str(random.randrange(nbr_tubes-2))+str(random.randrange(1,5))
                if boule_rand not in deja_eu:   #si la boule choisit n'a pas encore été ajouté à la liste deja_eu, l'ajoute au tube
                    deja_eu.append(boule_rand)
                    valide = 1
                    list_tubes["tube"+str(i)].empiler(list_boules["boule"+boule_rand])
    return (list_tubes) #renvoie la liste des tubes remplis par les balles

def init_jeu_level(nbr_tubes,level) :   #Initialise un niveau prédéfini
    global list_tubes
    list_tubes = {}
    for i in range(1,nbr_tubes+1):      #Crée autant d'instances de la classe tube que nbr_tubes
        list_tubes["tube{0}".format(i)] = tube([])
    for i in range(len(level)-2):       
        for j in range(4):          #Parcours tous les tubes-2 et place les 4 boules avec les couleurs correspondant au niveau choisi (fichier levels.json)
            c = pygame.Color(0, 0, 0)
            c.hsla = eval(level[i][j])      #Définie c comme la couleur correspondant
            list_tubes["tube"+str(i+1)].empiler(ball(c))    #ajoute une instance de ball au tube
    return (list_tubes) #renvoie la liste des tubes remplis par les balles