registros = int(input())
#dicionario
tempos_de_resposta = {}
esperando_resposta = {}
ultimo_tempo = 0
for _ in range(registros):
    entrada = input().split()
    tipo = entrada[0]
    #conversão
    x = int(entrada[1])

    if tipo == 'T':
        ultimo_tempo = ultimo_tempo + x - 1
    else:
        ultimo_tempo +=1
    if tipo == 'R':
        if x not in tempos_de_resposta:
            tempos_de_resposta[x] = 0
        esperando_resposta[x] = ultimo_tempo
    elif tipo == 'E':
        if x in esperando_resposta:
            if x not in tempos_de_resposta:
                tempos_de_resposta[x] = 0
            tempos_de_resposta[x] += (ultimo_tempo - esperando_resposta[x])
            del esperando_resposta[x]

for amigo in esperando_resposta:
    tempos_de_resposta[amigo] = -1

for amigo in sorted(tempos_de_resposta.keys()):
    print(f'{amigo} {tempos_de_resposta[amigo]}')
