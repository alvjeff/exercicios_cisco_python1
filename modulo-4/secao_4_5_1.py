## Funções de Exemplo: avaliando o IMC ##

#exemplo1
"""
def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))
"""

#exemplo2 - Avaliação do IMC e conversão de unidades imperiais em unidades métricas
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(bmi(352.5, 1.65))
print(bmi(52.5, 1.65))
print(bmi(103, 1.72))


#converter unidades imperiais em unidades métricas
def lb_to_kg(lb):
    return lb * 0.45359237

print(lb_to_kg(1))


#converter pés e polegadas
#def ft_and_inch_to_m(ft, inch):
def ft_and_inch_to_m(ft, inch = 0): #inch por padrao igual a zero
    return ft * 0.3048 + inch * 0.0254

print(ft_and_inch_to_m(1, 1))
print(ft_and_inch_to_m(6, 0))

#mais um teste
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7))) 

