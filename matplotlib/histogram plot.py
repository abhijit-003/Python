#plot histogram
from matplotlib import pyplot as plt

#co-ordinates
x = [1,3,5,7,9]

#title and axis labels (optional)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("histogram Plot")

#plot
plt.hist(x)
plt.show()