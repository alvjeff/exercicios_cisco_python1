#verificando escopo exemplo1
"""
def scope_test():
    x = 123

scope_test()
print(x)  # vai retornar NameError: name 'x' is not defined
"""

# EXEMPLO 2 #
def my_function():
    print("Eu conheço aquela variavel?", var)

var = 1
my_function()
print(var) #var foi enxergado dentro da funçao e o valor ofi mantido


#EXEMPLO 3 #
def my_function():
    var = 2
    print("Eu conheço aquela variável?", var)
 
 
var = 1
my_function()
print(var)
  
# é de se observar que o valor de var foi modificado dentro do escopo da funçao, por isso a divergencia nos resultados