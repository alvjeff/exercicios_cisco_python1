#while True:
#    print("Estou preso dentro de um loop.")

largest_number = -999999

number = int(input("Digite um número ou digite -1 para sair: "))

#se o numero nao for igual a -1, continue
while number != -1:
    if number > largest_number:
        largest_number = number

    number = int(input("Digite um número ou digite -1 para parar: "))

print("O maior número é: ", largest_number)