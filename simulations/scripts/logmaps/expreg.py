import scipy as sp
import numpy as np

r_list=np.linspace(2.00, 2.99, 100)
stepToNeighbourhood=[1, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 16, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 23, 23, 24, 25, 25, 26, 27, 28, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 44, 46, 47, 49, 52, 54, 56, 59, 62, 65, 68, 72, 76, 81, 86, 92, 99, 106, 115, 125, 137, 151, 168, 190, 217, 254, 305, 381, 507, 756, 1000]
print(len(r_list))
print(len(stepToNeighbourhood))
def exponential(x, a):
    return a*np.exp(x)

exp_coeff, _=sp.optimize.curve_fit(exponential, r_list, stepToNeighbourhood)
print(exp_coeff)

MSE=0
for i in range(1, 100):
    MSE+=(stepToNeighbourhood[i]-exponential(r_list[i], exp_coeff))**2

print(MSE)
