# Préstamo

class Prestamo:
    def __init__(self, num_cuotas, importe, interes):
        self.num_cuotas = num_cuotas
        self.importe = importe + importe * interes
        self.interes = interes
        self.cuota = self.importe/num_cuotas

    @property
    def num_cuotas(self):
        return self._num_cuotas

    @num_cuotas.setter
    def num_cuotas(self, v):
        self._num_cuotas = v

    @property
    def importe(self):
        return self._importe

    @importe.setter
    def importe(self, v):
        self._importe = v

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, v):
        self._interes = v


    def cuota(self):
        return self.cuota

    @property
    def cuota(self):
        return self._cuota

    @cuota.setter
    def cuota(self, v):
        self._cuota = v

    def get_num_cuotas(self):
        return self.num_cuotas

    def paga_cuota(self,):
        self.importe -= self.cuota

    def amortiza(self, x):
        self.importe -= x
        self.cuota = self.importe / self.num_cuotas

    def __str__(self):
        return str.format("Prestamo: Num_cuotas: {0}, Importe: {1}, Interes: {2}, Cuota: {3}", self.num_cuotas, self.importe, self.interes, self.cuota)

p1 = Prestamo(12, 15000, 0.03)
print(p1)

p1.paga_cuota()
print(p1)

p1.amortiza(5000)
print(p1)
