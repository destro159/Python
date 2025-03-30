import pandas as pd
read1 = pd.read_csv('Iris.csv')
print(read1.head())
print(read1.tail())
print(read1.describe())
print(read1.shape)
print(read1.iloc[0:4,0:3])
#print(read1.loc[0:4,('SepalLength','Petallength')])
print(read1.drop('SepalLengthCm',axis=1))
print(read1.drop([1,2,3],axis=0))
def half(s):
    return s*.5
r1 = read1[['SepalLengthCm','PetalLengthCm']].apply(half)   # apply operation on particaluar column as per need

print(r1)
r2 = read1['Species'].value_counts()
print(r2)
r3 = read1.sort_values(by='SepalLengthCm')
print(r3)