import operator

def plus(typeA, typeB):
    if operator.__add__(typeA.number.getNum(), typeB.number.getNum()):
        return True
    else:
        return False
