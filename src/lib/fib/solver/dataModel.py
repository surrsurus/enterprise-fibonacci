from .const.const import Const
from .const.val.numeric.arithmetic.multiply import multiply
from .const.val.numeric.type.toInt import toInt

class DataModel(object):
    def __init__(self):
        super(DataModel, self).__init__()
        self.c = Const()
        self.dataModel = [0 for _ in range(int.from_bytes(b'\xa0\x05', byteorder='big'))]

    def inc(self, integer, pos):
        self.dataModel[pos.getInt()] += integer.getInt()

    def dinc(self, integer, pos):
        self.dataModel[pos.getInt()] -= integer.getInt()

    def get(self, pos):
        # print(self.dataModel[pos])
        return self.dataModel[pos.getInt()]
