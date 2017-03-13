# herencia (Rectángulos y cuadrados)


class Rectangulo:
    def __init__(self, l1, l2):
        self._lado1 = l1
        self._lado2 = l2

    @property
    def lado1(self):
        return self._lado1

    @lado1.setter
    def lado1(self, v):
        self._lado1 = v

        if self.lado1 != self.lado2 and isinstance(self, Cuadrado):
            self.__class__ = Rectangulo

        if self.lado1 == self.lado2 and isinstance(self, Rectangulo):
            self.__class__ = Cuadrado

    @property
    def lado2(self):
        return self._lado2

    @lado2.setter
    def lado2(self, v):
        self._lado2 = v

        if self.lado1 != self.lado2 and isinstance(self, Cuadrado):
            self.__class__ = Rectangulo

        if self.lado1 == self.lado2 and isinstance(self, Rectangulo):
            self.__class__ = Cuadrado

    def calcula_area(self):
        return self.lado1 * self.lado2

    def __str__(self):
        return "[" + str(self.lado1) + ", " + str(self.lado2) + "]"


class Cuadrado(Rectangulo):
    def __init__(self, l):
        super().__init__(l, l)

    @property
    def lado(self):
        return self._lado1

    @lado.setter
    def lado(self, v):
        self._lado1 = v
        self._lado2 = v

r1 = Rectangulo(5, 6)
c1 = Cuadrado(9)

print(r1)
print(c1)
