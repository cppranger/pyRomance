import config


def readText():
    with open(config.file, 'r') as txt:
        lines = txt.read()
    txt.close()
    return lines


