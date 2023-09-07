# Week 3 Problem 1
# Code to compute the force between two Argon atoms, starting from the Lennard-Jones expression of the potential energy. 
# 
# Variables: 
#   epsilon and sigma: LJ parmeters in atomic units
#   distance: distance between atoms in atomic units
#   flj: magnitude of the force acting on the atoms, with flj = -dU/dr

epsilon = 4.0e-4 # these are a.u.
sigma = 6 # also a.u.
r = #choose your input distance
flj = #complete this line that calculates the forces derived from a LJ potential analytically
print("The force acting on two Argon atoms at a distance of ", distance, " a.u. is equal to", flj, " a.u.")
