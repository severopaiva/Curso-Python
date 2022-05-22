# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:28:44 2020

@author: Paiva
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