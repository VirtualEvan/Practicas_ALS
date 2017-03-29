# Ejercicio 5
import math

class Punto:
    _origen = None
    @staticmethod
    def get_origen():
        return Punto()

    def __init__(self, x=0, y=0):
        self.x = x  # Atributo privado (Convención)
        self.y = y  # Atributo privado (Convención)

    @staticmethod
    def get_origen():
        if not Punto._origen:
            Punto._origen = Punto()
        return Punto._origen

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, v):
        self._y = v

    def __str__(self):
        return "Soy una simple figura" + "Punto:" + self.p


class Figura:
    # Método al que se llama a través de la clase y no a través de una instancia de esta
    @staticmethod
    def get_origen():
        return Punto()

    def __init__(self, p = (0, 0)):
        self.p = p

    @staticmethod
    def get_origen():
        if not Punto._origen:
            Punto._origen = Punto()
        return Punto._origen

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, v):
        self._p = v

    def __str__(self):
        return "Soy una simple figura" + "Punto:" + self.p

    # Punto más alejado desde la posición inicial
    def punto_alejado(self):

        return math.sqrt(self._x ** 2 + self._x ** 2)


class Circulo(Figura):
    def __init__(self, p, r):
        super().__init__(p)
        self.radio = r

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, v):
        self._radio = v

    def __str__(self):
        return "Soy un circulo" + "Punto:" + self.p + "Radio: " + str(self.radio)

    def __repr__(self):
        return str.format("Circulo({0})", self.radio)


class Rectangulo(Figura):
    def __init__(self, p, l1, l2):
        super().__init__(p)
        self._lado1 = l1
        self._lado2 = l2

    @property
    def lado1(self):
        return self._lado1

    @lado1.setter
    def lado1(self, v):
        self._lado1 = v

    @property
    def lado2(self):
        return self._lado2

    @lado2.setter
    def lado2(self, v):
        self._lado2 = v

    def __str__(self):
        return "Soy un rectangulo" + "Punto:" + self.p + "Lado1: " + str(self.lado1) + "Lado2: " + str(self.lado2)

    def __repr__(self):
        return str.format("Rectangulo({0},{1}): {2}", self.lado1, self.lado2, self.p)

class Dibujo():
    l = []

    def __init__(self, l1=[]):
        self.l = l1

    def __str__(self):
        return "Soy un dibujo" + str(self.l)

    def add(self, f):
        for fig in f:
            self.l.append(fig)

d = Dibujo()
d.add([Circulo(Punto(10, 10), 1), Rectangulo((20, 20), 10, 5)])
print(d)
# [Circulo(10): (10, 10)–(20, 20) | Rectangulo(10, 5): (20, 20)-(30, 25)]