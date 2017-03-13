def analyze(file):
    """
    Read a file and show the frequency of each word
    :param file: The file that must be read
    :return: Frequency of each word in the file
    """
    if not type(file) is str:
        print("Parameter must be string")
        exit(0)

    f = open(file, "rU")

    if not f:
        print("File not found")
        exit(1)

    dict = {}

    for line in f:
        unicode_line = line.translate({ord(c): ' ' for c in '\(\):,{}."[]='}).lower()
        for word in unicode_line.split():
            if word not in dict.keys():
                dict[word] = 1
            else:
                dict[word] += 1

    for p in dict.keys():
        print(str.format("{0}: {1}", p, dict[p]))

analyze("diccionario.py")

