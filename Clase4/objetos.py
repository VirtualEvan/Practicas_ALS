# objetos
import math


class Punto:
    # Método al que se llama a través de la clase y no a través de una instancia de esta
    @staticmethod
    def get_origen():
        return Punto()

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancia_origen(self):
        return self.distancia(Punto.get_origen())

    def distancia(self, other):
        a = abs(self.x - other.x)
        b = abs(self.y - other.y)

        return math.sqrt(a ** 2 + b ** 2)

    def __str__(self):
        return "(" + str(self.x)+ ", " + str(self.y) + ")"

p1 = Punto(10, 10)
p2 = Punto(2, 3)

print(p1)

print("Distancia Origen: ", Punto.get_origen())

print("Distancia p1 - p2: ", p1.distancia(p2))
