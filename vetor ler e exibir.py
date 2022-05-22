# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:12:39 2020

@author: Paiva
"""

# Declarações e Inicialização variáveis #
TAM = int(input("Qual o tamanho do vetor: "))
V = [0] * TAM
Inicio=0
Fim=TAM
  
# Entrada de Dados #
for I  in range(Inicio,Fim): 
    V[I]=int(input("Digite o componente: "))
      
# Exibição dos dados digitados #
print ()
for I  in range(Inicio,len(V)): 
    print ("O componente de ordem ",I, " vale: ",V[I])
