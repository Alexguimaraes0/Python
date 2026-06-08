#for c in range()

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!')

print('=' * 10)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorrio de todos os valores é: {}'.format(s))