### README for PHYS 643 Problem Set 5 ###

Name: Tim Hallatt

Python 3.7.0

files:

advection.py: this file computes advection with the FTCS and Lax-Friedrichs schemes as per Q1.
diffusion.py: this file computes advection and diffusion in the Lax-Friedrichs and implicit schemes as per Q2.
hydro.py: this file computes the hydrodynamic evolution of a Gaussian density perturbation, subject to a user-defined amplitude ''amp''. (the user must define it in the code - ie. its hard-coded).

For Q3, for the file 'hydro.py':
At low amplitude (e.g. the 'amp' variable = 1.e-5), the Gaussian perturbation very smoothly collapses and splits into two waves which advect to the outer boundaries, where they reflect and constructively grow back into a large perturbation near the center. At large amplitudes (e.g. amp = 1e1), the Gaussian collapses and a shock front develops. Instead of two smooth waves travelling towards the boundaries, we have two fronts with widths only a cell or so wide, separating pre- and post- shock cells by a jump condition. The width of shocks in reality are set by viscosity such that \delta x \sim \lamba_{\rm MFP} / M_{\rm Mach}. In this case, although the code does not explicity include viscosity, there will be 'numerical' viscosity which contributes to momentum transfer between cells. The width of the cells will also contribute - smaller cells will be able to follow the momentum transfer and shock behaviour much better than our very coarse grid (of only 50 cells!).
