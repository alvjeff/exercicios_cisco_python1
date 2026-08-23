
print("TESTE 1")
print("")
def my_function(n):
    print("Eu obtive", n)
    n +=1
    print("Eu tenho", n)

var = 1
my_function(var)
print("Valor passado no parametro", var)

print("--------------------------------------------------------------------------------")
print("TESTE 2 - COM LISTA")
print()

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3", my_list_1)
    print("Print #4", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

print("--------------------------------------------------------------------------------")
print("TESTE 3 - MODIFICANDO A LISTA")
print()

def my_function(my_list_3):
    print("Print #1:", my_list_3)
    print("Print #2:", my_list_4)
    del my_list_3[0]
    print("Print #3:", my_list_3)
    print("Print #4:", my_list_4)


my_list_4 = [2, 3]
my_function(my_list_4)
print("Print #5:", my_list_4)