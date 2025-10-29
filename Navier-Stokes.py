import matplotlib.pyplot as plt # - Plotting - #
from matplotlib.animation import FuncAnimation, PillowWriter # - FuncAnimation for animating, PillowWriter for exporting the animation as a .gif - #
import numpy as np # type: ignore

# - Create a set of numbers for vectors - #
x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)
t = np.linspace(0, 25, 50)

X, Y, T = np.meshgrid(x, y, t, indexing='ij') # - Combine x, y, and t into one 3D grid in a really weird way - #

# - These two combine to create the u [velocity] vector field in 2D. - #
U = np.sin(Y) * T # - u[y] = t * sin(y)î - #
V = np.cos(X) * 2 * T # - u[x] = 2t * cos(x)ĵ - #

# - Replace U, V = 0 with 1e-12 to prevent divison by zero in np.gradient() - #
U = np.where((U == 0) & (V == 0), 1e-12, U)
V = np.where((U == 0) & (V == 0), 1e-12, V)

# - Calculate some small intervals for x, y, and t - #
dx = x[1] - x[0]
dy = y[1] - y[0]
dt = t[1] - t[0]

### - PDEs (18 count) - ###

dudt = np.gradient(U, dt, axis=-1) # - Calculate ∂u[x]/∂t in the x axis - #
dvdt = np.gradient(V, dt, axis=-1) # - Calculate ∂u[y]/∂t in the y axis seperately because Python - #
dudy, dudx = np.gradient(U, dy, dx, axis=(0,1)) # - Calculate ∂u[x]/∂x and ∂u[x]/∂y at the same time - #
dvdy, dvdx = np.gradient(V, dy, dx, axis=(0,1)) # - Calculating ∂u[y]/∂x and ∂u[y]/∂y - # 

conv_u = U * dudx * dudy # - u[x](∇*u[x]) - #
conv_v = V * dvdx * dvdy # - u[y](∇*u[y]) - #

DuDt = dudt + conv_u # - Material derivative, Du[x]/Dt = ∂u[x]/∂t + u[x](∇*u[x]) - #
DvDt = dvdt + conv_v # - Second material derivative, Du[y]/Dt = ∂u[y]/∂t + u[y](∇*u[y]) - #


fig, ax = plt.subplots()
quiv = ax.quiver(X[:, :, 0], Y[:, :, 0], DuDt[:, :, 0], DvDt[:, :, 0], angles='xy', scale_units='xy', scale=1e2)

def update(frame):

    quiv.set_UVC(U[:, :, frame], V[:, :, frame])
    ax.set_title(f"t={t[frame]:.2f}")
    return quiv,

animation = FuncAnimation(fig, update, frames=len(t), interval=300, blit=True)
plt.show()

animation.save("sim.gif", writer=PillowWriter(fps=10), dpi=150)