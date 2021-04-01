import matplotlib.pyplot as plt
import numpy as np
x = [17,18,15,15.5]
np.mean(x)
plt.plot(1,3,'rs')
plt.show()
x = np.arange(-9,9)
y = x**2

plt.plot(x,y,'r')
plt.plot(x,y/2,'bo')
plt.show()

plt.plot([-3,0],[1,-1],label="first line")
plt.plot([-6,0],[4,-1],label="second one")
plt.legend()
plt.show()

r = np.random.randint(1,11,size=(5,5))
print(r)

x = plt.imshow(r)
plt.show(x)