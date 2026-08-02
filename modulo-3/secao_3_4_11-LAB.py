# etapa 1
beatles = []
print("Etapa 1:", beatles)

# etapa 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)

# etapa 3
for i in range(2):
    x = input("Insira proximo integrante: ")
    beatles.append(x)
print("Etapa 3:", beatles)


# etapa 4
del beatles[-1]
del beatles[-1]
print("Etapa 4:", beatles)

# passo 5
beatles.insert(0,"Ringo Starr")
print("Etapa 5:", beatles)



# testando o tamanho da lista

print("o fabuloso", len(beatles))

