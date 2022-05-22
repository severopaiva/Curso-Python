# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:49:36 2020

@author: Paiva
"""

from selenium import webdriver
import time
import traceback
import sqlite3

nome, celular, mensagem = '', '', ''

try:
    conection = sqlite3.connect('agenda.db')
    c = conection.cursor()
    '''
    c.execute("""create table if not exists agenda(
                         nome text,
                         telefone text,
                         mensagem text
                         )""")

    c.execute(
        "insert into agenda (nome, telefone, mensagem) values ('Aninha', '5583988159418', 'Estamos testando"
        " o envio de mensagens pelo Watsapp')")

    conection.commit()
    '''
    c.execute("select * from agenda")
    driver = webdriver.Edge(executable_path='C:\geckodriver\MicrosoftWebDriver.exe')
    #driver = webdriver.Chrome(executable_path='C:\geckodriver\chromedriver.exe')
    driver.get('http://web.whatsapp.com')
        
    aux = input ("Posso continuar?")
    time.sleep(5)

    for linha in c:
        nome = linha[0]
        celular = linha[1]
        mensagem = linha[2]
        print(nome)
        print(celular)
        print(mensagem)

        # nova_mensagem = driver.find_element_by_xpath('//div[@title = "Nova conversa"]')
        # nova_mensagem.click()
        try:
            caixa_de_pesquisa = driver.find_element_by_class_name('jN-F5')
            caixa_de_pesquisa.send_keys(nome)

            time.sleep(5)

            contato = driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome))
            contato.click()

            time.sleep(2)

            caixa_de_mensagem = driver.find_element_by_class_name('_2S1VP')
            caixa_de_mensagem.send_keys(mensagem)

            time.sleep(2)

            botao_enviar = driver.find_element_by_class_name('_2lkdt')
            botao_enviar.click()

            botao_limpar_pesquisa = driver.find_element_by_class_name('_3Burg')
            botao_limpar_pesquisa.click()

        except:
            print('Não há ninguém com o nome de ' + nome + ' na sua agenda')
            try:
                botao_limpar_pesquisa = driver.find_element_by_class_name('_3Burg')
                botao_limpar_pesquisa.click()
            except:
                pass

    c.close()

except:
    print(traceback.format_exc())
