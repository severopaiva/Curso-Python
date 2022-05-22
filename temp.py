# -*- coding: utf-8 -*-

#Cálculo Média Aluno

# Entrada de Dados Pessoais Aluno
nome = input("Digite Nome Aluno: ")
turma = input("Digite a Turma: ")

# Entrada de Notas Aluno
n1 = float(input("Digite Nota1: "))
n2 = float(input("Digite Nota2: "))

# Cálculo Média
media = (n1 + n2) / 2

# Exibição do Resultado
print()
print ("O Resultado do aluno: ", nome, " - Turma: ", turma)
print
print ("Média: ", media, end=" ")
if media >= 7:
    print ("Aprovado")
else:
    print("Reprovado")   