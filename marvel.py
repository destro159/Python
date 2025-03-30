import pandas as pd
from matplotlib import pyplot as plt
marvel = pd.read_csv("marvel_demo_stats_powers.csv")
print(marvel.head())
good1 = marvel['Alignment_x'].value_counts()
print(good1)
good1 = marvel[marvel['Alignment_x']=='good']
print(good1.sort_values(by=['Speed'],ascending=False))
good1.sort_values(by=['Total'],ascending=False)
print(good1.head())
plt.bar(list(good1['Name'])[0:5],list(good1['Total'])[0:5],color ='g')
plt.show()