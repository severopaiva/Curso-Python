# -*- coding: utf-8 -*-
# CONVERSAO SISTEMAS DE NUMERAÇÃO

def conv(n, base):
    conv_string = "0123456789ABCDEF"
    if n < base:
       return conv_string[n]
    else:
       return conv(int (n / base), base) + conv_string [n % base]
    
# PROGRAMA PRINCIPAL

print ("\nConverte Decimal para bases entre 2 e 16 \n")
        
N = int(input(" Digite um número: "))

B = int(input(" Digite uma base: "))

print("\n O número ", N, "na base ", B, " corresponde a: ", conv(N,B))



