secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

tentativa = int(input("numero: "))

while tentativa != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    tentativa = int(input("numero: "))

print("Muito bem, trouxa! Você está livre agora.")
