"""
Sua tarefa é escrever e testar uma função que usa um argumento (um ano) e retorna True se o ano for um ano bissexto ou False caso contrário.

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
            

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("ok")
    else:
        print("Fracassou")