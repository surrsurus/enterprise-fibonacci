import operator

def lessThanOrEqual(typeA, typeB):
    if operator.__le__(typeA.number.getNum(), typeB.number.getNum()):
        return True
    else:
        return False
