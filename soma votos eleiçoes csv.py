# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:53:28 2020

@author: Paiva
"""

import csv

arquivo = open('votacao eleicao 2012.csv')

linhas = csv.reader(arquivo)
soma =0 
for linha in linhas:
    print(linha)

print ("Total de Votos: ", soma)