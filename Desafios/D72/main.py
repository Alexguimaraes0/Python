""" Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. """

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

vogais = 'aeiou'

for c in palavras:
    vogais_encontradas = [letra for letra in c if letra in vogais]
    print(f"na palavra {c.upper()} temos {' '.join(vogais_encontradas)}")
   