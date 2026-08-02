c0 = int(input("digite um número diferente de 0: "))
etapa = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = (3 * c0) + 1
    print(c0)
    etapa += 1

print("Etapas = " , etapa)

#exercicio realizado com sucesso!!!