# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:28:44 2020

@author: Paiva
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Criando um dicionário onde cada chave será uma coluna do DataFrame >>> 
data = {'País': ['Bélgica', 'Índia', 'Brasil'],
'Capital': ['Bruxelas', 'Nova Delhi', 'Brasília'],
'População': [123465, 456789, 987654]
}

#Criando o DataFrame
#df = pd.DataFrame(data, columns=['País','Capital','População'])

#df.describe()

#xlsx = pd.ExcelFile("jampaEleitorado.xlsx")
#df = pd.read_excel(xlsx) #, 'Planilha 1')

df = pd.read_csv('jampaEleitorado.csv',encoding='ISO-8859-1')

#print (df.describe())

#print (df.median())

#print (xlsx)
#aux = input("Enter")

#df.describe()
#df.columns
#df["Eleitorado"].plot.hist()
#plt.plot(df.Bairro,df.Eleitorado)

#df.to_csv('paise.csv')

bairro = []
eleitores = []

#df.index()

print (df.head())

print (df.tail())


#ind = 0
#for i in range(0,len(df)):
#    print (df.loc[i,['Bairro','Secoes','Eleitorado']])


#minimo = int (input("Eleitorado Mínimo: "))

#print (df.query("Eleitorado > minimo"))

print (df[df['Area'] == "Q2"])
df["Area"].value_counts().plot.barh()
df["bairro"].value_counts().plot.barh(title="Número de apartamentos")

"""
def ehprimo(num):
    retorno = True
    for j in range(2,num):
        if num % j == 0:
           retorno = False
           break
    return retorno

primos = []
lim = int(input('apresente um número limite: '))
soma = 0
for i in range(2, lim+1):
    if ehprimo(i):
       primos.append(i)
       soma = soma + i

print ("Os primos no intervalos são: ", primos)
print(f'A soma é {soma}')
"""