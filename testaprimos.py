# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:52:35 2020

@author: Paiva
"""


limite = int(input("Qual o valor limite? "))
lista_primos = []
for n in range(2,limite+1):
    primo = True
    for x in range(2,n):
        if (n % x)==0:
            print (n, "=", x, "*", n/x)
            primo = False
    if primo:
       print (n, "é primo")
       lista_primos.append(n)
print ("\nNo intervalo solicitado temos ",len(lista_primos), " números primos.")
print (lista_primos)