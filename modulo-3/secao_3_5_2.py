"""
Este exercicio serve para ordenar elementos numa lista de forma crescente
"""

my_list = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True

while swapped:
    swapped = False #nenhuma troca ate agora
    for i in range(len(my_list) -1): #precisamos de (5 - 1) comparações
        if my_list[i] > my_list[i + 1]: # comparar elementos adjacentes
            swapped = True # uma troca ocorreu
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] # aqui temos que trocar os elementos
 
print(my_list)