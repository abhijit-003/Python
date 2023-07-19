#pie chart
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 45, 10, 5]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
