print ("Calcula o MDC entre dois números pelo Método de Euclides")
n1 = 0
n2 = 0
while (n1 <= n2):
   print ("Digite dois números distintos, onde o primeiro é o maior e o segundo é o menor.")
   n1 = int(input("Digite o maior número: "))
   n2 = int(input("Digite o menor número: "))
maior = n1
menor = n2
resto = n1 % n2
while (resto != 0):
    n1 = n2
    n2 = resto
    resto = n1 % n2
print ("O MDC de ", maior, " e ", menor, "é: ",n2)

