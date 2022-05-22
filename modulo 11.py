# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:51:09 2020

@author: Paiva
"""
digitacao = input("Digite string numperico: ")
Listastring = list(digitacao)
Listanum = [3,6,7,8,9,3,2,4,5,7]
soma = 0
for i in range(len(Listastring)):
    soma = soma + Listanum [i] * int (Listastring [i])
mod11 = soma % 11
if mod11 > 9:
    mod11 = 0
print ("Módulo 11: ", int(mod11))

