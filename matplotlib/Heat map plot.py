#heat map plot

import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(5, 5)

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()
