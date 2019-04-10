from numpy import *
from cs50 import *


def countField(figure, x, y = 1):

    if x <= 0 or y <= 0:
        print('both parameters must be higher then 0')
        quit()

    if figure == 'circle':
        field = pi * x **2
    elif figure == 'rectangle':
        field = x * y
    elif figure == 'triangle' or figure == 'rhombus':
        field = (x * y)/2
    else:
        print('i do not know this fig')
        quit()

    return field


print(countField('rectangle',3,3))

