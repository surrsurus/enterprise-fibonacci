class Float(object):
    def __init__(self, number):
        super(Float, self).__init__()
        self.number = number

    def getFloat(self):
        return self.number.getNum()

    def setNum(self, number):
        self.number = number

    def setNumNum(self, number):
        self.number.setNum(number)
