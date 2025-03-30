import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
fifa = pd.read_csv('players_20.csv')
#print(fifa.head())
#for col in fifa.columns:
  #  print(col)
#print(fifa.shape)
#print(fifa['nationality'].value_counts())

#print(fifa['nationality'].value_counts()[0:10])

#print(fifa['nationality'].value_counts()[0:10].keys())
#print(plt.bar(fifa['nationality'].value_counts()[0:5].keys(),
       # fifa['nationality'].value_counts()[0:5],color ='g'))
#print(plt.show())
player_salary = fifa[['short_name','wage_eur']]
player_salary.head() 
print(player_salary)
player_salary = player_salary.sort_values(by=['wage_eur'],ascending=False)
#print(player_salary)
#plt.bar(list(player_salary['short_name'])[0:5],list(player_salary['wage_eur'])[0:5],color = ['blue','red','green','pink','yellow'])
#plt.show()
germany =fifa[fifa['nationality'] =='Germany']
#print(germany.head())
germany=germany.sort_values(by=['height_cm'],ascending= False).head()
#print(germany)
germany=germany[['short_name','wage_eur']].sort_values(by = ['wage_eur'],ascending= False).head()
#print(germany)

player_shooting = fifa[['short_name','shooting']].head()
#print(player_shooting.sort_values(by=['shooting'],ascending=False) )
player_defending = fifa[['short_name','defending','nationality','club']].head()
#print(player_defending.sort_values(by=['defending'],ascending=False))


real_madrid = fifa[fifa['club'] =='Real Madrid']
print(real_madrid.sort_values(by=['wage_eur'],ascending=False).head())
print(real_madrid.sort_values(by=['shooting'],ascending=False).head())
print(real_madrid.sort_values(by=['defending'],ascending=False).head())
print(real_madrid['nationality'].value_counts())
print(real_madrid['nationality'])