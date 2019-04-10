from numpy import *
from task1 import countField
from cs50 import get_float


def compare(figure1, figure2):
    values = []
    for i in (figure1, figure2):
        if i == 'circle':
            print(i,':')
            x = get_float('put radius: ')
            print('\n')
            fig = countField(i, x)
            values.append(fig)
        else:
            print(i+':')
            x = get_float('put parameter x: ')
            y = get_float('put parameter y: ')
            print('\n')
            fig = countField(i, x, y)
            values.append(fig)

    if values[0] > values[1]:
        print(figure1+ ' has bigger field than '+ figure2, ' by ', values[0] - values[1] )
    elif values[0] == values[1]:
        print(figure1+ ' has equal field to '+ figure2)
    else:
        print(figure2+ ' has bigger field than '+ figure1, ' by ', values[1]-values[0])


compare('circle','circle')