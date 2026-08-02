###lab###

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

user_number = int(input("Digite o número secreto sua besta: "))

while user_number != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    user_number = int(input("Digite o número secreto sua besta: "))

print("Muito bem, trouxa! Você está livre agora!")