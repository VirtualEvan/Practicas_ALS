# Leer archivo detexto


# rU ignora el tipo de fin linea
f = open("files.py", "rU")

for line in f:
    print(line)

f.close()
