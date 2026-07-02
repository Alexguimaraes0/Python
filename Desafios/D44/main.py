#FAÇA UMA TABUADA UTILIZANDO O NÚMERO QUE O USUÁRIO ESCOLHER E O LAÇO FOR

num = int(input('Digite um número: '))

for c in range(1, 11):
    print(f'{num} X {c} = {num * c}') 