import operator

def greaterThanOrEqual(typeA, typeB):
    if operator.__ge__(typeA.number.getNum(), typeB.number.getNum()):
        return True
    else:
        return False
