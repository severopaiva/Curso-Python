# -*- coding: utf-8 -*-

# FUNÇÃO FATORIAL RECURSIVA

def fat (N):
   if N == 0: # Teste para caso de N=0 (zero)
      return 1
   else:
      return (N * fat (N-1)) #Reativação de fat

# PROGRAMA PRINCIPAL

N = int(input("Digite um número: "))

print("O fatorial de ", N, " é ", fat(N))
