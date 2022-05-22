# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
def isint(numero):
    try:
        x = int(numero)
        return (True)
    except ValueError:
        return (False)
    
n1 = input ("Digite o 1o. número inteiro: ")
while not isint(n1):
    n1 = input ("Redigite um inteiro: ")

n2 = input ("Digite o 2o. número inteiro: ")
while not isint(n2):
    n2 = input ("Redigite um inteiro: ")

n3 = input ("Digite o 3o. número inteiro: ")
while not isint(n3):
    n3 = input ("Redigite um inteiro: ")

print ("Parabéns! Você digitou corretamente 3 inteiros: ",n1,", ", n2," e ", n3)

