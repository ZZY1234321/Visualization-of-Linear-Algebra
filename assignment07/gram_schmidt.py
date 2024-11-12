import matplotlib.pyplot as plt
import numpy as np
def draw_basis_vector(u1,u2,u3,X,Y,Z):
    fig=plt.figure(figsize=(12,12))
    ax=fig.add_subplot(projection='3d')
    ax.plot_wireframe(X,Y,Z,linewidth=1.5,alpha=0.3)

    vectors = [
        {'data':u1,'label':r'$\mathbf{u}_1$','color':'red'},
        {'data':u2,'label':r'$\mathbf{u}_2$','color':'blue'},
        {'data':u3,'label':r'$\mathbf{u}_3$','color':'green'}
    ]

    for vector in vectors:
        ax.quiver(0,0,0,vector['data'][0],vector['data'][1],vector['data'][2],length=1,normalize=False,
                  color=vector['color'],alpha=0.6,arrow_length_ratio=0.08,pivot='tail',linewidth=3)
        ax.text(vector['data'][0],vector['data'][1],vector['data'][2],vector['label'],size=15)

    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')

    ax.set_xlim([-10,10])
    ax.set_ylim([-10,10])
    ax.set_zlim([-10,10])
    plt.show()

def draw_orthogonal_basis_vector_v1_v2(u1,u2,u3,X,Y,Z):
    v1=u1
    v2=u2-(u2@v1)/(v1@v1)
    alpha=(u2@v1)/(v1@v1)
    projW_u2=[alpha*v1[0],alpha*v1[1],alpha*v1[2]]
    fig=plt.figure(figsize=(12,12))
    ax=fig.add_subplot(projection='3d')
    ax.plot_wireframe(X,Y,Z,linewidth=1.5,alpha=0.3)

    vectors = [
        {'data':u1,'label':r'$\mathbf{u}_1=\mathbf{v}_1$','color':'red'},
        {'data':u2,'label':r'$\mathbf{u}_2$','color':'blue'},
        {'data':u3,'label':r'%\mathbf{u}_3$','color':'green'},
        {'data':v2,'label':r'$\mathbf{v}_2$','color':'purple'},
        {'data':projW_u2,'label':r'$\mathbf{\hat{u}}_2$','color':'blue'}
    ]
    for vector in vectors:
        ax.quiver(0,0,0,vector['data'][0],vector['data'][1],vector['data'][2],length=1,normalize=False,
                  color=vector['color'],alpha=0.6,arrow_length_ratio=0.08,pivot='tail',linewidth=3)
        ax.text(vector['data'][0],vector['data'][1],vector['data'][2],vector['label'],size=15)
    ax.plot([projW_u2[0],u2[0]],[projW_u2[1],u2[1]],[projW_u2[2],u2[2]],c='b',lw=3.5,alpha=0.5,ls='--')
    ax.plot([v2[0],u2[0]],[v2[1],u2[1]],[v2[2],u2[2]],c='b',lw=3.5,alpha=0.5,ls='--')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    plt.show()
    return v1,v2,projW_u2
def draw_orthogonal_basis_vector_v1_v3(u1,u2,u3,v1,v2,X,Y,Z,projW_u2):
    projW_u3=(u3@v1)/(v1@v1)*v1+(u3@v2)/(v2@v2)*v2
    v3=u3-projW_u3
    fig=plt.figure(figsize=(12,12))
    ax=fig.add_subplot(projection='3d')
    ax.plot_wireframe(X,Y,Z,linewidth=1.5,alpha=0.3)
    vectors = [
        {'data':u1,'label':r'$\mathbf{u}_1=\mathbf{v}_1$','color':'red'},
        {'data':u2,'label':r'$\mathbf{u}_2$','color':'red'},
        {'data':u3,'label':r'$\mathbf{u}_3$','color':'red'},
        {'data':v2,'label':r'$$\mathf{v}_2$','color':'purple'},
        {'data':projW_u3,'label':r'$\hat{\mathbf{u}}_3$','color':'black'},
        {'data':projW_u2,'label':r'$\mathbf{\hat{u}}_2$','color':'blue'},
        {'data':v3,'label':r'$\mathbf{v}_3$','color':'purple'}
    ]
    for vector in vectors:
        ax.quiver(0,0,0,vector['data'][0],vector['data'][1],vector['data'][2],length=1,normalize=False,
                  color=vector['color'],alpha=0.6,arrow_length_ratio=0.08,pivot='tail',linewidth=3)
        ax.text(vector['data'][0],vector['data'][1],vector['data'][2],vector['label'],size=15)

    ax.plot([projW_u2[0],u2[0]],[projW_u2[1],u2[1]],[projW_u2[2],u2[2]],c='b',lw=3.5,alpha=0.5,ls='--')
    ax.plot([v2[0],u2[0]],[v2[1],u2[1]],[v2[2],u2[2]],c='b',lw=3.5,alpha=0.5,ls='--')
    ax.plot([projW_u3[0],u3[0]],[projW_u3[1],u3[1]],[projW_u3[2],u3[2]],c='b',lw=3.5,alpha=0.5,ls='--')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    plt.show()

u1 = np.array([5, 6, 4], dtype=np.float64)
u2 = np.array([2, 4, 8], dtype=np.float64)
u3 = np.array([6, -6, 4], dtype=np.float64)
s = np.linspace(-1,1,10)
t = np.linspace(-1,1,10)
S,T = np.meshgrid(s,t)
X = u1[0]*S+u2[0]*T
Y = u1[1]*S+u2[1]*T
Z = u1[2]*S+u2[2]*T
draw_basis_vector(u1,u2,u3,X,Y,Z)
v1,v2,projW_u2 = draw_orthogonal_basis_vector_v1_v2(u1,u2,u3,X,Y,Z)
draw_orthogonal_basis_vector_v1_v3(u1,u2,u3,v1,v2,X,Y,Z,projW_u2)
