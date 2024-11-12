import numpy as np
import matplotlib.pyplot as plt

vectors_set_1 = np.array([[2,4,5],[-4,-8,-6]])
vectors_set_2 = np.array([[3,5,7],[5,8,4]])

dot_product_set_1 = np.dot(vectors_set_1[0],vectors_set_1[1])
dot_product_set_2 = np.dot(vectors_set_2[0],vectors_set_2[1])

if (dot_product_set_1 == 0):
    isDependent_1 = 1
else:
    isDependent_1 = 0

if(dot_product_set_2 == 0):
    isDependent_2 = 1
else:
    isDependent_2 = 0

fig = plt.figure()
ax = fig.add_subplot(111,projection = "3d")

origin = np.zeros(3)

for vector in vectors_set_1:
    ax.quiver(*origin,*vector,color="blue",label="set1")
for vector in vectors_set_2:
    ax.quiver(*origin,*vector,color="red",label="set2")

ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
ax.set_zlim([-10,10])

if (isDependent_1):
    print("Vectors set1 is dependent.")
else:
    print("Vectors set1 is independent.")

if (isDependent_2):
    print("Vectors set2 is dependent.")
else:
    print("Vectors set2 is independent.")

plt.legend()
plt.show()