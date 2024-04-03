
import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x0, steps=1000):
    x = np.zeros(steps)
    x[0] = x0
    for i in range(1, steps):
        x[i] = r * x[i-1] * (1 - x[i-1])
     
    return x[100:]

r_values = np.linspace(0, 4, 1000)

for r in r_values:
    r_points = []
    x_points = []
    x = logistic_map(r, 0.8)  
    r_points.append([r] * len(x))  
    x_points.append(x)  
    plt.scatter(r_points, x_points, alpha=0.01, color='blue', marker='.')
    
plt.xlabel('r')
plt.ylabel('x')
plt.title('Logistic Map')
plt.show()
