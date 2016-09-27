from .numeric.type.num.number import Number
from .numeric.type.int.integer import Integer

CONST_TWO = Integer(Number(int.from_bytes(b'\x00\x02', byteorder='big')))
