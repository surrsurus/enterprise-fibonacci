import operator

def subtract(typeA, typeB):
    return operator.__sub__(typeA.number.getNum(), typeB.number.getNum())
