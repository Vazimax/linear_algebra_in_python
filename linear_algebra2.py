import matplotlib.pyplot as plt 
import numpy as np

v1 = np.array([1,-4,6,2])
v2 = np.array([2,0,3,1])

np.dot(v1,v2)

v3 = np.array([0,8,1,999997])
np.dot(v2,v3)

vector1 = np.array([5,-5,])
vector2 = np.array([5,5,])
vector3 = np.array([2,3,])

np.dot(vector1,vector2)
np.dot(vector2,vector3)

plt.plot([0,vector1[0]],[0,vector1[1]],'go-',label="vector1")
plt.plot([0,vector2[0]],[0,vector2[1]],'bs-',label="vector2")
plt.plot([0,vector3[0]],[0,vector3[1]],'ko-',label="vector3")

plt.axis('square')
plt.grid()
plt.legend()
plt.show()