from matplotlib.pyplot import *
from numpy import *
from cs50 import get_int , get_float

print('FOR X')
print('If the radius is float, press "f" ')
print('If the radius is int, press "i" ')
print('_'*20)
z=str(input('"f" or "i"?   '))


if z== 'f':
    X=get_float("put float radius X: ")
    F=pi*(X)**2
    P=2*pi*X
    print("field: ",F,"parimeter: ",P)
elif z == 'i':
    X = get_int("put int radius X: ")
    F = pi * (X) ** 2
    P = 2 * pi * X
    print("field: ", F, "parimeter: ", P)

print('FOR Y')
print('If the radius is float, press "f" ')
print('If the radius is int, press "i" ')
print('_'*20)
z=str(input('"f" or "i"?   '))


if z== 'f':
    Y=get_float("put float radius Y: ")
    F=pi*(Y)**2
    P=2*pi*Y
    print("field: ",F,"parimeter: ",P)
elif z == 'i':
    Y = get_int("put int radius Y: ")
    F = pi * (Y) ** 2
    P = 2 * pi * Y
    print("field: ", F, "parimeter: ", P)
