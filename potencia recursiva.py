# -*- coding: utf-8 -*-

# FUNÇÃO POTÊNCIA RECURSIVA

def POT(BASE,EXPOENTE):
    if EXPOENTE < 0:
       return 1 / POT (BASE, EXPOENTE * (-1))
    elif EXPOENTE == 0:
       return 1
    else:
       return BASE * POT (BASE,EXPOENTE - 1)


# PROGRAMA PRINCIPAL

print ("\n Potência de forma Recusiva: \n")
N = int(input(" Digite um número: "))

E = int(input(" Digite um expoente: "))

print("\n A potência de ", N, " elevado a ",E, " é: ", POT(N,E))

