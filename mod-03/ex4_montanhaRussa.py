print('Seja bem-vindo(a) ao serviço de bilheteria da montanha russa da TipsPark')
altura = int(input('Informe a a sua altura em cm'))
if altura >= 120:
        idade = int(input('Qual a sua idade '))
        if idade <= 12:
                print('O valor a pagar é de R$05,00')
        elif idade <=18:
                print('O valor a pagar é de R$12,00')
        else:
                print('O valor a pagar é de R$24,00')
else:
        print('Pedimos desculpa, mas a venda do ingresso não é permitida. \nO requisito mínimo de altura para participar é de 120 cm ou maior. \nEsta regra é estabelecida para garantir a segurança de todos os participantes, agradeço a compreensão.')