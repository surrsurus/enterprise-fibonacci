import operator

def plus(typeA, typeB):
    return operator.__add__(typeA.number.getNum(), typeB.number.getNum())
