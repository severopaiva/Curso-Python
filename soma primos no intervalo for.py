# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:28:44 2020

@author: Paiva
"""

primos = []
lim = int(input('apresente um número limite: '))
soma = 0
num = 2
for i in range(2, lim+1):
    retorno = True
    for j in range(2,i):
        if i % j == 0:
           retorno = False
           break
    if retorno:
       primos.append(i)
       soma = soma + i

print ("Os primos no intervalos são: ", primos)
print(f'a soma é {soma}')
