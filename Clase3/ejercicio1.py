# Conversion de fechas
def date_format(date):
    months = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6, "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12}
    l = date.split()

    print(str.format("{0}-{1:0>2}-{2:0>2}", l[2], months[l[1]], l[0]))

date_format("12 feb 2015")
date_format("1 ene 2017")
date_format("6 oct 2003")
