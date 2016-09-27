import operator

def lessThan(typeA, typeB):
    if operator.__lt__(typeA.number.getNum(), typeB.number.getNum()):
        return True
    else:
        return False
