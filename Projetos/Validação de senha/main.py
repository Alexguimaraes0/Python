""" Validação de senha """


while True:
    c = 0
    tem_numero = False
    tem_maiuscula = False
    tamanho = False

    senha = input("Digite sua senha: ")
    while c < len(senha):
        letra = senha[c]
        if letra.isdigit():
            tem_numero = True
        if letra.isupper():
                tem_maiuscula = True
        c += 1

    if len(senha) < 8:
        print("Senha muito curta! Precisa ter pelo menos 8 caracteres.")
    else:
         tamanho = True

    if tem_numero != True:
        print("A senha tem que conter pelo menos um número.")
    else:
         tem_numero = True

    if tem_maiuscula != True:
         print("A senha tem que conter pelo menos uma letra maiuscula.")
    else:
         tem_maiuscula = True

    if tamanho == True and tem_numero == True and tem_maiuscula == True:
         print("Senha Valida! ✔")
         break
    