#barplot
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
pok = pd.read_csv('pokemon.csv')
#print(pok.head())
sns.barplot(x='Legendary', y = 'Speed',data= pok ,palette='vlag',hue='Generation'  )
#print(plt.show())

#scatterplot
iris = pd.read_csv('Iris.csv')
#print(iris.head())
sns.scatterplot(x ='SepalLengthCm', y= 'PetalLengthCm',data= iris , hue='Species',style= 'Species')
#print(plt.show())

#distplot(histogram+frequency) if remove histogram ,hist =false 
# if rmove frequency curve kde =False
sns.displot(iris['Species'])
#print(plt.show())

# jointplot (scattered +histogram)  kind = reg is regression on both graph
sns.jointplot(x ='SepalLengthCm', y= 'PetalLengthCm',data= iris, color= 'olive',kind='reg')
#print(plt.show())


###boxplot
sns.boxplot(x ='Species', y= 'PetalLengthCm' ,data= iris,linewidth= 3)
#print(plt.show())

## Pairplot
df = pd.read_csv('Iris.csv')
sns.pairplot(df , hue= 'Species')
print(plt.show())