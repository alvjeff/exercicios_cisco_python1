def happy_new_year(wishes = True):
    print("Três...")
    print("Dois...")
    print("Um...")
    if not wishes:
        print("nada")
        return
    
    print("Feliz ano novo!")

happy_new_year(False) 

def boring_function():
    return 123

x = boring_function()
print("a função aborrecimento retornou seu resultado. Isso é:", x)