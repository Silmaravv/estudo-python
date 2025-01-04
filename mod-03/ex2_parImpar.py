# esse progra tem objetivo de identificar se o número inteiro é par ou impa

try:
    num = int(input("Informe o numero inteiro"))

    if num % 2 == 0:
        print(f"O numero {num} é par")
    else:
        print(f"o numero {num} é impar")
except ValueError:  
    print("informe um número inteiro válido.")