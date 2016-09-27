import operator

def equalTo(typeA, typeB):
    if operator.__eq__(typeA.number.getNum(), typeB.number.getNum()):
        return True
    else:
        return False
