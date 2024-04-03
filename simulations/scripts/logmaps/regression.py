import scipy as sp
import numpy as np
import math

r_list=np.linspace(1.01, 2.99, 199)
print(len(r_list))
stepToNeighbourhood=[1000, 713, 485, 368, 297, 248, 213, 187, 166, 150, 136, 124, 114, 106, 99, 92, 87, 81, 77, 73, 69, 66, 62, 59, 57, 54, 52, 50, 48, 46, 44, 43, 41, 40, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 26, 25, 24, 23, 23, 22, 22, 21, 20, 20, 19, 19, 18, 18, 17, 17, 17, 16, 16, 15, 15, 15, 14, 14, 13, 13, 13, 12, 12, 12, 11, 11, 11, 10, 10, 10, 9, 9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 6, 5, 5, 4, 1, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 16, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 23, 23, 24, 25, 25, 26, 27, 28, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 41, 42, 44, 46, 47, 49, 52, 54, 56, 59, 62, 65, 68, 72, 76, 81, 86, 92, 99, 106, 115, 125, 137, 151, 168, 190, 217, 254, 305, 381, 507, 756, 1000]
def parabolic(x, a, b, c):
    return a*(x**2)+b*(x)+c

def exponential(x, a):
    return a*math.exp(x)

par_coeff, _=sp.optimize.curve_fit(parabolic, r_list, stepToNeighbourhood)
print(type(par_coeff))

MSE=0

for i in range(1, 100):
    MSE+=(stepToNeighbourhood[i]-parabolic(r_list[i], par_coeff[0], par_coeff[1],par_coeff[2]))**2

print(MSE)
