from Matrix import *
from RREF import rref

a = Matrix(input())
a.print_matrix()
print()
b = rref(a)
print()
b.print_matrix()