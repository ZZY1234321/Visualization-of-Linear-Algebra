import numpy as np
import matplotlib.pyplot as plt

u1 = np.array([2,5,-1])
u2 = np.array([-2,1,1])
y = np.array([1,2,3])

projection_u1 = ((np.dot(y,u1)/np.dot(u1,u1))*u1)
projection_u2 = ((np.dot(y,u2)/np.dot(u2,u2))*u2)
projection = projection_u1 + projection_u2

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax.quiver(0,0,0,u1[0],u1[1],u1[2],color='r',label='u1')
ax.quiver(0,0,0,u2[0],u2[1],u2[2],color='b',label='u2')
ax.quiver(0,0,0,y[0],y[1],y[2],color='g',label='y')
ax.quiver(0,0,0,projection[0],projection[1],projection[2],color='b',label='projection')

for vec in [projection_u1,projection_u2]:
    ax.plot([y[0],vec[0]],[y[1],vec[1]],[y[2],vec[2]],linestyle='dashed',color='gray')

ax.set_xlim([-3,3])
ax.set_ylim([-3,3])
ax.set_zlim([-3,3])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()