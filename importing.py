import itertools
from pyfunction import *

al = ['a', 'b', 'c']
pms = itertools.combinations(al, 2)
for p in pms:
    print(p)

s = square(5)
print(s)