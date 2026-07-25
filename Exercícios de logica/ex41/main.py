""" Crie um programa que simule um sistema de login. O programa deve ter um usuário e senha corretos pré-definidos
 (ex: usuário "admin", senha "Senha123"). O programa deve pedir usuário e senha ao jogador, e permitir no máximo 3 tentativas.
 Se acertar usuário e senha, mostra "Login realizado com sucesso!". Se errar as 3 vezes, mostra "Conta bloqueada!" e encerra. """

user = "admin"
password = "senha123"
tent = 0


while tent < 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    tent += 1
    if usuario != user or senha != password:
        print("Usuário ou senha invalida.")

    if usuario == user and senha == password:
        print("Login realizado com sucesso!")
        break

if tent == 3:    
    if usuario != user or senha != password:
        print("Conta Bloqueada!")
        