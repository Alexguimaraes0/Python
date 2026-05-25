#- Manipulação de texto
frase = 'Curso em Vídeo Python'
print(frase[0:14])

print(frase.count('o'))

print(frase.upper().count('E'))

# A função len() em Python serve para contar a quantidade de itens em algo.
print(len(frase))

# A função strip() em Python serve para remover espaços no começo e no fim de um texto.
print(len(frase.strip()))

# A função replace() em Python serve para trocar uma palavra, letra ou caractere por outro.
print(frase.replace('Python', 'Android'))
# Salvar o Android
"""frase = frase.replace('Python', 'Android')
print(frase)"""

# O in em Python serve para verificar se algo existe dentro de outro (texto, lista, etc.).
print('Curso' in frase)

# A função find() em Python serve para procurar a posição de uma palavra ou letra em um texto.
print(frase.find('Vídeo'))

# A função split() em Python serve para separar um texto em partes, transformando ele em uma lista.
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])