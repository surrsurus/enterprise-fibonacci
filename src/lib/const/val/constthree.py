from .numeric.type.num.number import Number
from .numeric.type.int.integer import Integer

CONST_THREE = Integer(Number(int.from_bytes(b'\x00\x03', byteorder='big')))
