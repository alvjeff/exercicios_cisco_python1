"""
Sua tarefa é escrever e testar uma função que usa três argumentos (um ano, um mês e um dia do mês) e retorna o dia correspondente do ano ou retorna None se algum dos argumentos for inválido.

Use as funções escritas e testadas anteriormente. Adicione seus próprios casos de teste ao código.


"""

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
    dias_ano_bissexto = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias_nao_bissexto = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year):
        return dias_ano_bissexto[month-1]
    else:
        return dias_nao_bissexto[month-1]

def day_of_year(year, month, day):
# Escreva seu código aqui.

    


print(day_of_year(2000, 12, 31))