from numpy import *
from cs50 import get_int , get_float

print('circle = c')
print('rectangle = re')
print('triangle = t')
print('rhombus = r')

#o = str(input('podaj fig'))

def countField(figure):
    if figure == 'c':
        while True:
            x = get_float('put radius x: ')
            if x > 0:
                Fie = pi * x ** 2
                break
        return Fie
    elif figure == 're':
        while True:
            x = get_float('put parameter x: ')
            y = get_float('put parameter y: ')
            if x > 0  and y > 0:
                Fie = x * y
                break
        return Fie
    elif figure == 't' or figure == 'r':
        while True:
            x = get_float('put parameter x: ')
            y = get_float('put parameter y: ')
            if x > 0 and y > 0:
                Fie = 1/2 * x * y
                break
        return Fie
    else:
        return('error')




print(countField('s'))

