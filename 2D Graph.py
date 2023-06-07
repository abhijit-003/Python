#python 2D graph
import matplotlib.pyplot as plt
#from matplotlib.pyplot import *
from numpy import *


#1
x1=linspace(-5,5)
x=x1
y=x1
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("2D graphs")
plt.plot(x,y)


#2
x1=linspace(0,2*180)
x=sin(x1)
y=sin(x1)
plt.plot(x,x1)
plt.plot(y,x1)


#3
lin=linspace(-5,5)
a=lin*sin(1/lin**2)
x=a
y=a
plt.plot(x,y)


#4
lin=linspace(0,10)
x=log(lin)
y=log(lin)
plt.title("Graph 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x,y,'r')


#5
lin=linspace(0,5)
a=lin**4
x=a
y=a
plt.plot(x,y,'g',linestyle='dashed',marker='o')
plt.show()
