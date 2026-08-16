"""
Um número natural é primo se for maior que 1 e não tiver divisores diferentes de 1 e ele próprio.

Complicado? Não mesmo. Por exemplo, 8 não é um número primo, pois você pode dividi-lo por 2 e 4 (não podemos usar divisores iguais a 1 e 8, pois a definição proíbe isso).

Por outro lado, 7 é um número primo, pois não podemos encontrar divisores legais para ele.

Sua tarefa é escrever uma função verificando se um número é primo ou não.
"""

def is_prime(num):
 #
 # Escreva seu código aqui.
 #

for i in range(1, 20):
    if is_prime(i + 1):
    print(i + 1, end=" ")
print()