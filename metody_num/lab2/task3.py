from cs50 import get_int , get_float

x=get_int('x: ')
y=get_int('y: ')

ifdivisible= 'X is divisible by Y' if y != 0 and x !=0 and x % y == 0  else 'X is not divisible by Y'
print(ifdivisible)

print