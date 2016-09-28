from .const.val.numeric.type.toInt import toInt
from .const.const import Const
from .const.val.numeric.arithmetic.plus import plus
from .const.val.numeric.compare.equalTo import equalTo
from .const.val.numeric.compare.equalToSym import equalToSym

class LogTracker(object):
    def __init__(self, n):
        super(LogTracker, self).__init__()
        self.c = Const()
        self.n = toInt(n)
        self.p = self.c.getZero()

    def log(self, c):
        if not equalToSym(c, ','):
            print(c, end="")

        if equalToSym(c, ' '):
            self.p = toInt(plus(self.p, self.c.getOne()))
            print()

        if equalTo(self.p, self.n):
            return True

        return False
