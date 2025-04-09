#Créer les fonctions de déplacements bas, droite et gauche
# L setheading
# H setheading
#Écrire les écoutes pour ces mêmes mouvements

# Initialisation de notre tortue dans la variable t

import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("Déplacement avec les flèches")
t = turtle.Turtle()
# Fonctions pour déplacer la tortue
        # Oriente vers le haut
def haut():
    t.setheading(90)  
    t.forward(20)
        # Oriente vers le bas
def bas() :
    t.setheading(270) 
    t.forward(20)
        # Oriente vers la droite
def droite() :
    t.setheading(0)
    t.forward(20)
        # Oriente vers la gauche
def gauche() :
    t.setheading(180)
    t.forward(20)