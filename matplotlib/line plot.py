#3d line plot

from matplotlib import pyplot as plt

#co-ordinates
x = [2,3,4,5] #x cordinates
y = [8,3,9,1] #y cordinates

#title and axis labels (optional)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Line Plot")

#plot line
plt.plot(x,y)
plt.show()