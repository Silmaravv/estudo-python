import random

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


'''


tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


'''
game_img = [pedra, papel, tesoura]

user_choice = int(input("faça sua jogada: (0) Pedra, (1) Papel, (2) Tesoura! \n"))

computer_choice = random.randint(0,2)
print('computador')
print(game_img[computer_choice])

if user_choice >= 0 and user_choice <= 2:
    print(game_img[user_choice])


if user_choice >= 3:
    print('opção invalida, você perdeu')

if user_choice == 0 and computer_choice == 2:
    print('Você ganhou')

elif computer_choice == 0 and user_choice == 2:
    print('você perdeu!')

elif computer_choice >user_choice:
    print('Vitória do PC')

elif user_choice > computer_choice:
    print('Você ganhou')

elif computer_choice == user_choice:
    print('Empate!')

elif user_choice >=3 or user_choice < 0:
    print("Você perdeu")

else:
    print('Você digitou uma opção inválida')