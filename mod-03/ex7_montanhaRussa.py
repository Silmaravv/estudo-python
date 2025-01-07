# Os clientes de 45 a 55 anos possuem isenção do ingresso, ajuste o código:
print('Seja bem-vindo(a) ao serviço de bilheteria da montanha russa da TipsPark')
altura = int(input('Informe a a sua altura em cm'))
conta =0
if altura >= 120:
        idade = int(input('Qual a sua idade '))
        if idade <= 12:
                print('O valor a pagar é de R$05,00')
                conta = 5
        elif idade <=18:
                print('O valor a pagar é de R$12,00')
                conta = 12
        elif idade >=45 and idade <=55:
                print('entrada free')
                conta = 0
        
        else:
           conta = 24
           print('O valor a pagar é de R$24,00')
               

        photo = input('Deseja tirar foto? Sim (s), Não (n)')
               

        if photo == 's':
                #add +3 reais na conta
               conta +=3 #conta = conta + 3 é a mesma coisa

        print(f'Sua conta final é R${conta}')              
else:
        print('Pedimos desculpa, mas a venda do ingresso não é permitida. \nO requisito mínimo de altura para participar é de 120 cm ou maior. \nEsta regra é estabelecida para garantir a segurança de todos os participantes, agradeço a compreensão.')