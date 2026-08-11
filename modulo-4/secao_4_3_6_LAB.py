"""
Sua tarefa é escrever e testar uma função que usa três argumentos (um ano, um mês e um dia do mês) e retorna o dia correspondente do ano ou retorna None se algum dos argumentos for inválido.

Use as funções escritas e testadas anteriormente. Adicione seus próprios casos de teste ao código.


"""
dias_ano_bissexto = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dias_nao_bissexto = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_year_leap(year):
# Seu código do LAB anterior.
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
 # Seu código do Lab anterior.
    

    if is_year_leap(year):
        return dias_ano_bissexto[month-1]
    else:
        return dias_nao_bissexto[month-1]

def day_of_year(year, month, day):
# Escreva seu código aqui.
#----------------------------------
# - criei uma variável chamada dia_no_ano para por meio de um loop armazenar os meses anteriores ao mês do dia da entrada no parâmetro
# - usei um for in para percorrer do índice 0 até o índice do mẽs anterior o da entrada
# - no fim, soma-se aos dias do meses anteriores ao day da entrada no parâmetro
# - ex: dia 5 de março de 2000 (ano bissexto), percorre o índice 0, janeiro com 31 dias, soma-se a 29 dias (de fevereiro, ano bissexto) e por fim, soma-se a 5 dias, totalizando 65.
# - o código usa métodos anteriores que faz o filtro se o ano é bissexto ou não. 
#----------------------------------


    dia_no_ano = 0
    for i in range(0, month-1):
        dia_no_ano += days_in_month(year, i+1)
    dia_no_ano += day

    return dia_no_ano


print(day_of_year(2000, 12, 31))
print(day_of_year(2000, 3, 5))
print(day_of_year(2026, 5, 18))