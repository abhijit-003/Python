import matplotlib.pyplot as plt

'''
#simple line graph
x=[1,2,3]
y=[6,7,3]
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Graph")
plt.show()
'''
#multi lines on same graph
x1=[1,2,3,4,5,6]
y1=[2,4,3,6,4,7]

#color is colour of line
#style means dashed,dotted,solid

plt.plot(x1,y1, color='blue',linestyle='dashed',linewidth='8',marker='o',markersize='16',markerfacecolor='orange',label= "line 1")

x2=[0.1,1.1,2.1,3.1,4.1,5.1]
y2=[1,3,2,5,3,6]
plt.plot(x2,y2, label="line 2")

x3=[1,2,3,4,5,6]
y3=[1,1,1,1,1,1]
plt.plot(x3,y3,label="label 3",linewidth="10",linestyle='dotted')

#define axis lim
plt.xlim(0,8)
plt.ylim(0,8)
# #plt.legend this gives the info about line in small rectangle box like
#---- line 1, ---- line 2
plt.legend()
plt.show()
