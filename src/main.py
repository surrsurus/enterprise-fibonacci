from .lib.fib.solver.const.const import Const
from .lib.fib.generator import Generator

def main():
    c = Const()
    g = Generator(5)
    # print('---')
    g.solve()
