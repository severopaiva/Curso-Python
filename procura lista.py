# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 07:44:05 2020

@author: Paiva
"""

lista = ["Paris", "Londres", "Brasilia", "Moscou"]
pos = 0
achou = False
item = input ("Qual a capital a procurar: ")
while pos < len(lista) and not achou:
    if lista [pos] == item:
        achou = True
    else:
        pos = pos + 1
if achou:
    print (item, " Elemento encontrado na posição: ", pos)
else:
    print (item, " não encontrado")