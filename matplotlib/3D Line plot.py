#3d line plot 

import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
t = np.linspace(0, 20, 100)
x = np.sin(t)
y = np.cos(t)
z = t

# Create the 3D line plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)

# Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

#show output
plt.show()
