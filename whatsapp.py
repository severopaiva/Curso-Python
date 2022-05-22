# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:50:48 2020

@author: Paiva
"""


from selenium import webdriver
import time
import traceback
#import sqlite3

nome, celular, mensagem = '', '', ''

#try:
#    conection = sqlite3.connect('agenda.db')
#    c = conection.cursor()
#    '''
#    c.execute("""create table if not exists agenda(
#                         nome text,
#                         telefone text,
#                         mensagem text
#                         )""")
#
#    c.execute(
#        "insert into agenda (nome, telefone, mensagem) values ('VANILTON', '0000000000000', 'Estamos testando"
#        " o envio de mensagens pelo Watsapp')")
#
#    conection.commit()
#    '''
#    c.execute("select * from agenda")

agenda = ['5583988029401','5583988159418']
driver = webdriver.Chrome(executable_path='C:\geckodriver\chromedriver.exe')
driver.get('http://web.whatsapp.com')
time.sleep(5)
mensagem = "teste de MSG Zap"

for i in agenda:
#   nome = linha[0]
    celular = agenda [i]
    
    print(celular)
    print(mensagem)

    try:
       
       caixa_de_mensagem = driver.find_element_by_class_name('_2S1VP')
       caixa_de_mensagem.send_keys(mensagem)

       time.sleep(2)

       botao_enviar = driver.find_element_by_class_name('_2lkdt')
       botao_enviar.click()

       botao_limpar_pesquisa = driver.find_element_by_class_name('_3Burg')
       botao_limpar_pesquisa.click()

    except:
       print('Erro de envio')
            