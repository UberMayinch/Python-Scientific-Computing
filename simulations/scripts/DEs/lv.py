import matplotlib.pyplot as plt
from rk import RK4

A1 = .1
A2 = .05
B1 = .01
B2 = 0.001

xdot = lambda t, x, y: A1*x - x*y*B1
ydot = lambda t, x, y: B2*x*y - A2*y

lv = RK4(xdot, ydot)
t, y = lv.solve([80, 40], .1, 250)

plt.plot(t, y[0], t, y[1])
plt.show()
