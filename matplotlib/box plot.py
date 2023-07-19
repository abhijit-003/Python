#box plot
import matplotlib.pyplot as plt

data = [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9]

plt.boxplot(data)
plt.ylabel('Values')
plt.title('Box Plot')
plt.show()
