#desenvolva um programa para uma pizzaria em Python que calcule a conta do usuario automaticamente de acordo com suas opções:
print('🤩 Bem vindo(a) a Pizza Mania')
print('Sabor que vicia, escolha sem agonia.😋🤤')

tamanho = int(input(" \nDigite o número de acordo com a opção desejada: \n\n Opções de tamanho 🍕 Preço 💲 \n 1 - Pizza pequena 👉 R$15,00 \n 2 - Pizza Média   👉 R$20,00 \n 3 - Pizza Grande  👉 R$25,00"))

if tamanho == 1:
    preco = 15
    maisPepperoni = str(input("Deseja adicionar Pepperoni por +R$2,00? S/N"))
    if maisPepperoni == "S":
        preco += 2
    elif maisPepperoni == "N":
        pass
elif tamanho == 2:
    preco = 20

elif tamanho == 3:
    preco = 25
else:
    print("Opção inválida!")

if tamanho == 2 or tamanho ==3:
    maisPepperoni = str(input("Deseja adicionar Pepperoni por +R$3,00? S/N"))
    if maisPepperoni == "S":
        preco += 3
    elif maisPepperoni == "N":
        pass
queijoExtra = str(input("Deseja queijo extra por +R$1,00? S/N"))
if queijoExtra == "S":
        preco += 1
elif queijoExtra == "N":
    pass
print(f"O preço final da sua pizza é R${preco}")





    



