'''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''
import pandas as pd
from pandas import read_csv
from seaborn import scatterplot, relplot, histplot
from matplotlib.pyplot import show


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
unique_values = data['whoAmI'].unique()
one_hot_df = pd.DataFrame(0, index=data.index, columns=unique_values)
for value in unique_values:
    one_hot_df.loc[data['whoAmI'] == value, value] = 1
data.head()

print(data)
print(one_hot_df)



