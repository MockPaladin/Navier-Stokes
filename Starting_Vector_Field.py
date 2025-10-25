#import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)
t = np.linspace(0, 1, 10)

X, Y = np.meshgrid(x, y)

U = np.sin(Y)
V = np.cos(X)

"""
plt.quiver(X, Y, U, V, color='black')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Starting vector field')

plt.axis('equal')

plt.show()
"""