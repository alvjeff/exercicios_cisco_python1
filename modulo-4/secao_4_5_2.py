"""
Sabemos pela escola que a soma de dois lados arbitrários precisa ser maior que o terceiro lado.

Não será um desafio difícil. A função terá três parâmetros - um para cada lado.

Ele retornará True se os lados puderem construir um triângulo, e False caso contrário. Nesse caso, is_a_triangle é um bom nome para essa função.
"""

def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

##versão refatorada / mais compacta
def is_a_triangle2(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle2(1, 1, 1))
print(is_a_triangle2(1, 1, 3))


## triangulo e o teorema de pitagoras ##
def is_a_triangle3(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Digite o primeiro lado\'s cumprimento: "))
b = float(input("Entre no segundo lado\'s cumprimento: "))
c = float(input("Entre no terceiro lado\'s cumprimento: "))

if is_a_triangle3(a, b, c):
    print("Sim, pode ser um triângulo.")
else:
    print("Não, não pode ser um triângulo.")


def is_a_right_triangle(a, b, c):
    if not is_a_triangle3(a, b, c):
        return False
    if c > a and c > b:
        return c**2 == a**2 + b**2 
    if a > b and a > c:
        return a**2 == b**2 + c**2

print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))


## encontrando area do triangulo pela formula de heron ##
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_trinangle(a, b, c):
    if not is_a_triangle3(a, b, c):
        return None
    return heron(a, b, c)

print(area_of_trinangle(1., 1., 2. ** .5))