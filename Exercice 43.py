#BANKOLE Nathanaël, Master 1 IA
import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def draw(self):
        t = turtle.Turtle()
        t.speed(0)

        for _ in range(2):
            t.forward(self.longueur)
            t.right(90)
            t.forward(self.largeur)
            t.right(90)

        turtle.done()

class Square(Rectangle):
    def __init__(self, cote, inclinaison=30):
        super().__init__(cote, cote)
        self.inclinaison = inclinaison

    def draw(self):
        t = turtle.Turtle()
        t.speed(0)

        t.color("red")
        t.fillcolor("black")
        t.right(30)
        t.begin_fill()
        for _ in range(4):
            t.forward(self.longueur)
            t.right(90)
        t.end_fill()

        turtle.done()

while True:
    choix = input("Choisissez 1 pour dessiner un rectangle ou 2 pour dessiner un carré : ")
    if choix == '1':
        longueur = int(input("Entrez la longueur du rectangle : "))
        largeur = int(input("Entrez la largeur du rectangle : "))
        rectangle = Rectangle(longueur, largeur)
        rectangle.draw()
        break
    elif choix == '2':
        cote = int(input("Entrez la longueur du côté du carré : "))
        carré = Square(cote)
        carré.draw()
        break
    else:
        print("Veuillez entrer soit 1 pour dessiner un rectangle, soit 2 pour dessiner un carré.")

