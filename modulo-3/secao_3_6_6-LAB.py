my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9, 9]
var = my_list[0]

for i in range(my_list):
    if i == 0:
        continue
    for j in range(my_list[1:]):
        if var == my_list[j]:
            del my_list[i]


print("A lista com os elementos exclusivos aqui")
print(my_list)