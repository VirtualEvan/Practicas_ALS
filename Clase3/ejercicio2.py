# Listado empresas
def file_format(string):
    lines = string.split("\n")
    first = lines[0].split(', ')
    dictionary = {}

    for w in range(1, len(first), 2):
        dictionary[first[w]] = first[w-1]

    for l in range(1, len(lines)):
        key = lines[l].split(', ')[0]
        print(lines[l].replace(key, dictionary[key], 1))


file_format("Microsoft, 1, Apple, 2, Google, 3, Yahoo, 4\n"
            "1, 2015-01-09, 120, 34, 256, 78, 93, 222, 5\n"
            "2, 2015-01-09, 900, 346, 730, 456, 33, 345, 234\n"
            "3, 2015-01-09, 934, 922, 866, 444, 235, 999, 789\n"
            "4, 2015-01-09, 45, 56, 78, 23, 44, 90, 9")


