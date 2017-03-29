# Ejercicio2

def historigrama(l):
    m = max(l)
    for e in l:
        print("*" * int(10*e/m))


l1 = [100, 50, 80]
l2 = [10, 5, 8]
l3 = [20, 10, 16]
l4 = [2, 12, 5]

historigrama(l1)
print("------------")
historigrama(l2)
print("------------")
historigrama(l3)
print("------------")
historigrama(l4)