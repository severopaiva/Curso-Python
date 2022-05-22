# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 06:25:23 2021

@author: Paiva
"""

# Tamanho de uma cadeia sem usar função predefinida e recursivamente

def comp (cadeia):
    if not cadeia:
        return 0
    else:
        return 1 + comp (cadeia [1:])


print ("Calcula o comprimento de uma cadeia qualquer")

cad = input ("Digite uma cadeia: ")

print ("\nA cadeia ", cad, "tem ", comp(cad), " caracteres")

        
