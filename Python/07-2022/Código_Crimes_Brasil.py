from array import array
from gettext import npgettext
import os
from re import X
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados_1 = pd.read_excel('C:/Users/natha/Documents/Crimes_2021.xlsx')
dados_2 = pd.read_excel('C:/Users/natha/Documents/Crimes_2019.xlsx')
dados_3 = pd.read_excel('C:/Users/natha/Documents/Crimes_2017.xlsx')
dados_4 = pd.read_excel('C:/Users/natha/Documents/Crimes_2015.xlsx')
coluna_1 = dados_1['Ocorrências']
coluna_2 = dados_2['Ocorrências']
coluna_3 = dados_3['Ocorrências']
coluna_4 = dados_4['Ocorrências']
x = (2015,2017,2019,2021)
y = [sum(coluna_4),sum(coluna_3),sum(coluna_2),sum(coluna_1)]
plt.bar(x,y,width= 0.9, align='center',color='blue', edgecolor = 'red')
plt.title(u'Brasil: total de crimes registrados por ano(janeiro à setembro)')
plt.xlabel(u'Ano')
for i in range(len(x)):
    plt.text(x[i],y[i],y[i],ha = "center", va = "bottom")
plt.ylabel(u'Número de crimes')
plt.show()
