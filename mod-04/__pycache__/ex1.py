#monte uma lista e depois, selecione apenas um item da lista usando array


frutas = ['banana', 'uva', 'banana']

print(frutas)
print(frutas[1])

print()

estados_brasileiros = [
    "AAcre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal",
    "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", 
    "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", 
    "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", 
    "São Paulo", "Sergipe", "Tocantins"
]
print(estados_brasileiros)

print()

print(estados_brasileiros[5])

#e possivel operar com números negativos de trás para frente

print(estados_brasileiros[-1])

print(estados_brasileiros[-2])

#Fazendo atribuição para correção, no caso de erro de digitação do item


estados_brasileiros[0] = 'Acre'

print(estados_brasileiros)

#acrescentar de forma dinâmica

estados_brasileiros.append('Estado Secreto' )

print(estados_brasileiros)

