#BANKOLE Nathanaël, Master 1 IA
import turtle

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def tracer_figure(self):
        t = turtle.Turtle()
        t.speed(0)

        t.color("green")
        t.forward(self.longueur)
        t.right(90)
        t.color("yellow")
        t.forward(self.largeur)
        t.right(90)
        t.color("red")
        t.forward(self.longueur)
        t.right(90)
        t.color("blue")
        t.forward(self.largeur)
        t.right(90)

        turtle.done()

#La longueur et la largeur du rectangle
longueur = float(input("Entrez la longueur du rectangle : "))
largeur = float(input("Entrez la largeur du rectangle : "))
        
rectangle = Rectangle(longueur, largeur)
rectangle.tracer_figure()