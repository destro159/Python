import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
ipl = pd.read_csv('matches.csv')
#print(ipl.head())
print(ipl.shape)
print(ipl['player_of_match'].value_counts())
print(ipl['player_of_match'].value_counts()[0:10])
print(ipl['player_of_match'].value_counts()[0:5])
print(list(ipl['player_of_match'].value_counts()[0:5].keys()))  # returns the index of the list
s1 = plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys())
             ,list(ipl['player_of_match'].value_counts()[0:5]),color = 'r')
plt.title('MAN OF THE MATCH ')
plt.xlabel('player')
plt.ylabel('counts')
#plt.show()
#print(ipl['result'].value_counts())
#print(ipl['toss_winner'].value_counts())
batting_first = ipl[ipl['result_margin']!=0]
#print(batting.head())
plt.figure(figsize=(4,6))
plt.hist(batting_first['result_margin'])
plt.title('distribution of run')
plt.xlabel('runs')
plt.show()
print(ipl['season'].value_counts())
print(ipl['city'].value_counts())





