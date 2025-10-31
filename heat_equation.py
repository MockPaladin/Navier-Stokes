import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

α = 0.2

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
t = np.linspace(0, 50, 100)

X, Y, T = np.meshgrid(x, y, t)

u = np.sqrt(X ** 2 + Y ** 2)

dx = x[1] - x[0]
dy = y[1] - y[0]
dt = 0.1

u_all = [u.copy()]  # store the initial temperature field

for _ in range(10):
    d2udx2 = np.gradient(np.gradient(u, dx, axis=1), dx, axis=1)
    d2udy2 = np.gradient(np.gradient(u, dy, axis=0), dy, axis=0)
    u = u + α * (d2udx2 + d2udy2) * dt  # evolve the field in time
    u_all.append(u.copy())  # store the new field

fig, ax = plt.subplots(figsize=(6, 5)) # type: ignore
cax = ax.imshow(u[:, :, 0], origin='lower', extent=[x.min(), x.max(), y.min(), y.max()], cmap='viridis') # type: ignore
fig.colorbar(cax, label='heat') # type: ignore
ax.set_title('heat(t)') # type: ignore
ax.set_xlabel('X') # type: ignore
ax.set_ylabel('Y') # type: ignore

def update(frame): # type: ignore

  cax.set_array(u[:, :, frame])
  ax.set_title(f'ρ (t={t[frame]:.2f})') # type: ignore
  return [cax] # type: ignore

anim = FuncAnimation(fig, update, frames=len(t), interval=100, blit=True) # type: ignore

writer = PillowWriter(fps=10)
anim.save('heat.gif', writer=writer)