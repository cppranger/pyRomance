from os import path

file = path.join(path.dirname(__file__), 'text', 'choises.txt')


def nextLine():
    with open(file, 'r') as txt:
        lines = txt.read()
    txt.close()
    return lines


