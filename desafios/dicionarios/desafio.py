pessoa = {'nome': 'Arthur', 'idade': 19, 'cidade': 'Itapevi'}

print(pessoa)

pessoa['idade'] = 20
print(pessoa)

pessoa['profissão'] = 'dev'

pessoa.update({
    'time': 'palmeiras',
    'linguagem': 'java'
})

print(pessoa)

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

frase = 'O Palmeiras vai classificar hoje contra a LDU'
contagem_palavras = {}
palavras = frase.split()

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)