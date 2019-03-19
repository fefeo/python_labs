from numpy import *
from cs50 import get_int , get_float

x = get_float("put radius x: ")
y = get_float("put radius y: ")

while x <= 0 or y <= 0:
    x = get_float("put radius x: ")
    y = get_float("put radius y: ")
for i in [x,y]:
    F = pi * (i**2)
    P = 2 * pi * i
    print('for radius', i ,'Field = ', F ,'\n', 'Parimeter = ', P)

