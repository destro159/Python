import numpy as np
from matplotlib import pyplot as plt
x  = np.arange(1,11)
y  = x*2
z  = x*3
plt.subplot(1,2,1)
plt.plot(x,y,color ='g',linestyle=':',linewidth =5)
plt.title('line plot')
plt.xlabel('x label')
plt.ylabel('y label')
plt.subplot(1,2,2)
plt.plot(x,z,color ='r',linestyle='-',linewidth =7)
plt.title('line plot')
plt.xlabel('x label')
plt.ylabel('y label')
plt.grid(True)
plt.show()

