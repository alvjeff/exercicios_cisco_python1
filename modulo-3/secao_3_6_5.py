####alguns programas com listas####

#encontrando o maior elemento
my_list = [17, 3, 11, 5, 15, 23]
largest = my_list[0]
indice = 0

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
        indice = i

print(indice, largest)


#encontrar um elemento
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")