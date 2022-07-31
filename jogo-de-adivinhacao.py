print("#########################")
print("###JOGO DE ADIVINHAÇÂO###")
print("#########################")

riddle = 10
attempts = 3
turn = 1


while(turn <= attempts):
    print(f"-Tentativa {turn} de {attempts}")
    kick = int(input("Digite um número: "))
    accurate = kick == riddle
    bigger = kick > riddle


    if(accurate):
        print("Parabéns! Você advinhou o número.\n")
        break
    else:
        if(bigger):
            print(f"Você errou. {kick} é maior que o número a ser adivinhado.\n")
        else:
            print(f"Você errou. {kick} é menor que o número a ser adivinhado.\n")

    turn = turn + 1

print("Fim de jogo.")
