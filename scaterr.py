import numpy as np
from matplotlib import pyplot as plt        
n1 =[10,20,30,40,50,60,70,80]
n2 =[3,5,7,9,8,7,6,5]
n3 = [5,6,5,8,9,7,3,2]
plt.subplot(1,2,1)
plt.scatter(n1,n2,marker="*",c='g',s=90)
plt.subplot(1,2,2)
plt.scatter(n1,n3,marker=".",c='r',s=190)
plt.show()