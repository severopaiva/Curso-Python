# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:09:56 2020

@author: Paiva
"""

# Inicialização e Dados Iniciais
print ("Informe as dimensões da matriz: ")
LIN = int(input("Quantas linhas : "))
COL = int(input("Quantas colunas: "))
MAT = [[0,0],[0,0],[0,0],[0,0]]
#MAT = [[0,0]] * (LIN)  
print (MAT)

# Processamento
Inicio = 0
SOMA = 0
for I  in range (Inicio, LIN):
    for J in range (Inicio, COL):
        MAT [I] [J] = int(input(" Digite item: "))
        print (MAT)
        SOMA = SOMA + MAT [I] [J]

# Exibição de Resultado
print("A soma dos componentes vale: " ,SOMA)
print (MAT)
