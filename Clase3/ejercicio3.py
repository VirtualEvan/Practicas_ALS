# Almacen

warehouse = {"Manolo": "manu@gmail.com", "Marta": "marita@gmail.com", "Pepa": "pepucha@gmail.com"}


def menu():
    op = int(input("Option: "))
    {1: list, 2: add}[op]()
    menu()


def list():
    for i in warehouse:
        print(str.format("{0}: {1}", i, warehouse[i]))


def add():
    name = str(input("Name: "))
    mail = str(input("eMail: "))
    warehouse[name] = mail


menu()
