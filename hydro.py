#!/usr/bin/env python3

# method to compute hydrodynamic evolution of isothermal gas. follows evolution of a sound wave initially Gaussian in distribution.

import numpy as np
import matplotlib.pyplot as plt

# set up grid
Ngrid= 50 # including ghost cells
Nsteps = 5000
dt = 0.05
dx = 1

# x defined at cell centers
x = np.arange(Ngrid) * dx
# xi defined at cell walls
xi = np.ones(len(x)+1)
xi[1:-2] = 0.5 * (x[0:-2]+x[1:Ngrid-1])
xi[0] = x[0] - 0.5 * dx
xi[Ngrid] = x[Ngrid-1] + 0.5 * dx
xi[Ngrid-1] = x[Ngrid-2] + 0.5 * dx

# initial density distribution is Gaussian, with amplitude ''amp''
amp = 1.e1
f1 = amp*np.exp(-(x-25)**2./3**2.)+1
# initial velocity distribution
u1 = np.ones(len(x)) * 1 / Ngrid
# flux term; rho * u
f2 = f1 * u1
# define arrays at cell edges
u_edges = np.ones(len(xi))
J_edges1 = np.ones(len(xi))
J_edges2 = np.ones(len(xi))

plt.ion()
# set up plotting and labels as previous problems
fig,axes = plt.subplots(1,1)
axes.set_title('')
axes.set_xlabel('x')
axes.set_ylabel('density(x)')

axes.plot(x, f1, 'k-')

plt1, = axes.plot(x, f1, 'ro')

axes.set_xlim([0,Ngrid])

fig.canvas.draw()

count=0

# isothermal sound speed
cs=1.

while count < Nsteps:

	# reflective boundary conditions
	u_edges[0]=-u_edges[1]
	u_edges[-1]=-u_edges[-2]
	f1[0]=f1[1]
	f1[-1]=f1[-2]
	
	# array of velocity at cell edges
	for i in range(1,Ngrid):
		u_edges[i] = 0.5 * (f2[i-1] / f1[i-1] + f2[i] / f1[i])
	
	# compute flux terms at cell edges for advection
	for i in range(1,Ngrid):
		if u_edges[i] > 0:
			J_edges1[i] = f1[i-1] * u_edges[i]
		else:
			J_edges1[i] = f1[i] * u_edges[i]

	# advect density
	for i in range(1,Ngrid-1):
		f1[i] = f1[i] - (dt / dx) * (J_edges1[i+1] - J_edges1[i])

	# similar for flux f2
	# compute flux at cell edges
	for i in range(1,Ngrid):
		if u_edges[i] > 0:
			J_edges2[i] = f2[i-1] * u_edges[i]
		else:
			J_edges2[i] = f2[i] * u_edges[i]

	# advect flux
	for i in range(1,Ngrid-1):
		f2[i] = f2[i] - (dt / dx) * (J_edges2[i+1] - J_edges2[i])
	
	# isothermal pressure
	p = f1 * cs**2.
	
	# evolve flux due to pressure gradient force
	for i in range(1,Ngrid-1):
		f2[i] = f2[i] - (dt / dx) * (p[i+1] - p[i-1])
	
	# update the plot, same as previous problems
	plt1.set_ydata(f1)
	
	fig.canvas.draw()
	plt.pause(0.001)
	count += 1
