from .numeric.type.num.number import Number
from .numeric.type.int.integer import Integer

CONST_FIVE = Integer(Number(int.from_bytes(b'\x00\x05', byteorder='big')))
