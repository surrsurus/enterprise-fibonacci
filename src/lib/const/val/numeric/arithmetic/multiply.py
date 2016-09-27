import operator

def multiply(typeA, typeB):
    if operator.__mul__(typeA.number.getNum(), typeB.number.getNum()):
        return True
    else:
        return False
