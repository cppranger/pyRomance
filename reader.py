import config


def readText():
    with open(config.file, 'r') as txt:
        lines = txt.read()
    txt.close()
    return lines


def readFinal():
    with open(config.final, 'r') as txt:
        lines = txt.readline()
    txt.close()
    return lines

