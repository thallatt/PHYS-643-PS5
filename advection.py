#!/usr/bin/env python3

# method to compute advection via Lax-Friedrichs and FTCS schemes

import numpy as np
import matplotlib.pyplot as plt

# set up grid, time step
# time step satisfies Courant condition, ie. dt<dx/v
Ngrid= 50
Nsteps = 5000
dt = 1
dx = 1

# initial velocity
v = -0.1
alpha = v * dt * 0.5 / dx

x = np.arange(Ngrid) * dx

# initial f(x) grids
# f(x)=x at t=0
f1 = np.copy(x) * 1. # FTCS
f2 = np.copy(x) * 1. # LF

plt.ion()
# label axes
fig,axes = plt.subplots(1,2)
axes[0].set_title('FTCS')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[1].set_title('Lax-Friedrichs')
axes[1].set_xlabel('x')
axes[1].set_ylabel('f(x)')

# plot initial condition for f(x)
axes[0].plot(x, f1, 'k-')
axes[1].plot(x, f2, 'k-')

plt1, = axes[0].plot(x, f1, 'ro')
plt2, = axes[1].plot(x, f2, 'ro')

fig.canvas.draw()

count=0

# loop through time
while count < Nsteps:
	
	# FTCS
	# only update grid cells inside boundaries -- fixed boundary condition
	f1[1:Ngrid-1] = f1[1:Ngrid-1] - alpha * (f1[2:] - f1[:Ngrid-2])
	
	# Lax-Friedrichs
	# only update grid cells inside boundaries -- fixed boundary condition
	f2[1:Ngrid-1] = 0.5 * (f2[2:] + f2[:Ngrid-2]) - alpha * (f2[2:] - f2[:Ngrid-2])
	
	# update the plot
	# animation code as suggested in problem set by Prof. Eve J Lee, McGill, Astrophysical Fluids PHYS 643 2020
	plt1.set_ydata(f1)
	plt2.set_ydata(f2)
	
	fig.canvas.draw()
	plt.pause(0.001)
	count += 1

