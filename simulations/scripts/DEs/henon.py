import matplotlib.pyplot as plt
from rk import RK4  

A = 1.4
B = 0.3

xdot = lambda t, x, y: 1 - A * x**2 + y
ydot = lambda t, x, y: B * x

henon_solver = RK4(xdot, ydot)

initial_conditions = [0.1, 0.1]  # Initial coordinates (x, y)
time_points, results = henon_solver.solve(initial_conditions, 0.01, 1000)
plt.plot(results[0], results[1], '.-', markersize=1)  # Use '.' for markers, adjust markersize as needed
plt.xlabel('x')
plt.ylabel('y')
plt.title('Henon Map: x vs y')
plt.show()

