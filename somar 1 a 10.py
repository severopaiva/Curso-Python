# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:51:09 2020

@author: Paiva
"""

soma = 0 #Somatório
print ("Soma do números inteiros de 1 a um valor qualquer \n")
n = int(input("Último número a somar: "))

i = 1
while (i <= n):
    soma = soma + i
    print ("Valor de i: ",i, " Valor de soma: ", soma)
    i = i + 1
print ("\n Fim de programa")   
