import random


userPlay = int(input("Você escolhe, 0(pedra) 5(papel) 2(tesoura): "))

pcPlay = random.choice([0, 5, 2])

print(f"O seu oponente escolheu: {pcPlay}")

if userPlay == pcPlay:
    print("Empate!")
elif (userPlay == 0 and pcPlay == 2) or (userPlay == 5 and pcPlay == 0) or (userPlay == 2 and pcPlay == 5):
    print("Você ganhou!")
else:
    print("Você perdeu.")
