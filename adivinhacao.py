print("***************************")
print("Bem vindo ao jogo da adivinhacao")
print("***************************")

numero_secreto = "42"

chute_strg = input("Digite o numero secreto:")

print("Você digitou", chute_strg)

chute = int(chute_strg)

if (numero_secreto == chute_strg):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do Jogo!")