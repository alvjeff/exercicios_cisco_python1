""" um progrema lê uma sequencia de números e conta quantos são ímpares e termina quando zero é digitado"""

odd_numbers = 0
even_numbers = 0

#ler número
number = int(input("Digite um número ou digite 0 para parar: "))

while number != 0:
    #verifica se é par
    if number % 2 == 1:
        odd_numbers +=1
    else:
        even_numbers += 1

    #ler o número seguinte
    number = int(input("Digite um número ou digite 0 para parar: "))

#imprimir resultados
print("Números ímpares contam: ", odd_numbers)
print("Números pares contam: ", even_numbers)