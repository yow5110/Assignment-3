# Week 3 Assignment 2
# Write a finite difference calculation of the Lennard-Jones force, plot it, and compare it with a plot from your previous analytical calculation.
#
#
# Variables: 
#   epsilon, sigma: parameters of the Lennard-Jones potential, in a.u.
#   dx: finite-difference parameter

import numpy as np
epsilon=4.e-4 # in a.u.
sigma=6 # in a.u.
rmin = 5.5
rmax = 10
dr = 0.1
r_range = np.arange(rmin,rmax,dr)


def flj_analytical(r):
  #return the analytical result
  
def flj_numerical(r,dx)
  #return the result by numerical diffrentition

flj_analytical_list = #finish constructing this list
flj_numerical_list =  #finish constructing this list

#plot two curves
import matplotlib.pyplot as plot
plt.figure(figsize=(7,4))
