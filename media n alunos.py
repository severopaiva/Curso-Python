# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:51:09 2020

@author: Paiva
"""

n = int (input("Quantidade de alunos: "))
soma = 0
for i in range(1,n+1):
    nome = input("Nome Aluno: ")
    n1 = float (input("Nota1: "))
    n2 = float (input("Nota2: "))
    media = (n1 + n2) / 2
    print ("\n",nome," Notas: ", n1,n2, " Média: ", media)
    soma = soma + media
print ("\n Esta turma tem média geral: ", soma/n)
     
    
    
        
        
    
