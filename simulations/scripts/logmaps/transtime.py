from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

def log_trans(r,x, step, tol=1e-8):
    fp=(r-1)/r
    count=1
    x_list=[x]
    for i in range(1,step):
        if abs(x_list[i-1]-fp) < tol:
            break
        x_list.append(r*x_list[i-1]*(1-x_list[i-1]))
        count+=1  
    if count == 1:
        print(f"min value of transient steps:{r}")
    return count


r_list=list(np.linspace(2.9, 2.99999, 10000))
stepToNeighbourhood=[]

for r in r_list:
    sum=0
    for k in range(1, 10):
        init = np.random.random()
        sum+=log_trans(r, init, 100000)
    sum = sum / 10
    stepToNeighbourhood.append(sum) 

print(r_list)    
print(stepToNeighbourhood)
#plt.plot(r_list,stepToNeighbourhood)    
#plt.plot()
#plt.xlabel("paramter r")
#plt.ylabel("steps taken to reach within $\epsilon$=1e-8 of tolerance")
#plt.show()


