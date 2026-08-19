### CONVERTENDO CONSUMO DE COMBUSTÍVEL ###

"""
O consumo de combustível de um carro pode ser expresso de várias maneiras diferentes. Por exemplo, na Europa, ele é mostrado como a quantidade de combustível consumida por 100 quilômetros.

Nos EUA, é mostrado como o número de quilômetros percorridos por um carro usando um litro de combustível.

Sua tarefa é escrever um par de funções convertendo l/100 km em mpg e vice-versa.

As funções:

    - são nomeados liters_100km_to_miles_gallon e miles_gallon_to_liters_100km respectivamente;
    - use um argumento (o valor correspondente aos nomes)

Preencha o código no editor e execute-o para verificar se a sua saída é igual à nossa.
"""

def liters_100km_to_miles_gallon(liters):
 # aqui o meu codigo
 # fiz a conversão de L para galao e km para milha
    resultado = (100/1.609344) / (liters / 3.785411784)
    return resultado  


def miles_gallon_to_liters_100km(miles):
 ## aqui o meu codigo
    resultado = (3.78) * 100 /  (1.609 * miles) 
    return resultado

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

"""
obs: cometi um erro crasso de por a vírgula no lugar do ponto em variavel do tipo float.
"""