from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns

def dot_product(vector1,vector2):
    result=0
    for i in range(len(vector1)):
        result += vector1[i]*vector2[i]
    return result
def outer_product(vector1,vector2):
    result=[[0]*len(vector2) for _ in range(len(vector1))]
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            result[i][j]=vector1[i]*vector2[j]
    return result
def matrix_vector_multiply(matrix,vector):
    rows,cols=len(matrix),len(matrix[0])
    result=[0]*rows
    for i in range(rows):
        for j in range(cols):
            result[i]+=matrix[i][j]*vector[j]
    return result
def matrix_matrix_multiply(matrix1,matrix2):
    rows1=len(matrix1)
    cols1=len(matrix1[0])
    cols2=len(matrix2[0])
    result=[[0]*cols2 for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k]*matrix2[k][j]
    return result
def matrix_transpose(matrix):
    rows,cols=len(matrix),len(matrix[0])
    transposed=[[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i]=matrix[i][j]
    return transposed
def norm(vector):
    result=0
    for x in vector:
        result +=x ** 2
    return sqrt(result)
def normalize(vector):
    result_norm=norm(vector)
    return [element / result_norm for element in vector]
def print_vector(vector):
    n = len(vector)
    for i in range(n):
        if i != n-1:
            print("{:.4f},".format(vector[i]),end=" ")
        else:
            print("{:.4f}".format(vector[i]),end="")
    print("]")

def power_method(matrix,max_iterations=2000,tolerance=1e-8):
    initial_vector=[1,1,0]
    diff=[0,0,0]
    eigenvector=initial_vector
    eigenvalue=0
    final_iteration=0
    for iteration in range(max_iterations):
        eigenvector=matrix_vector_multiply(matrix,initial_vector)
        eigenvector=normalize(eigenvector)
        eigenvalue=dot_product(eigenvector,matrix_vector_multiply(matrix,eigenvector))

        for i in range(len(eigenvector)):
            diff[i]=eigenvector[i]-initial_vector[i]
        if norm(diff) < tolerance:
            final_iteration = iteration
            break
        initial_vector = eigenvector
    print("Iter",final_iteration,end=" ")
    print(",eigenvalue = ","{:.4f},".format(eigenvalue),end=" ")
    print(",eigenvector = [",end="")
    print_vector(eigenvector)
    return eigenvector,eigenvalue
def svd(A):
    n,m = len(A),len(A[0])
    k=min(n,m)
    singularValues = [0] * k
    us = [[0]*k for _ in range(n)]
    vs = [[0]*m for _ in range(k)]
    matrixForsvd = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrixForsvd[i][j] = A[i][j]
    for i in range(k):
        v,eigenvalue=power_method(
            matrix_matrix_multiply(matrix_transpose(matrixForsvd),matrixForsvd))
        sigma=sqrt(eigenvalue)
        u = [element / sigma for element in matrix_vector_multiply(A,v)]
        singularValues[i] = sigma
        for row in range(len(us)):
            us[row][i] = u[row]
        for col in range(len(vs[0])):
            vs[i][col] = v[col]
        outer_u_v = outer_product(u,v)
        for p in range(n):
            for q in range(m):
                matrixForsvd[p][q] -= sigma * outer_u_v[p][q]
    return us, singularValues, vs
def add_annotations(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if abs(matrix[i][j]) <= 1e-8 and abs(matrix[i][j]) != 0:
                plt.text(j + 0.5,i+0.5, '~0,00',
                         ha='center',va='center',color='black',fontsize=12)
            elif abs(matrix[i][j]) == 0:
                plt.text(j+0.5,i+0.5,'Not Stored',
                         ha='center',va='center',color='black',fontsize=7)
            else:
                plt.text(j+0.5,i+0.5,f'{matrix[i][j]:.2f}',
                         ha='center',va='center',color='black',fontsize=12)
def draw(A,u,sigma,v,axs,index):
    title_A = ['$A=U*S*V$','$U\' *S\'*V\'$', '$U\'\'*S\'\'*V\'\'$',
               '$U*S*V$']
    title_U = ['$U$','$U\' \ (Compression \ rate \ 66 \\%)$', '$U\'\' \ (Compression \ rate \ 33\\%)$',
               '$U$']
    title_S = ['$S$','$S\' \ (Compression \ rate \ 66 \\%)$', '$S\'\' \ (Compression \ rate \ 33\\%)$',
               '$S$']
    title_V = ['$V$','$V\' \ (Compression \ rate \ 66 \\%)$', '$V\'\' \ (Compression \ rate \ 33\\%)$',
               '$V$']

    plt.sca(axs[0])
    ax=sns.heatmap(A,cmap='Wistia',vmax=2,vmin=1)
    ax.set_aspect(0.6)
    plt.title(title_A[index],size=10)
    add_annotations(A)
    ax.tick_params(axis='both',labelsize=8)
    cbar=ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=8)

    plt.sca(axs[1])
    ax=sns.heatmap(u,cmap='Wistia',vmax=1,vmin=-1)
    ax.set_aspect(0.6)
    plt.title(title_U[index],size=10)
    add_annotations(u)
    ax.tick_params(axis='both',labelsize=8)
    cbar=ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=8)

    plt.sca(axs[2])
    ax=sns.heatmap(sigma,cmap='Wistia',vmax=7,vmin=0)
    ax.set_aspect(0.6)
    plt.title(title_S[index],size=10)
    add_annotations(sigma)
    ax.tick_params(axis='both',labelsize=8)
    cbar=ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=8)

    plt.sca(axs[3])
    ax=sns.heatmap(v,cmap='Wistia',vmax=1,vmin=-1)
    ax.set_aspect(0.6)
    plt.title(title_V[index],size=10)
    add_annotations(v)
    ax.tick_params(axis='both',labelsize=8)
    cbar=ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=8)

A=[[2.0,2.0,2.0],
   [2.0,1.0,1.0],
   [2.0,2.0,2.0],
   [1.0,1.0,2.0],
   [2.0,2.0,2.0]]

fig,axs = plt.subplots(nrows=4,ncols=4,figsize=(12,10))
m=len(A)
n=len(A[0])

u,sigma,v = svd(A)
sigma = [[sigma[i] if j == i else 0 for j in range(n)] for i in range(n)]

draw(A,u,sigma,v,axs[0],0)
u_new = [[0] * n for _ in range(m)]
sigma_new = [[0] * n for _ in range(n)]
v_new = [[0] * n for _ in range(n)]
for k in range(0,len(sigma)):
    for i in range(len(u)):
        for j in range(k+1):
            u_new[i][j] = u[i][j]
    for i in range(k+1):
        for j in range(len(sigma[0])):
            sigma_new[i][j] = sigma[i][j]
    for i in range(k+1):
        for j in range(len(v[0])):
            v_new[i][j] = v[i][j]
    A_new = matrix_matrix_multiply(matrix_matrix_multiply(u_new,sigma_new),v_new)

    draw(A_new,u_new,sigma_new,v_new,axs[k+1],k+1)

plt.tight_layout()
plt.show()