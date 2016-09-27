class Number(object):
    def __init__(self, const):
        super(Number, self).__init__()
        self.const = const

    def getNum(self):
        return self.const
