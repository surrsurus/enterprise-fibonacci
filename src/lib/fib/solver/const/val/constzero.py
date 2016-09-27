from .numeric.type.num.number import Number
from .numeric.type.int.integer import Integer

CONST_ZERO = Integer(Number(int.from_bytes(b'\x00\x00', byteorder='big')))
