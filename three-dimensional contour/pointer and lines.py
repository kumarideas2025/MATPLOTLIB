import numpy as np
import matplotlib.pyplot as plt
ax=plt.axes(projection='3d')
z=np.linspace(0,15,1000)

x=np.sin(z)
y=np.cos(z)
ax.plot3D(x,y,z,'red')

z=15*np.random.random(100)
x=np.sin(z)+0.1*np.random.random(100)
y=np.cos(z)+0.1*np.random.random(100)
ax.scatter3D(x,y,z,c=z,cmap='Greens')
plt.savefig('3D points and lines BY MATPLOTLIB.png',dpi=300,bbox_inches='tight')
plt.show()