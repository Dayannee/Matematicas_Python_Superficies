# Intento de plotear 3D la piezo del cuarzo
# Author: Luis (Senior)

import numpy as np
from mayavi import mlab

# Create data with phi (colatitude) and beta (longitude) scanning a sphere

phi,beta = np.mgrid[0:np.pi:100j,0:2*np.pi:200j]

r= np.sin(phi)**3*np.cos(3*beta)


x= r*np.sin(phi)*np.cos(beta)
y= r*np.sin(phi)*np.sin(beta)
z= r*np.cos(phi)


mlab.figure(1, fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))

# Visualize the points
pts = mlab.points3d(x, y, z, z, scale_mode='none', scale_factor=0.03)
#Create and visualize the mesh
#mesh = mlab.pipeline.delaunay2d(pts)
#surf = mlab.pipeline.surface(pts)

mlab.view(47, 57, 8.2, (0.1, 0.15, 0.14))
mlab.show()
