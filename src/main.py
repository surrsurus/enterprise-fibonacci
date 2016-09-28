from .lib.fib.solver.const.const import Const
from .lib.fib.generator import Generator

def main():
    c = Const()
    g = Generator(int(input('Fibonacci: ')))
    # print('---')
    g.solve()
