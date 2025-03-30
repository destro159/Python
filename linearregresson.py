import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import linearRegression
lr =linearRegression()
iris= pd.read_csv('iris.csv')
print(iris.head())
sns.scatterplot(x='SepalLengthCm',y ='PetalLengthCm',data=iris,hue='Species')
plt.show()
x= iris[['SepalLengthCm']]
y= iris[['PetalLengthCm']]    
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.3)
print(x_train.head())
print(x_test.head())
print(y_train.head())
print(y_test.head())
lr.fit(x_train,y_train)
y_pred = lr.Predict(x_test)
print(y_test.head())
print(y_pred[0:5])


