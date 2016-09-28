
class List(object):
    def __init__(self, symbolList, length):
        super(List, self).__init__()
        self.symbolList = symbolList
        self.length = length

    def getSymAt(self, pos):
        return self.symbolList[pos.getInt()]
