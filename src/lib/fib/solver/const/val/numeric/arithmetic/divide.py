import operator

def divide(typeA, typeB):
    return operator.__div__(typeA.number.getNum(), typeB.number.getNum())
