import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return np.sin(np.sqrt(x**2 + y**2))
x=np.linspace(-6,6,30)
y=np.linspace(-6,6,30)
x,y=np.meshgrid(x,y)
z=f(x,y)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.contour3D(x,y,z,50,cmap='binary')
ax.set_xlabel('x') 
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig('3D BY MATPLOTLIB.png',dpi=300,bbox_inches='tight')
plt.show()