# import sympy as sym
#
# k = sym.Symbol("x")
# print(k)
# d = sym.sin(k)
# print(d)
# l = sym.diff(d)
# print(l)


import random as r


k = [[r.randint(10, 50) for m in range(4)] for n in range(7)]
for row in range(len(k)):
    print(k[row])