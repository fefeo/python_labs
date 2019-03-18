from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
#TASKS (4p)
#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
#2 ask the user for a number and print its factorial (1p)
#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)
#Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.

#1
print(' calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100]')


def y(x):
    y=2*(x**2)+2*x+2
    return y
for x in range(56,101):
    print(y(x))


print('-'*20)

#2
print('ask the user for a number and print its factorial')


z=int(input('put int number: '))

if z>0:
    s=1
    for i in range(z):
        s=s*(i+1)
        print(s)
else:
    print('wrong number')

print('-'*20)

#3
print(   'write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value')


#def tln(x):
 #   x=int(input('size of an array: '))
  #  arr=[]

   # for i in range(x):
    #    print('value of index',i,":"),
     #   v=int(input())
      #  if v>0:
       #     arr.append(v)
        #else:
         #  print('wrong number')
    #print(arr)
    #return print('index:',arr.index(min(arr)),"value:",min(arr))
#tln(x)

l=[]
d=int(input('put array size: '))
for z in range(d):
    print('put value of index',z,':')
    v=int(input())
    l.append(v)
print(l)

#l=[4,5,3,1,55]
index=[]
def min(i):

    n=l[0]
    for i in l:
        if i <= n:
            n=i
    print('lowest value: ',n)

    for i in range(len(l)):
        if l[i]==n:
            index.append(i)

    print('index: ', index)


min(l)


print('-'*20)

#4
print('looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length')

s=int(input('start point: '))
e=int(input('end point: '))

if s==e:
    print('points set wrong! ')
    while s==e:
        e=int(input('put correct end point: '))

x=linspace(s,e,10)
y=sin((x**2)+2*x+2)

plot(x,y, color='orange')
plot(x,y, 'o', color='red')
title('wykres')
xlabel('my lenght')
ylabel('oś y')
ylim(-2,2)
show()

