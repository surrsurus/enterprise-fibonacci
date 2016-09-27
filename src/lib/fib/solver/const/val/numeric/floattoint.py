from type.int.integer import Integer
from type.num.number import Number

def floatToInt(float):
    return Integer(Number(float.getFloat()))
