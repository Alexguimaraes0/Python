#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO

num = int(input('Digite um número: '))

primo = True

for c in range(2, num):
    if num % c == 0:
        primo = False

if primo:
    print('É primo')
else:
    print('Não é primo')