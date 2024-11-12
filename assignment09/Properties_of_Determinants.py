import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
vertices=[]
def plot_arrow(ax,start,scale,color):
    end=[start[0]+scale[0],start[1]+scale[1],start[2]+scale[2]]

    ax.quiver(start[0],start[1],start[2],scale[0],scale[1],scale[2],color=color,arrow_length_ratio=0.08,linewidths=3)
    ax.text(end[0],end[1],end[2],f"({end[0]},{end[1]},{end[2]})")

    if end not in vertices:
        vertices.append(end)

def plot_3D_det(matrix):
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111,projection='3d')

    det=np.linalg.det(matrix)

    ax.text(0,0,0,f"({0,0},{0,0},{0,0})")
    vertices.append([0,0,0])
    color=['green','blue','red']

    for i in range(3):
        start=[[0,0,0],matrix[(i+1)%3],matrix[(i+2)%3],[matrix[(i+1)%3][j]+matrix[(i+2)%3][j] for j in range(3)]]
        for j in range(4):
            plot_arrow(ax,start[j],matrix[i],color[i])

    faces=[[vertices[1],vertices[3],vertices[4],vertices[2]],
           [vertices[5],vertices[6],vertices[4],vertices[2]],
           [vertices[0],vertices[7],vertices[6],vertices[5]],
           [vertices[0],vertices[1],vertices[3],vertices[7]],
           [vertices[0],vertices[7],vertices[3],vertices[1]],
           [vertices[7],vertices[6],vertices[4],vertices[3]]]
    for face in faces:
        ax.add_collection3d(Poly3DCollection([face],facecolors='gray',linewidths=1,edgecolors='k',alpha=0.1))

    ax.text(matrix[0][0]/2,matrix[1][1]/2,matrix[2][2]/2,f'determinant={det:.2f}',size=12)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.grid()
    plt.show()

matrix=np.array([[2,0,0],[0,3,0],[0,3,4]])
plot_3D_det(matrix)