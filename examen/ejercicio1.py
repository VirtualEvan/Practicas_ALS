# Ejercicio1

def elementos_comunes(l1,l2):
    toret = []
    for x in l1:
        if x in l2:
            toret.append(x)
            l2.remove(x)

    return toret


l1 = [1, 2, 3, 3, 4, 5]
l2 = [3, 5, 7]

print(elementos_comunes(l1, l2))