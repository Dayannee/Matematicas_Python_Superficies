from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)

phi,beta = np.mgrid[0 : np.pi:100j, 0 : 2 * np.pi:100j]

r= np.sin(phi) ** 3 * np.cos(3 * beta)

x= r * np.sin(phi) * np.cos(beta)
y= r * np.sin(phi) * np.sin(beta)
z= r * np.cos(phi)


surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.jet,
        linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.8, aspect=8)

plt.show()


