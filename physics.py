class KE():
    def __init__(self, m, v):
        self.m = m
        self.v = v

    def solve(self):
        return 0.5 * self.m * (self.v ** 2)

    def show_formula(self):
        pass

# ke = KE(1, 1)
# print(ke.solve())

from sympy.interactive import printing
printing.init_printing(use_latex=True)

import numpy as np
import sympy as sp

m = sp.Symbol('m')
v = sp.Symbol('v')

# func = sp.Eq('func')
func = sp.Eq(sp.sin(m), v)
print(func)