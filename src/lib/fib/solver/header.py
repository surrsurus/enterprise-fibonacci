from .const.val.numeric.type.num.number import Number
from .const.val.numeric.type.int.integer import Integer
from .const.val.numeric.type.flt.float import Float
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

class Header(object):
    def __init__(self, integer, list):
        super(Header, self).__init__()
        self.integer = integer
        self.list = list
        self.c = Const()

    def inc(self, value):
        self.integer.setNum(Number(plus(self.integer, self.value)))

        if lessThan(self.integer, self.c.getZero()):
            self.integer = self.c.getZero()

    def dinc(self, value):
        self.integer.setNum(Number(subtract(self.integer, self.value)))

        if greaterThan(self.integer, self.list.getLength()):
            self.integer = self.list.getLength()
