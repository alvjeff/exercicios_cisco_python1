"""def bmi(weight, height):
    return weight / height **2


print(bmi(52.5, 1.65))
"""

from tkinter import W


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
        weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(bmi(352.5, 1.65))
print(bmi(52.5, 1.65))

# obs1: lembrando que essa "\" permite escrever o restante do codigo de uma linha em outra linha facilitando a legibilidade


##convertendo unidades imperiais em unidades métricas##
#1 lb = 0.45359237 kg.
def lb_to_kg(lb):
    return lb * 0.45359237

print(lb_to_kg(1))


##convertendo pés em polegadas
#pés e polegadas: 1 pé = 0.3048 m, e 1 in = 2.54 cm = 0.0254 m
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254