print("#########################")
print("###JOGO DE ADIVINHAÇÂO###")
print("#########################")

number = 10
attempts = 3

kick = int(input("Digite um número: "))

if(kick == number):
    print("Parabéns! Você advinhou o número.")
else:
    print(f"Você errou, o número era {number} .Tente novamente.")
