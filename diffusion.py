#!/usr/bin/env python3

# method to compute advection via Lax-Friedrichs scheme as well as diffusion though an implicit solver

import numpy as np
import matplotlib.pyplot as plt

# set up grid, as used in problem 1
Ngrid= 50
Nsteps = 5000
dt = 1
dx = 1

# initial velocity
v = -0.1
alpha = v * dt * 0.5 / dx

x = np.arange(Ngrid) * dx

f1 = np.copy(x) * 1.
f2 = np.copy(x) * 1.

# store initial values for boundaries
f1_0, f1_end = f1[0], f1[-1]
f2_0, f2_end = f2[0], f2[-1]

plt.ion()
# set plot titles and labels
fig,axes = plt.subplots(1,2)
axes[0].set_title('D=2')
axes[1].set_title('D=0.1')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[1].set_xlabel('x')
axes[1].set_ylabel('f(x)')

axes[0].plot(x, f1, 'k-')
axes[1].plot(x, f2, 'k-')

plt1, = axes[0].plot(x, f1, 'ro')
plt2, = axes[1].plot(x, f2, 'ro')

fig.canvas.draw()

count=0

# diffusive constants
D1, D2 = 2., 0.1
beta1, beta2 = D1 * dt / dx**2., D2 * dt / dx**2.

while count < Nsteps:
	
	# matrix to apply diffusion step
	A1 = np.eye(Ngrid) * (1. + 2. * beta1) + np.eye(Ngrid, k=1) * -beta1 + np.eye(Ngrid, k=-1) * -beta1
	# apply zero velocity gradient boundary condition
	A1[-1][-1] = 1 + beta1
	# solve matrix equation
	f1 = np.linalg.solve(A1, f1)
	A2 = np.eye(Ngrid) * (1. + 2. * beta2) + np.eye(Ngrid, k=1) * -beta2 + np.eye(Ngrid, k=-1) * -beta2
	A2[-1][-1] = 1 + beta2
	f2 = np.linalg.solve(A2, f2)

	# advection step via Lax-Friedrichs
	f1[1:Ngrid-1] = 0.5 * (f1[2:] + f1[:Ngrid-2]) - alpha * (f1[2:] - f1[:Ngrid-2])
	f2[1:Ngrid-1] = 0.5 * (f2[2:] + f2[:Ngrid-2]) - alpha * (f2[2:] - f2[:Ngrid-2])
	
	# boundary conditions
	f1[0], f1[-1] = f1_0, f1_end
	f2[0], f2[-1] = f2_0, f2_end
	
	# update the plot, same as problem 1
	plt1.set_ydata(f1)
	plt2.set_ydata(f2)
	
	fig.canvas.draw()
	plt.pause(0.001)
	count += 1

