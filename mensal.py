import json

file = open('dados.json', 'r')
dados = json.load(file)
lista = []

for item in dados:
    lista.append(item['valor'])

media = 0
zeros = lista.count(0)

for valor in lista:
    media = valor

media = media / (len(lista) - zeros)

dias = 0

for valor in lista:
    if valor > media:
        dias += 1

print(f"Menor valor: {min(x for x in lista if x != 0)}")
print(f"Maior valor: {max(x for x in lista if x != 0)}")
print(f"Dias acima da média: {dias}")
