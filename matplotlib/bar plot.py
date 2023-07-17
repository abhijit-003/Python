#plot bar
from matplotlib import pyplot as plt

#co-ordinates
x = [1,3,5,7,9]
y = [2,6,8,3,9]

#title and axis labels (optional)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("bar Plot")

#plot
plt.bar(x,y)
plt.show()