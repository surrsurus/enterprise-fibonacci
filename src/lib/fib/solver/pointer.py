from .const.val.numeric.type.num.number import Number
from .const.val.numeric.type.int.integer import Integer
from .const.val.numeric.type.flt.float import Float
from .const.val.numeric.type.toInt import toInt
from .const.val.numeric.arithmetic.plus import plus
from .const.val.numeric.arithmetic.subtract import subtract
from .const.val.numeric.arithmetic.divide import divide
from .const.val.numeric.arithmetic.multiply import multiply
from .const.val.numeric.compare.greaterThan import greaterThan
from .const.val.numeric.compare.lessThan import lessThan
from .const.val.numeric.compare.equalTo import equalTo
from .const.val.numeric.compare.lessThanOrEqual import lessThanOrEqual
from .const.val.numeric.compare.greaterThanOrEqual import greaterThanOrEqual

from .const.const import Const

class Pointer(object):
    def __init__(self, integer):
        super(Pointer, self).__init__()
        self.integer = integer
        self.c = Const()

    def inc(self, value):
        self.integer = toInt(plus(self.integer, value))

    def dinc(self, value):
        self.integer = toInt(subtract(self.integer, value))

    def get(self):
        return self.integer
