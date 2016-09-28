from .int.integer import Integer
from .flt.float import Float
from .num.number import Number

def toInt(rawInt):
    return Integer(Number(rawInt))
