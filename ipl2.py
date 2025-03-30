import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
deli = pd.read_csv('deliveries.csv')
print(deli.head())
print(deli['match_id'].unique)
pri=deli[deli['match_id']==1]
print(pri.head())