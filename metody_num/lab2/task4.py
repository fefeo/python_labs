from numpy import *
from cs50 import get_int , get_float

x=get_float('x: ')
y=get_float('y: ')

ifdivisible= 'X is divisible by Y' if y != 0 and x !=0 and x % y == 0  else 'X is not divisible by Y'
print(ifdivisible)

a = x / y
#print(round_(a, 10))
print("%.6f" % a)


