# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:09:56 2020

@author: Paiva
"""

# Área de Inicialização
LIN=4
COL=2
MAT = [[0,0], [0,0], [0, 0],[0,0]]
Inicio = 0
SOMA = 0

# Processamento
for I  in range (Inicio, LIN):
    for J in range (Inicio, COL):
        MAT [I] [J] = int(input(" Digite item: "))
        SOMA = SOMA + MAT [I] [J]

# Apresentação de Resultados
print("A soma dos componentes vale: " ,SOMA)
print (MAT)
