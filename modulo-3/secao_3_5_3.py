"""
Este exercicio serve para ordenar elementos numa lista de forma crescente, so que interativo com o usuario
"""

my_list = [] 
swapped = True
num = int(input("Quantos elementos deseja embaralhar?"))

for i in range(num):
    val = float(input("Entre com a lista de elementos:"))
    my_list.append(val)

while swapped:
    swapped = False #nenhuma troca ate agora
    for i in range(len(my_list) -1): #precisamos de (5 - 1) comparações
        if my_list[i] > my_list[i + 1]: # comparar elementos adjacentes
            swapped = True # uma troca ocorreu
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # aqui temos que trocar os elementos
 
print("\nSorted:")
print(my_list)