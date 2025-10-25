from scipy.integrate import odeint # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib.animation import FuncAnimation, PillowWriter # type: ignore
import numpy as np # type: ignore
import os

x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)
t = np.linspace(0, 25, 20)

X, Y, T = np.meshgrid(x, y, t, indexing='ij')

U = np.sin(Y) * T
V = np.cos(X) * 2 * T

U = np.where((U == 0) & (V == 0), 1e-12, U)
V = np.where((U == 0) & (V == 0), 1e-12, V)

dx = x[1] - x[0]
dy = y[1] - y[0]
dt = t[1] - t[0]

dudt = np.gradient(U, dt, axis=-1)
dvdt = np.gradient(V, dt, axis=-1)
dudy, dudx = np.gradient(U, dy, dx, axis=(0,1))
dvdy, dvdx = np.gradient(V, dy, dx, axis=(0,1))

conv_u = U * dudx * dudy
conv_v = U * dudx * dudy

DuDt = dudt + conv_u
DvDt = dvdt + conv_v

"""for time in range(0, 10):

    plt.quiver(X[:, :, time], Y[:, :, time], DuDt[:, :, time], DvDt[:, :, time])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Plot at t={time}')
    plt.savefig(os.path.join('images', f't{time}.png'))

"""

fig, ax = plt.subplots()
quiv = ax.quiver(X[:, :, 0], Y[:, :, 0], DuDt[:, :, 0], DvDt[:, :, 0], angles='xy', scale_units='xy', scale=1e2)

def update(frame):

    quiv.set_UVC(U[:, :, frame], V[:, :, frame])
    ax.set_title(f"t={t[frame]:.2f}")
    return quiv,

animation = FuncAnimation(fig, update, frames=len(t), interval=300, blit=True)
plt.show()

animation.save("sim.gif", writer=PillowWriter(fps=10), dpi=150)