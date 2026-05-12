""" Verificar se pelo menos um dos dois valores é True (VERDADEIRO). """

valor1 = int(input("Digite o Valor1:"))
valor2 = int(input("Digite o Valor2:"))

'converte uma string para um valor booleano'

if valor1 == 1:
    valor1 = True
    print(valor1)
else:
    valor1 = False
    print(valor1)


    if valor1 == valor2:
        if valor1 == True:
            print('Ambos são verdadeiros')

        else:
            print('Ambos são falsas')
    else:
        print('Uma é verdadeira e outra é falsa')  
        