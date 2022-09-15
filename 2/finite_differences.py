# Week 3 Assignment 2
# Write a finite difference calculation of the Lennard-Jones force, plot it, and compare it with a plot from your previous analytical calculation.
#
#
# Variables: 
#   epsilon, sigma: parameters of the Lennard-Jones potential, in a.u.
#   h: finite-difference parameter
#   flj_analytic: analytic result of the Lennard-Jones force, in a.u.
#   flj_numerical: numerical result of the Lennard-Jones force, in a.u.
#
import numpy as np
epsilon=4.e-4 # in a.u.
sigma=6 # in a.u.

h = 1e-5

def finite_diff(f,h):
#finish writing this function for taking finite differences

flj_analytic = 
flj_numerical= 

#plot two curves
import matplotlib.pyplot as plot
plt.figure(figsize=(7,4))
