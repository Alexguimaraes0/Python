""" Crie um programa que peça uma senha ao usuário.

Enquanto a senha estiver errada, peça novamente.
Quando acertar, mostre "Acesso permitido!". """

senha = input('Senha: ')
senha_correnta = 'luffy123'

while senha != senha_correnta:
    print('Acesso Negado')
    senha = input('Senha: ')

if senha == senha_correnta:
    print('Acesso permitido!')
