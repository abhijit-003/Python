#matplotlib
#scatter plot

import matplotlib.pyplot as plt
import numpy as np

# Generate random data
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot')

# Show the plot
plt.show()
