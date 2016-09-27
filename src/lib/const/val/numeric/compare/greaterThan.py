import operator

def greaterThan(typeA, typeB):
    if operator.__gt__(typeA.number.getNum(), typeB.number.getNum()):
        return True
    else:
        return False
