import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])
C = np.dot(A,B)

fig,axs = plt.subplots(1,3,figsize=(12,4))

im1 = axs[0].imshow(A,cmap='OrRd',interpolation='nearest',aspect='auto')
axs[0].set_title('Matrix A')
axs[0].axis('off')
cbar1 = plt.colorbar(im1,ax=axs[0],pad=0.02)

im2 = axs[1].imshow(B,cmap='summer',interpolation='nearest',aspect='auto')
axs[1].set_title('Matrix B')
axs[1].axis('off')
cbar2 = plt.colorbar(im2,ax=axs[1],pad=0.02)

im3 = axs[2].imshow(C,cmap='PuBu',interpolation='nearest',aspect='auto')
axs[2].set_title('Matrix C(A × B)')
axs[2].axis('off')
cbar2 = plt.colorbar(im2,ax=axs[2],pad=0.02)

for i in range(3):
    for j in range(3):
        axs[0].text(j,i,str(A[i,j]),ha='center',va='center',color='black')
        axs[1].text(j, i, str(B[i, j]), ha='center', va='center', color='black')
        axs[2].text(j, i, str(C[i, j]), ha='center', va='center', color='black')

plt.tight_layout()
plt.show()
