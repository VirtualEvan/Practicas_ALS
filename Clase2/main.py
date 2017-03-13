l = [1, 2, 3]

# Imprime una lista
print(l)

# Imprime un array completo
for x in l:
    print(x, end=' ')

print()

for i, x in enumerate(l):
    print(str.format("{0}: {1}", i, x), end=', ')

#Número de elementos
print("\nNúmero de elementos: ", len(l))

#Slices
#Del segundo en adelante
print("\nDel segundo en adelante: ", l[1:])

#Por rangos
print("\nDel segundo en adelante: ", l[0:2])

#Hasta el segundo
print("\nDel segundo en adelante: ", l[:2])

# Último elemento
print("\nÚltimo elemento: ", l[-1])

# "Comprension" de listas
# nueva_lista = [ <expr> for <id> in <expr que devuelve una lista> ]
print("\n", list([float(x) for x in l]))

# <cond>? <val1>:<val2>
# | En Python
# V
# <val1> if <cond> else <val2>

print([x for x in l if x % 2 == 0])


# Fibonacci que chachi
def fibonacci(x):
    toret = [0, 1]
    if x == 1:
        print([0, 1])
    for _ in range(x-2):
        toret.append(toret[-2] + toret[-1])
    print("Fibonnaci", toret)

fibonacci(4)


# Primos
def primos(x):
    """
    Returns a list with the first x prime numbers.
    :param x: A given natural numbers
    :return: True if prime, False otherwise
    """
    def esprimo(n):
        """
        Determines whether a natural number is a prime number
        :param n: Agiven natural number
        :return: True if prime, False otherwise
        """
        toret = False
        if x == 2:
            toret = True
        elif x % 2 == 0:
            toret = False
        else:
            for i in range(3, x, 2):
                if x % i == 0:
                    break
                else:
                    toret = True
                    # Se ejecuta cuando no se rompe el bucle

        return toret

    toret = []
    for i in range(0, x):
        if esprimo(i):
            toret.append(i)

    return toret

print("Primos: ", primos(10))
