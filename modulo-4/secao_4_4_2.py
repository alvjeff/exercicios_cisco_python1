## estender o escopo de uma variável de uma forma que inclua o corpo da função (mesmo se você quiser não apenas ler os valores, mas também modificá-los).

def my_function():
    global var
    var = 2
    print("Eu conheço aquela variável?", var)


var = 1
my_function()
print(var)

#obs pessoal: por meio a palavra reservada "global" é possível, além de ser, modificar dentro de uma função variáveis declaradas fora dela.