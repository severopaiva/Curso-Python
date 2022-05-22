# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:17:43 2022

@author: Paiva
"""


import pandas as pd
from  IPython.display import display
venda = {'Data'  : ['15/07/2022', '20/07/2022'],
         'Valor' : [500, 200],
         'Produto': ['Feijão', 'Arroz'],
         'Quantidade' : [120, 150]
        }
vendas_df = pd.DataFrame(venda)
print (vendas_df)
print()
display(vendas_df)
print()
print(vendas_df.shape)
print()
print(vendas_df.describe())
print()
display(vendas_df.loc[1])
print()
display(vendas_df.loc[vendas_df['Produto'] == 'Feijão'])