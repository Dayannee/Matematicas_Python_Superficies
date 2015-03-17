from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

d = 1

i = np.linspace(0, (10*np.pi), 100)
j = np.linspace(0, (40*np.pi), 200)

phi = 0.05 * i
betha = 0.05 * j

#senos y cosenos
sinphi = np.sin(phi)
sinbetha = np.sin(betha)
cosphi = np.cos(phi)
cosbetha = np.cos(betha)

#Calculos para matriz dij
uno = np.power(sinphi,3)
dos = np.cos(3*betha)

res = np.outer(uno,dos)
dij = res * d

#sin (phi i) * cos (betha j) ===> M sini  cosj
msincos = np.outer(sinphi, cosbetha)
xij = dij * msincos

#sin (phi i) * sin (betha j) ===> M sini  sinj
msinsin = np.outer(sinphi, sinbetha)
yij = dij * msinsin

z = ((dij.transpose()) * cosphi)
zij = z.transpose()


ax.plot_surface(xij, yij, zij,  rstride=2, cstride=2, cmap=cm.jet)

plt.show()