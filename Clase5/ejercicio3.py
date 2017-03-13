# Inventario fontanería

class Pieza:
    def __init__(self, precio):
        self.precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, v):
        self._precio = v

    def __str__(self):
        return "Soy una pieza"


class Tuberia(Pieza):
    def __init__(self, precio):
        super().__init__(precio)

    def __str__(self):
        return "Soy una tubería"


class Tuerca(Pieza):
    def __init__(self, precio):
        super().__init__(precio)

    def __str__(self):
        return "Soy una tuerca"


class Codo(Pieza):
    def __init__(self, precio):
        super().__init__(precio)

    def __str__(self):
        return "Soy una codo"


class Invetario:
    def __init__(self):
        self.lista = []

    @property
    def lista(self):
        return self._lista

    @lista.setter
    def lista(self, v):
        self._lista = v

    def anadir_pieza(self, p):
        self.lista.append(p)

    def eliminar_pieza(self, p):
        self.lista.remove(p)

    def modificar_pieza(self, p, precio):
        self.lista[self.lista.index(p)].precio = precio

    def listar(self):
        for p in self.lista:
            print(str.format("Pieza tipo: {0} - {1}$", p.__class__.__name__, p.precio))

inv = Invetario()

p1 = Pieza(200)

t1 = Tuberia(100)
t2 = Tuberia(200)

t3 = Tuerca(300)
t4 = Tuerca(400)

c1 = Codo(1000)
c2 = Codo(7000)

inv.anadir_pieza(p1)
inv.anadir_pieza(t1)
inv.anadir_pieza(t2)
inv.anadir_pieza(t3)
inv.anadir_pieza(t4)
inv.anadir_pieza(c1)
inv.anadir_pieza(c2)
inv.listar()
print("--------------------")
inv.eliminar_pieza(c2)
inv.modificar_pieza(c1, 50)
inv.listar()

