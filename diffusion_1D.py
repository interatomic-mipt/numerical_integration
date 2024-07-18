#generated with ChatGPT

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
L = 500        # Number of grid points
T = 500       # Number of time steps
Da = 0.5       # Diffusion coefficient of A
Db = 0.5      # Diffusion coefficient of B
dx = 1         # Spatial step size
dt = 0.5       # Time step size

# Initialize concentrations
A = np.zeros(L)
B = np.zeros(L)

# Add initial A and B concentration in a small region
A[L//2 - 150:L//2 - 50] = 0.75
B[L//2 - 50:L//2 + 50] = 1

# Function to perform the diffusion in 1D
def diffuse(C, D, dx, dt):
    dCdt = D * (np.roll(C, 1) + np.roll(C, -1) - 2 * C) / (dx * dx)
    return C + dCdt * dt

# Prepare the plot
fig, ax = plt.subplots()
line1, = ax.plot(A, label='A')
line2, = ax.plot(B, label='B')
ax.set_ylim(0, 1.2)
plt.title('Diffusion of A and B in 1D')
plt.xlabel('Position')
plt.ylabel('Concentration')
plt.legend()

# Animation update function
def update(t):
    global A, B
    
    # Diffuse both A and B
    for i in range(100):
        A = diffuse(A, Da, dx, dt)
        B = diffuse(B, Db, dx, dt)

    # Update the plot data
    line1.set_ydata(A)
    line2.set_ydata(B)
    ax.set_title(f'Time step: {t}')
    return line1, line2

# Create animation
ani = animation.FuncAnimation(fig, update, 100)

plt.show()
