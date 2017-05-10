# lambdas

# import functools # para filter

double = lambda x: x * 2
factorial = lambda n: 1 if n <= 1 \
                        else n * factorial(n - 1)
fibo = lambda n: [] if n < 1 \
                        else [0] if n == 1 \
                        else [0, 1] if n == 2 \
                        else fibo(n-1) + [fibo(n-1)[-1] + fibo(n - 1)[-2]]

reverse = lambda l: [] if not l \
                        else [l[-1]] + reverse(l[:-1])

car = lambda l: None if not l \
                        else l[0]
cdr = lambda l: None if not l \
                        else l[1:]

map = lambda f, l: [] if not l \
                        else [f(car(l))] + map(f, cdr(l))

filter = lambda f, l: [] if not l \
                            else [car(l)] + filter(f, cdr(l)) if f(car(l)) \
                            else filter(f, cdr(l))

reduce = lambda f, l: None if not l \
                            else car(l) if not cdr(l) \
                            else f(car(l), reduce(f, cdr(l)))

print("double(4) = ", double(4))
print("factorial(5) = ", factorial(5))
print("fibo(8) = ", fibo(8))
print("reverse([1, 2, 3, 4]) = ", reverse([1, 2, 3, 4]))
print("map(double, [1, 2, 3]) = ", map(lambda x: x * 2, [1, 2, 3]))
print("filter(espar, range(7)) = ", filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print("reduce(suma, range(6)) = ", reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

