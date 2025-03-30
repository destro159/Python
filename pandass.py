import pandas as pd
s1 =pd.Series([1,2,3,4,5])
print(s1)

s2 =pd.Series([1,2,3,4,5,6],index =['a','b','c','d','e','f'])
print(s2)

s3 =pd.Series({'a':10,'b':20})
print(s2)
print(s2['b'])
print(s2[:4])
print(s2[-3:])
## data frames
d1 = pd.DataFrame({"name":['bob','sam','john'],"marks":[28,78,89]})
print(d1)
