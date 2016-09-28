import operator

def equalToSym(symA, symB):
    if operator.__eq__(symA, symB):
        return True
    else:
        return False
