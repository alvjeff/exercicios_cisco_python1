##exemplo de codigo com if-else##

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("O maior número é: ", larger_number)


##Exemplo3 - comparar 3 numeros
number1 = int(input("Insira o numero 1: "))
number2 = int(input("Insira o numero 2: "))
number3 = int(input("Insira o numero 3: "))

larger_number = number1

if number2 > larger_number:
    larger_number = number2
    if number3 > larger_number:
        larger_number = number3
elif number3 > larger_number:
    larger_number = number3

print("O maior número é: ", larger_number)

