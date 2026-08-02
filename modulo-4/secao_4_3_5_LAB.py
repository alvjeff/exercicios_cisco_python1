"""
Sua tarefa é escrever e testar uma função que usa dois argumentos (um ano e um mês) e retorna o número de dias para o determinado par de ano-mês (embora apenas fevereiro seja sensível ao valor do year, sua função deve ser universal).

**Como resolvi**
    - tive que fazer a funçao days_in_month() que faz o teste e dá o retorno se o ano é bissexto ou não;
    - No if desta função usa a outra função para o teste.

    OBS: preciso entender melhor como já foi feito a parte pronta
"""

def is_year_leap(year):
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
            else:
                return False

def days_in_month(year, month):
    dias_ano_bissexto = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias_nao_bissexto = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        return dias_ano_bissexto[month-1]
    else:
        return dias_nao_bissexto[month-1]

#parte que veio pronta no desafio
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")


"""
*** Excelente exercio e preciso reve-lo 

"""