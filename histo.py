import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
n1 =[1,3,3,3,3,3,9,9,9,4,5,4,4,8,8,8,6,6,6,6,7,7]
plt.hist(n1,color='y',bins =4) # bins = no. of bars 
plt.show()

iris =pd.read_csv('Iris.csv')
iris.head()
plt.hist(iris['SepalLengthCm'],bins =30, color ='r')
plt.show()