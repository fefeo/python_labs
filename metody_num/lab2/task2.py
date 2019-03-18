from numpy import *
from cs50 import get_int

s = get_int('set range from: ')
e = get_int('set range to: ')
if s >= 0 and e >= 0:
    for x in range(s , e):
        for y in range(s , e):
            if x%y ==0:
                if x % 2 == 0 and y % 2 == 0:
                    print("x: ",x,"y: ",y)
elif s == 0 or e == 0:
    for x in range(s+1,e+1):
        for y in range(s+1,e+1):
            if x%y ==0:
                if x % 2 == 0 and y % 2 == 0:
                    print("x: ",x,"y: ",y)
else:
    print("wrong range")

