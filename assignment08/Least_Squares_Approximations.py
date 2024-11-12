import numpy as np

def compute_least_squares(A,b):
    Q,R = np.linalg.qr(A)
    x = np.linalg.solve(R,np.dot(Q.T,b))

    print("Least-squares solutions:",x)
A = np.array([[1,-1],
              [1,4],
              [1,-1],
              [1,4]])
b = np.array([-1,6,5,7])

compute_least_squares(A,b)