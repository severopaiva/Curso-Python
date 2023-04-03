import itertools

#Permutações que podem ser Geradas com seis carcateres:  151200

caracteres = []
qtd = int(input("Quantos caracteres para usar na geração: "))
for i in range(qtd):
    carac = input ("Caracter: ")
    caracteres.append(carac)
    
arq = open("senhas.dat","w")
comb = 0

print ("\nCaracteres para gerar senhas: \n", caracteres)

for subset in itertools.permutations(caracteres,qtd):
                linha = list(subset)
                n = ''.join([d for d in linha])
                n = n + "\n"
                print (n)
                comb = comb + 1
                arq.write(n)
arq.close()
print ("\nSenhas Geradas: ", comb)
