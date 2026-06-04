""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal     """

num = int(input('Digite o número que deseja: '))


print('1 - binário')
print('2 - octal')
print('3 - hexadecimal')

escolha = int(input('Qual deseja? '))

if escolha == 1:
    print('Binário: {}'.format(bin(num)[2:]))

elif escolha == 2:
    print('Octal: {}'.format(oct(num)[2:]))

elif escolha == 3:
    print('Hexadecimal: {}'.format(hex(num)[2:]))

else:
    print('Opção invalida!')