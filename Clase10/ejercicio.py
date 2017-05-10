# encoding: utf-8
# Ejercicio completo
# http://ideone.com/ejv8zy

from datetime import date
import pickle

# 1. Crea una clase Libro, que guarde título, autor,
# editorial, y fecha de devolución
class Libro:
    _titulo = None
    _autor = None
    _editorial = None
    _fecha_devolucion = None

    def __init__(self, titulo, autor, editorial):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.fecha_devolucion = date.min

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, v):
        self._titulo = v

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, v):
        self._autor = v

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, v):
        self._editorial = v

    @property
    def fecha_devolucion(self):
        return self._fecha_devolucion

    @fecha_devolucion.setter
    def fecha_devolucion(self, v):
        self._fecha_devolucion = v

    def pon_fecha_devolucion(self, nuevaFecha):
        self.fecha_devolucion = nuevaFecha

    def __str__(self):
        return "{0}, {1}, {2}".format(self.titulo, self.autor, self.editorial)


# 2. Crea la funcionalidad estaprestado(), que devuelve True si el libro
# ya ha sido devuelto, y False en otro caso. No crear nungún método

    def __getattr__(self, item):
        if item =="esta_prestado":
            return lambda: (self.fecha_devolucion > date.today())


# 3. Crea también la clase biblioteca, que guarda libros.
# Tendrá un método inserta(l) que permitirá añadir el libro l
# Necesitamos un constructor __init__() y tambien __str__()

# 4. Utilizando
class Biblioteca:
    biblio = None

    def __init__(self, lista=[]):
        self.biblio = lista

    def inserta(self, l):
        self.biblio.append(l)

    def guarda(self, nf):
        with open(nf, "wb") as f:
            for l in self.biblio:
                pickle.dump(l)

    @staticmethod
    def carga(self, nf):
        toret = Biblioteca()

        try:
            with open(nf, "rb") as f:
                while(True):
                    toret.inserta(pickle.load(f))
        finally:
            return

    def __len__(self):
        return len(self.biblio)

    def __str__(self):
        return str.join("\n", [str(l) for l in self.biblio])


if __name__ == "__main__":
    b0 = Biblioteca()

    if len(b0) == 0:
        l1 = Libro("El conde de montecristo", "Alejandro Dumas", "Timun-Mas")
        l1.pon_fecha_devolucion(date(2017, 5, 9))

        l2 = Libro("Viaje al centro de la tierra", "Julio Verne", "Timun-Mas")
        l2.pon_fecha_devolucion(date(2017, 5, 1))

        b0.inserta(l1)
        b0.inserta(l2)

    # b0.guarda("biblio.dat")

    l3 = Libro("Libro de prueba", "Yo", "Mi casa")
    l3.pon_fecha_devolucion(date(2017, 2, 1))

    print(l1)
    print(l2)

    print("Prestado 'el conde...': ", l1.esta_prestado())
    print("Prestado 'viaje al...': ", l2.esta_prestado())

    b1 = Biblioteca([l1, l2])
    b1.inserta(l3)

    print(b1)
