# -*- coding: utf-8 -*-
#Cálculo Média Aluno

def entrada_dados_pessoais():
# Entrada de Dados Pessoais Aluno
    global nome,turma
    nome = input("Digite Nome Aluno: ")
    turma = input("Digite a Turma: ")

def entrada_notas():
# Entrada de Notas Aluno
    global n1,n2
    n1 = float(input("Digite Nota1: "))
    n2 = float(input("Digite Nota2: "))

def calcula_media(x1,x2):
# Cálculo Média (n1,n2):
    global media
    media = (x1 + x2) / 2

def exibe_resultados(nome,turma,media):
# Exibição do Resultado
    print ("O Resultado do aluno: ", nome, " - Turma: ", turma)
    print ("   Média: ", media, end = " ")
    if media >= 7:
        print ("Aprovado")
    else:
        print("Reprovado")


#Programa Principal
nome=""
turma=""
n1 = n2 = 0.00
media = 0.00
entrada_dados_pessoais()
entrada_notas()
calcula_media(n1,n2)
exibe_resultados(nome,turma,media)



