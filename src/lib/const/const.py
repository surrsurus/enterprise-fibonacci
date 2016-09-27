from .val.constone import *
from .val.consttwo import *
from .val.constthree import *
from .val.constfour import *
from .val.constfive import *
from .val.constsix import *
from .val.constseven import *
from .val.consteight import *
from .val.constnine import *
from .val.constzero import *

class Const(object):
    def __init__(self):
        super(Const, self).__init__()

    def getOne(self):
        return CONST_ONE

    def getTwo(self):
        return CONST_TWO

    def getThree(self):
        return CONST_THREE

    def getFour(self):
        return CONST_FOUR

    def getFive(self):
        return CONST_FIVE

    def getSix(self):
        return CONST_SIX

    def getSeven(self):
        return CONST_SEVEN

    def getEight(self):
        return CONST_EIGHT

    def getNine(self):
        return CONST_NINE

    def getSeven(self):
        return CONST_ZERO
