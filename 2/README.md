# Week 3 Assignment 2

Now that you've implemented an analytic formula for the force between two Argon atoms, in this assignment, you will implement an approximate estimate of the force using finite differences. If you remember your Calculus course, the derivative of a function can be written as the limit of the difference quotient:

<a href="https://www.codecogs.com/eqnedit.php?latex=f'(x)=\lim_{h\rightarrow0}\frac{f(x&plus;h)-f(x)}{h}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f'(x)=\lim_{h\rightarrow0}\frac{f(x&plus;h)-f(x)}{h}" title="f'(x)=\lim_{h\rightarrow0}\frac{f(x+h)-f(x)}{h}" /></a>

Using this formula, we can compute the LJ force at a given separation between the atoms as 

<a href="https://www.codecogs.com/eqnedit.php?latex=F^{LJ}(r)=-\lim_{h\rightarrow0}\frac{U^{LJ}(r&plus;h)-U^{LJ}(r)}{h}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F^{LJ}(r)=-\lim_{h\rightarrow0}\frac{U^{LJ}(r&plus;h)-U^{LJ}(r)}{h}" title="F^{LJ}(r)=-\lim_{h\rightarrow0}\frac{U^{LJ}(r+h)-U^{LJ}(r)}{h}" /></a>

TASK: Given the expression for the Lennard-Jones potential energy, compute the associated magnitude of the force between two atoms using the formula above, assuming that *h* is a fixed numerical parameter: as this value becomes smaller, we approach the result of the limit, thus we should get close to the exact derivative.

Plot the force calculated analytically and calculated numerically by finite differences.

EXPECTED OUTCOME: Two curves that should agree with each other within a small numerical error. Tip: To avoid two curves overlapping each other so that one curve becomes blocked by the other, plot one using a solid line and the other using dots.