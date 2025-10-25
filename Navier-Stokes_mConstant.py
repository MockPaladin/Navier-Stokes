import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 25)
y = np.linspace(-np.pi, np.pi, 25)

X, Y = np.meshgrid(x, y)

U = np.sin(X)
V = np.sin(Y)

plt.quiver(X, Y, U, V, color='blue')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Vector Field Visualization')

plt.axis('equal')

plt.show()