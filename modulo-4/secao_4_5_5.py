### Recursão ###

#refatorando fibonacci
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    return fib(n - 1) + fib(n - 2)

print("##Fibonacci##")
for n in range(1, 10):
    print(n, "->", fib(n))


# refatorando fatorial
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    return n * factorial_function(n - 1)

print("###fatorial###")
for n in range (1, 6): 
    print(n, factorial_function(n))

