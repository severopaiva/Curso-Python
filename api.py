import pprint, json
import requests

numero = input("Digite o número do Salmo que você quer ler: ")
argumento = "https://www.abibliadigital.com.br/api/verses/nvi/sl/" + numero
requisicao = requests.get(argumento)
verso = requisicao.json()

# Saída formatada com pprint:
pprint.pprint(verso)
