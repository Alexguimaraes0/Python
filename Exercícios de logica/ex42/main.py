# Exercício: Validador de Login com Tentativas Limitadas

user = "admin"
password = "1234"
cont = 0
tent = 3

while cont < 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    cont +=1

    if usuario != user or senha != password:
        print("Usuário ou senha invalida!")
        print(f"Tentativas restantes {tent - 1}")
    tent -= 1

    if usuario == user and senha == password:
        print("Login efetuado com sucesso!")
        break
    
    if tent == 0:
        print("Acesso Bloquado.")
        break
