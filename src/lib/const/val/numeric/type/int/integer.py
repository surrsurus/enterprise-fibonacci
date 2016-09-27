class Integer(object):
    def __init__(self, number):
        super(Integer, self).__init__()
        self.number = number

    def getInt(self):
        return self.number.getNum()
