# Ejercicio3

def es_subconjunto(c1, l1):
    toret = True

    def comporbar_vacio(c1, l1):
        if not c1 or not l1:
            return False

        return True

    def comprobar_subconjunto(c1, l1):
        for c in l1:
            if not c1.issubset(c):
                return False
        return True

    if not comporbar_vacio(c1, l1):
        return False

    toret = comprobar_subconjunto(c1, l1)

    return toret

c2 = {}
c1 = {1, 2, 3, 4, 4, 5}
print(c1)

l2 = None
l1 = [c1, {3, 6, 8, 9}, {}]
print(l1)

print(es_subconjunto(c1, l2))

c3 = {1, 2}
c4 = {1, 2, 3, 4}
c5 = {5, 6, 7, 1, 2}
c6 = {1, 2}
l3 = [c4, c5, c6]

print(es_subconjunto(c3, l3))



