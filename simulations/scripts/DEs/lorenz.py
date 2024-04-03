import matplotlib.pyplot as plt
import numpy as np
from rk import RK4

sigma = 10.0
rho = 28.0
beta = 8/3

xdot = lambda t, x, y, z: sigma * (y - x)
ydot = lambda t, x, y, z: x * (rho - z) - y
zdot = lambda t, x, y, z: x * y - beta * z

initial_conditions = [1.0, 1.0, 1.0]
h = 0.01  
total_time = 100.0  

solver = RK4(xdot, ydot, zdot)

t, xyz = solver.solve(initial_conditions, h, total_time)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xyz[0], xyz[1], xyz[2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz Attractor')
plt.show()
