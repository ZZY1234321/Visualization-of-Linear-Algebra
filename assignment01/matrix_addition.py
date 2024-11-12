import numpy as np
import matplotlib.pyplot as plt

u = np.array([4,7])
v = np.array([8,4])

w = u + v
z = v - u

plt.quiver(0,0,*u,angles='xy',scale_units='xy',scale=1,color='r',label='u')
plt.quiver(0,0,*v,angles='xy',scale_units='xy',scale=1,color='b',label='v')
plt.quiver(u[0],u[1],*v,angles='xy',scale_units='xy',scale=1,color='b')
plt.quiver(v[0],v[1],*u,angles='xy',scale_units='xy',scale=1,color='r')
plt.quiver(0,0,*w,angles='xy',scale_units='xy',scale=1,color='g',label='u+v')
plt.text(u[0],u[1],'u',color='black')
plt.text(v[0],v[1],'v',color='black')
plt.text(w[0],w[1],'u+v',color='black')
plt.xlim(0,15)
plt.ylim(0,15)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Vector Addition')
plt.legend()
plt.grid()
plt.show()

print("u + v = ",w)
