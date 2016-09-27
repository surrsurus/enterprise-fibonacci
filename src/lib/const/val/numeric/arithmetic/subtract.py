import operator

def subtract(typeA, typeB):
    if operator.__sub__(typeA.number.getNum(), typeB.number.getNum()):
        return True
    else:
        return False
