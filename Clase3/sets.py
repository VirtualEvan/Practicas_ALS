# Conjuntos

s0 = set()
print(s0)

s1 = {1, 2, 3, 3}  # s1 = set([1, 2, 3, 3])
print(s1)

s2 = set([3, 4, 5])  # s2 = {3, 4, 5}
print(s1 | s2)  # Union
print(s1 - s2)  # Diferencia
print(s1 & s2)  # Interseccion

elto = int(input("Elemento: "))
print(elto in (s1 | s2))
