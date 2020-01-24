from Matrix import *
from RREF import rref

a = Matrix(input())
a.print_matrix()
print()
rref(a)
print()
a.print_matrix()