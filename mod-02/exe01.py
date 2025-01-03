"""
Como eu resolvi
#escreva um programa que some dois números de dois dígitos

print('realize somas de números')
n1 = input('digite o 1º número')
n2 = input('digite o 2º número')
# em python o que é inserido no input é tratado como String, para fazer a soma dos números é necessário converter antes
n1 = int(n1)
n2 = int(n2)

soma = n1 + n2
print('A soma dos números é igual a '+ str(soma)) #para mostrar o resultado, converti soma para String"""

'''#escreva um programa que faça a extração de dois números e some

numero = input('Digite um valor com 2 digitos: ')

n1 = int(numero[0])
n2 = int(numero[1])

soma = n1 + n2

print(soma)'''

#complementando o código de forma que o usuário não digite além do que o solicitado

while True:
    numero = input('digite um valor com 2 dígitos: ')

    if len(numero)== 2 and numero.isdigit():
        try:
            n1 = int(numero[0])
            n2 = int(numero[1])
            soma = n1+n2
            print(f'A soma dos dois dígitos é {soma}')
            break
        except ValueError:
            print('algo deu errado')
    else:
        print('Entrada inválida. Você realmente digitou 2 números?')

