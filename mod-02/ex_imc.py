# calcule o IMC do usúario
altura = float(input('digite sua altura'))
peso = float(input('digite seu peso: '))
imc = peso / (altura * altura)
novo_imc = int(imc)
print('seu IMC é: ' + str(novo_imc))