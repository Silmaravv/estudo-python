import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '+','[', ']', '{', '}','/', '?']

qtdeLetras = int(input('Qual a quantidade de letras que deseja para sua senha?:\n'))
qtdeNumeros = int(input('Qual a quantidade de numeros que deseja para sua senha?:\n'))
qtdeSimbolos = int(input('Qual a quantidade de simbolos que deseja para sua senha?:\n'))

senha1 = ''

#forma fácil de gerar senha para treinar
for char in range (0, qtdeLetras):
    senha1 += random.choice(letras)


for char in range (0, qtdeSimbolos):
    senha1 += random.choice(simbolos)

for char in range (0, qtdeNumeros):
    senha1 += random.choice(numeros)

print('sua senha seguindo a sequência de quantidade de letras símbolos e números é: '+senha1)


# forma normal

senha_list = []

for char in range (0, qtdeLetras):
    senha_list += random.choice(letras)


for char in range (0, qtdeSimbolos):
    senha_list += random.choice(simbolos)

for char in range (0, qtdeNumeros):
    senha_list += random.choice(numeros)


random.shuffle(senha_list)


senha2 = ''
for char in senha_list:
    senha2 += char

print(f'sua senha com caracteres aleatorios é: {senha2}')



