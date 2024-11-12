import random
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def matrix_vector_product(matrix,vector):
    return np.dot(matrix,vector)
def normalize(vector):
    norm=np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm
def dot_product(vector1,vector2):
    return np.dot(vector1,vector2)
def print_vector(vector):
    n = len(vector)
    for i in range(n):
        if i != n-1:
            print("{:.4f},".format(vector[i]),end=" ")
        else:
            print("{:.4f}".format(vector[i]),end="")
    print("]")

def power_method(matrix,max_iterations=2000,tolerance=1e-5):
    initial_vector=[1.0,1.0,1.0]
    right_vector=[0.41,0.41,0.82]

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')

    for iteration in range(max_iterations):
        eigenvector = matrix_vector_product(matrix,initial_vector)
        eigenvector=normalize(eigenvector)
        eigenvalue=dot_product(eigenvector,matrix_vector_product(matrix,eigenvector))
        diff_squared_sum=np.sum((eigenvector-initial_vector) ** 2)
        if math.sqrt(diff_squared_sum)<tolerance:
            break
        print("Iter",iteration,end=" ")
        print(",eigenvector=[",end="")
        print_vector(eigenvector)

        ax.cla()

        ax.quiver(0,0,0,eigenvector[0],eigenvector[1],eigenvector[2],color='blue',label='eigen vector',
                  alpha=0.8,
                  lw=1.5,arrow_length_ratio=0.2)
        ax.quiver(0,0,0,right_vector[0],right_vector[1],right_vector[2],color='red',label='right eigen vector',
                  alpha=0.8,lw=1.5,arrow_length_ratio=0.2)

        ax.text(eigenvector[0],eigenvector[1],eigenvector[2],
                f'({eigenvector[0]:.2f},{eigenvector[1]:.2f},{eigenvector[2]:.2f})')
        ax.text(right_vector[0],right_vector[1],right_vector[2],
                f'({right_vector[0]:.2f},{right_vector[1]:.2f},{right_vector[2]:.2f})')

        ax.set_xlim([-1,1])
        ax.set_ylim([-1,1])
        ax.set_zlim([-1,1])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.legend()

        ax.set_title(f'Iteration{iteration+1}')

        ax.grid(True)

        plt.pause(2)

        initial_vector = eigenvector

    plt.close()
    return eigenvalue,eigenvector
matrix=[[1,-3,3],
        [3,-5,3],
        [6,-6,4]]
max_eigenvalue,eigenvector=power_method(matrix)
print("The Maximum Eigenvalue = ","{:.4f}".format(max_eigenvalue))
print("The Corresponding Eigenvector = [",end="")
print_vector(eigenvector)
