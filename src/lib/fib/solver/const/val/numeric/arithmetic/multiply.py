import operator

def multiply(typeA, typeB):
    return operator.__mul__(typeA.number.getNum(), typeB.number.getNum())
