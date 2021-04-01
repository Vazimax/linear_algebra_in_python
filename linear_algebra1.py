import matplotlib.pyplot as plt 
import numpy as np

vector = np.array([2,4])
x1 = 2
x2 = .5
x3 = -1

plt.plot([0,vector[0]],[0,vector[1]],'bs-',label='v')
plt.plot([0,x1*vector[0]],[0,x1*vector[1]],'ro-',label='v*x1')
plt.plot([0,x2*vector[0]],[0,x2*vector[1]],'kp-',label='v*x2')
plt.plot([0,x3*vector[0]],[0,x3*vector[1]],'g*-',label='v*x3')

plt.axis('square')
plt.xlim([-4,4])
plt.ylim([-4,4])
plt.grid()
plt.legend()
plt.show()

vector = np.random.randint(1,11,size=(2,1))
x1 = 3
x2 = -4

plt.plot([0,vector[0]],[0,vector[1]],'bs-',label="v")
plt.plot([0,x1+x2],[0,x1+x2],'go-',label="v")
plt.plot([0,x1-x2],[0,x1-x2],'ks-',label="v")
plt.plot([0,(x1*4)+(x2/2)],[0,(x1*4)+(x2/2)],'go-',label="v")



plt.grid()
plt.show()