from scipy.integrate import odeint # type: ignore
import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
t = np.linspace(0, 1, 10)

X, Y, T = np.meshgrid(x, y, t)

U = np.sin(Y) * T
V = np.cos(X) * 2 * T

dx = x[1] - x[0]
dy = y[1] - y[0]
dt = t[1] - t[0]

dudt = np.gradient(U, dt, axis=2)
dvdt = np.gradient(V, dt, axis=2)
dudy, dudx = np.gradient(U, dy, dx, axis=(0,1))
dvdy, dvdx = np.gradient(V, dy, dx, axis=(0,1))

conv_u = U * dudx * dudy
conv_v = U * dudx * dudy

DuDt = dudt + conv_u
DvDt = dvdt + conv_v

time = 1 # only works in [0, 1]

plt.quiver(X[:, :, time], Y[:, :, time], DuDt[:, :, time], DvDt[:, :, time])

plt.xlabel('x')
plt.ylabel('y')
plt.show()