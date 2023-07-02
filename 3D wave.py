import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig=plt.figure()
ax=plt.axes(projection='3d')

x=np.linspace(0,1,100)
y=x*np.sin(25*x)
z=x*np.cos(25*x)
ax.plot3D(x,y,z)
plt.show()
