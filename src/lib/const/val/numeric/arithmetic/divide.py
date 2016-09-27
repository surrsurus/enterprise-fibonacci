import operator

def divide(typeA, typeB):
    if operator.__div__(typeA.number.getNum(), typeB.number.getNum()):
        return True
    else:
        return False
