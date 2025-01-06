altura = float(input('digite sua altura'))
peso = float(input('digite seu peso: '))
imc = peso / (altura * altura)
novo_imc = float(imc)
print('seu IMC é: ' + str(novo_imc))

if novo_imc >= 25:
    print('Acima do peso')
  
elif novo_imc >=18.5:
    print('Peso Normal')
       
else:
    print('abaixo do peso')