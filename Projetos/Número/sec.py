

while True:
    telefone = input("Digite seu número: ")

    if telefone.isdigit():    
        if telefone.isdigit() == 11:
            numeros = telefone
            print(f'({numeros[0:2]}) {numeros[2:7]}-{numeros[7:11]}')