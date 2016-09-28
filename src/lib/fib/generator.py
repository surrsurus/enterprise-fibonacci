from .solver.header import Header
from .solver.list import List
from .solver.dataModel import DataModel
from .solver.logTracker import LogTracker
from .solver.const.const import Const
from .solver.symbols.decrement import DecrementSym
from .solver.symbols.increment import IncrementSym
from .solver.symbols.left import LeftSym
from .solver.symbols.right import RightSym
from .solver.symbols.loopEnd import LoopEndSym
from .solver.symbols.loopStart import LoopStartSym
from .solver.symbols.log import LogSym
from .solver.const.val.numeric.compare.equalToSym import equalToSym
from .solver.const.val.numeric.type.toInt import toInt
from .solver.const.val.numeric.compare.equalTo import equalTo
from .solver.const.val.numeric.compare.greaterThan import greaterThan
from .solver.const.val.numeric.arithmetic.plus import plus
from .solver.const.val.numeric.arithmetic.subtract import subtract
from .solver.pointer import Pointer

class Generator(object):

    def __init__(self, n):
        super(Generator, self).__init__()
        self.c = Const()
        self.d = DataModel()
        self.l = LogTracker(n)
        self.p = Pointer(self.c.getZero())
        self.h = Header(self.c.getZero())
        self.list = List([
            RightSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            RightSym(),
            IncrementSym(),
            RightSym(),
            IncrementSym(),
            LoopStartSym(),
            LoopStartSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopEndSym(),
            RightSym(),
            LogSym(),
            LeftSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            IncrementSym(),
            LoopStartSym(),
            RightSym(),
            DecrementSym(),
            DecrementSym(),
            DecrementSym(),
            DecrementSym(),
            DecrementSym(),
            DecrementSym(),
            DecrementSym(),
            DecrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopEndSym(),
            IncrementSym(),
            LeftSym(),
            LeftSym(),
            LeftSym(),
            LoopEndSym(),
            RightSym(),
            LogSym(),
            RightSym(),
            RightSym(),
            LoopStartSym(),
            LoopStartSym(),
            DecrementSym(),
            LoopEndSym(),
            LeftSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopEndSym(),
            RightSym(),
            RightSym(),
            LoopStartSym(),
            LeftSym(),
            LeftSym(),
            IncrementSym(),
            RightSym(),
            IncrementSym(),
            RightSym(),
            DecrementSym(),
            LoopEndSym(),
            LeftSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            LoopStartSym(),
            DecrementSym(),
            LoopEndSym(),
            RightSym(),
            IncrementSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            LeftSym(),
            LeftSym(),
            DecrementSym(),
            LoopStartSym(),
            RightSym(),
            IncrementSym(),
            LeftSym(),
            DecrementSym(),
            LoopEndSym(),
            LoopEndSym(),
            LoopEndSym(),
            LoopEndSym(),
            LoopEndSym(),
            LoopEndSym(),
            LoopEndSym(),
            LoopEndSym(),
            LoopEndSym(),
            LoopEndSym(),
            LoopEndSym(),
            IncrementSym(),
            RightSym(),
            RightSym(),
            RightSym(),
            LoopEndSym(),
            LeftSym(),
            LeftSym(),
            LeftSym(),
            LoopEndSym()
        ], 172)

    def solve(self):
        #s = self.h.getSymAt(self.p.get()).getSymbol()
        ptr = 0
        i = 0
        arr = [0] * 30000


        while True:
            s = self.list.getSymAt(self.p.get()).getSymbol()
            # print(s)
            if equalToSym(s, '>'):
                self.h.inc(self.c.getOne())

            elif equalToSym(s, '<'):
                self.h.dinc(self.c.getOne())

            elif equalToSym(s, '+'):
                self.d.inc(self.c.getOne(), self.h.get())

            elif equalToSym(s, '-'):
                self.d.dinc(self.c.getOne(), self.h.get())

            elif equalToSym(s, '.'):
                try:
                    if self.l.log(toInt(int(chr(self.d.get(self.h.get().getInt()))))):
                        break
                except:
                    pass

            elif equalToSym(s, '['):
                if equalTo(toInt(self.d.get(self.h.get().getInt())), self.c.getZero()):
                    l = self.c.getOne()
                    while greaterThan(l, self.c.getZero()):
                        self.p.inc(self.c.getOne())
                        c = self.list.getSymAt(self.p.get()).getSymbol()
                        if equalToSym(c, '['):
                            l = toInt(plus(l, self.c.getOne()))
                        elif equalToSym(c, ']'):
                            l = toInt(subtract(l, self.c.getOne()))

            elif equalToSym(s, ']'):
                l = self.c.getOne()
                while greaterThan(l, self.c.getZero()):
                    self.p.dinc(self.c.getOne())
                    c = self.list.getSymAt(self.p.get()).getSymbol()
                    if equalToSym(c, '['):
                        l = toInt(subtract(l, self.c.getOne()))
                    elif equalToSym(c, ']'):
                        l = toInt(plus(l, self.c.getOne()))

                self.p.dinc(self.c.getOne())
            self.p.inc(self.c.getOne())
