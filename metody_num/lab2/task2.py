from numpy import *
s=int(input('set range from: '))
e=int(input('set range to: '))
for x in range(s,e):
    for y in range(s,e):
        if x%y ==0:
            if x % 2 == 0 and y % 2 == 0:
                print("x: ",x,"y: ",y)

