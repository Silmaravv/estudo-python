#Sorteio de duplas: Faça um sorteio automatizado para os participantes se dividir em duplas.
import random

num_participantes = int(input("Digite o número de participantes: "))

if num_participantes % 2 != 0:
    print("Número de participantes ímpar. Adicione mais um participante ou retire um para formar duplas.")
else:
    nomes = []

    for i in range(num_participantes):
        nome = input(f"Digite o nome do participante {i+1}: ")
        nomes.append(nome)

    random.shuffle(nomes)

    print("\nDuplas formadas:")
    for i in range(0, num_participantes, 2): 
        dupla = (nomes[i], nomes[i + 1])
        print(f"Dupla {i//2 + 1}: {dupla[0]} e {dupla[1]}")

