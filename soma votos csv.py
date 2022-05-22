# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:53:28 2020

@author: Paiva
"""

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

soma =0
nomescompletos=[]
nomeurna = []
votos2012 = []
votos2008 = []
votos2016 = []
numero2008 = []
numero2012 = []
numero2016 = []
situacao2008 = []
situacao2012 = []
situacao2016 = []

dicionario = {
'Nome': nomescompletos,
'Nomeurna': nomeurna,
'Votos2008': votos2008, 
'Votos2012': votos2012,
'Votos2016': votos2016,
'Numero2008': numero2008,
'Numero2012': numero2012,
'Numero2016': numero2016,
'Situacao2008': situacao2008,
'Situacao2012': situacao2012,
'Situacao2016': situacao2016
}



def pesquisa():
    procura = input("Qual nome pesquisar: ")
    while procura != "fim":
       try:
          ind = nomeurna.index(procura.upper())
          print ("            Votos   Votos   Votos    Votação") 
          print ("Candidato   2008    2012    2016      Média")
          print (nomeurna [ind],"        ",votos2008[ind],votos2012[ind],votos2016[ind])
       except:
          print("Não encontrado!")
       procura = input("Qual nome pesquisar: ")
    return

def pesquisanome (nome):
    retorno = False
    for i in nomeurna:
        if nome.upper() == i:
           #print ("Achei! Nome procurado: ",nome,"* Nome Urna: *",i,"*")
           retorno = True
           break
        else:
            #print ("Nome procurado: ",nome,"* Nome Urna: *",i,"*")
            aux = input("Enter")
    return retorno
 
def relatorio():
    print ("                       Votos   Votos     Votos    Votação") 
    print ("   CANDIDATO           2008    2012      2016     Média")
    for i in range(len(nomescompletos)):
        cand = nomeurna [i]
        media = int((votos2008[i]+votos2012[i] + votos2016[i])/3)
        print ("{0:.<20}".format(cand[0:19])," ",'{0:4}'.format(votos2008[i]),"  ",'{0:4}'.format(votos2012[i]),"    ",'{0:4}'.format(votos2016[i]),"    ",'{0:4}'.format(media))
        if (i % 10 == 0) and (i >= 10):
           aux = input("Enter continuar")
           print ("                       Votos   Votos     Votos    Votação") 
           print ("   CANDIDATO           2008    2012      2016     Média")


def cria_pdf():
    # Aqui vem o código de criação do dicionário `dic`

    c = canvas.Canvas("relatório.pdf")

    # Move a origem do cursor para a parte superior esquerda
    c.translate(inch,inch)

    # Inicia um objeto texto limitando a área para que linhas 
    # muito grandes, não ultrapassem a margem.
    textobject = c.beginText(0, 650)
    textobject.setFont("Helvetica-Oblique", 14)

    # Percorrendo o dicionário definido anteriormente
    for key, value in dicionario():
        textobject.textLine(key + ' : ' + value)

    c.drawText(textobject)

    c.showPage()
    c.save()

    os.system('arquivo.pdf')
    
    return


arquivo = open('votacao eleicao 2012.csv')
candidatos = []
#linhas = csv.reader(arquivo)


linha = arquivo.readline()
linha = arquivo.readline()
linha = arquivo.readline()
linha = arquivo.readline()
linha = arquivo.readline()
linha = arquivo.readline()
linha = arquivo.readline()
linha = arquivo.readline()
linha = arquivo.readline()

while linha:
    candidato = str(linha).split(";")
    if int(candidato[8]) > 0:
       nomescompletos.append(candidato[5].upper())
       nomeurna.append(candidato[6].upper())
       votos2012.append(int(candidato[8]))
       votacao = int (candidato[8])
       nome = candidato [6]
       
       votos2008.append(0)
       votos2016.append(0)
       numero2008.append("")
       numero2012.append(candidato[4])
       situacao2012.append(candidato[9])
       numero2016.append("")
       situacao2008.append("")
       situacao2016.append("")
    linha = arquivo.readline()
#arquivo.close()


#df = pd.DataFrame(dicionario, columns=['Nome','Nomeurna','Votos2008','Votos2012', 'Votos2016','Numero2008','Situacao2008','Situacao2012','Situacao2016'])

#Média 
#print("Média: ",df.mean())

#Mediana dos valores
#print ("Mediana: ",df.median())

#print (df.describe())



print (df.head())
print (df.tail())

print ("Pesquisa antes 2008")
#pesquisa()


arquivo1 = open('votacao eleicao 2008.csv')
candidatos = []


linha = arquivo1.readline()
linha = arquivo1.readline()
linha = arquivo1.readline()
linha = arquivo1.readline()
linha = arquivo1.readline()
linha = arquivo1.readline()
linha = arquivo1.readline()
linha = arquivo1.readline()
while linha:
    candidato = str(linha).split(";")
    votacao = int (candidato[8])
    nome = candidato [6].upper()
    
    try: 
       ind = nomescompletos.index(candidato[5].upper())
    except:
       ind = 0  
    if ind > 0:
       votos2008 [ind] = votacao
       numero2008.append(candidato[4])
       situacao2012.append(candidato[9].upper())
    else:
       nomescompletos.append(candidato[5].upper())
       nomeurna.append(candidato[6].upper())
       numero2008.append(candidato[4])
       situacao2008.append(candidato[9].upper())
       votos2008.append(votacao)
       
       votos2012.append(0)
       situacao2012.append("")
       numero2012.append("")
       
       votos2016.append(0)
       numero2016.append("")
       situacao2016.append("")
       
    linha = arquivo1.readline()
#arquivo1.close()

print ("Pesquisa antes 2016")
#pesquisa()

arquivo2 = open('resultado eleicao 2016.csv')
candidatos = []


linha = arquivo2.readline()
linha = arquivo2.readline()
linha = arquivo2.readline()
linha = arquivo2.readline()
linha = arquivo2.readline()
linha = arquivo2.readline()

while linha:
    candidato = str(linha).split(";")       
    votacao = int (candidato[10])
    
    try: 
       ind = nomescompletos.index(candidato[4].upper())
    except:
       ind = 0  
    #if candidato[5].upper() == "LEO BEZERRA":
    #    print ("LEO", "Ind:",ind,candidato)
    #    aux = input("Enter")
    if ind > 0:
       votos2016 [ind] = votacao
       numero2016 [ind] = candidato[3]
       situacao2016 [ind] = candidato [9]
    else:    
       nomescompletos.append(candidato[4].upper())
       nomeurna.append(candidato[5].upper())
       numero2016.append(candidato[3])
       situacao2016.append(candidato[9].upper())
       votos2016.append(votacao)
       
       votos2012.append(0)
       situacao2012.append("")
       numero2012.append("")
  
       votos2008.append(0)
       situacao2008.append("")
       numero2008.append("")

    linha = arquivo2.readline()

pesquisa()

print ("Relatório Final")
relatorio()

cria_pdf()

arquivo.close()
arquivo1.close()
arquivo2.close()
#for i in df:
#    print (i[0], i[1]) #,df['Votos'])

 #print (df.sort_values(by="Nomeurna"))
