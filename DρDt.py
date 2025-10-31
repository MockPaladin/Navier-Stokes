import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
t = np.linspace(0, 50, 100)

X, Y, T = np.meshgrid(x, y, t)

V = np.sqrt(X ** 2 + Y ** 2)

rho = V * np.exp(-0.05 * T)

rho = np.where((rho == 0), 1e-12, rho) # - Replace rho=0 with rho=1e-12 to prevent vision by zero - #

dx = x[1] - x[0]
dy = y[1] - y[0]
dt = t[1] - t[0]

drhodt = np.gradient(rho, dt, axis=-1)
drhody, drhodx = np.gradient(rho, dy, dx, axis=(0,1))

conv_rho = rho * drhodx * drhody

DrhoDt = drhodt + conv_rho

fig, ax = plt.subplots(figsize=(6, 5)) # type: ignore
cax = ax.imshow(rho[:, :, 0], origin='lower', extent=[x.min(), x.max(), y.min(), y.max()], cmap='viridis') # type: ignore
fig.colorbar(cax, label='ρ') # type: ignore
ax.set_title('ρ(t)') # type: ignore
ax.set_xlabel('X') # type: ignore
ax.set_ylabel('Y') # type: ignore

def update(frame): # type: ignore

  cax.set_array(rho[:, :, frame])
  ax.set_title(f'ρ (t={t[frame]:.2f})') # type: ignore
  return [cax] # type: ignore

anim = FuncAnimation(fig, update, frames=len(t), interval=100, blit=True) # type: ignore

writer = PillowWriter(fps=15)
anim.save('rho.gif', writer=writer)