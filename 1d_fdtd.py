import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
eps0 = 8.8541878128e-12
mu0 = 1.256637062e-6
c0 = 1 / np.sqrt(eps0 * mu0)
imp0 = np.sqrt(mu0 / eps0)

jmax = 500
jsource = 250
nmax = 2000

Ex = np.zeros(jmax)
Hz = np.zeros(jmax)
Ex_prev = np.zeros(jmax)
Hz_prev = np.zeros(jmax)

lambda_min = 350e-9  # meters
dx = lambda_min / 20
dt = dx / c0

eps = eps0


def source_function(t):
    lambda_0 = 550e-9
    w0 = 2 * np.pi * c0 / lambda_0
    tau = 30
    t0 = tau * 3
    return np.exp(-(t - t0) ** 2 / tau ** 2) * np.sin(w0 * t * dt)


fig = plt.figure()
ims = []
for n in range(nmax):
    # Update magnetic field boundaries
    Hz[jmax-1] = Hz_prev[jmax-2]
    # Update magnetic field
    for j in range(jmax - 1):
        Hz[j] = Hz_prev[j] + dt / (dx * mu0) * (Ex[j + 1] - Ex[j])
        Hz_prev[j] = Hz[j]

    # Update electric field boundaries
    Ex[0] = Ex_prev[1]
    # Update electric field
    for j in range(1, jmax):
        Ex[j] = Ex_prev[j] + dt / (dx * eps) * (Hz[j] - Hz[j - 1])
        Ex_prev[j] = Ex[j]
    # Electric field source
    Ex[jsource] += source_function(n + 1)
    Ex_prev[jsource] = Ex[jsource]

    if n % 10 == 0:
        im = plt.plot(Ex, "navy")
        # plt.ylim([-1, 1])
        ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=50, blit=False)
ani.save("tau30source250.gif", writer='pillow')

