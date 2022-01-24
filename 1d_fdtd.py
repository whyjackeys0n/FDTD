import numpy as np
import matplotlib.pyplot as plt

# Define constants
eps0 = 8.8541878128e-12
mu0 = 1.256637062e-6
c0 = 1 / np.sqrt(eps0 * mu0)
imp0 = np.sqrt(mu0 / eps0)

jmax = 500
nmax = 2000

Ex = np.zeros(jmax)
Hz = np.zeros(jmax)
Ex_prev = np.zeros(jmax)
Hz_prev = np.zeros(jmax)

lambda_min = 35e-9
dx = lambda_min/20
dt = dx/c0

for n in range(nmax):
    # Update magnetic field boundaries
    Hz[jmax-1] = Hz_prev[jmax-2]

    for j in range(jmax):
        Hz[j] = Hz_prev[j] + dt/(dx*mu0) * (Ex[j+1] - Ex[j])

