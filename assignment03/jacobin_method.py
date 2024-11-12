import numpy as np

a = np.array([[2.0,-1.0,0.0],[-1.0,3.0,-1.0],[0.0,-1.0,2.0]])
b = np.array([1.0,8.0,-5.0])
x0 = np.zeros(len(b))
n = 1000

for i in range(n):
    x = np.zeros_like(x0)
    for j in range(len(b)):
        s = np.dot(a[j,:],x0) - a[j,j] * x0[j]
        x[j] = (b[j] - s) / a[j,j]
    x0 = x

print(x.astype((int)))