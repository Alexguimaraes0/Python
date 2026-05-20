

nota1 = float(input('Nota do 1° Bimestre:'))
nota2 = float(input('Nota do 2° Bimestre:'))
nota3 = float(input('Nota do 3° Bimestre'))

for x in range(5):
    total = nota1 + nota2 + nota3 / 3   
    print(f'Sua média:{total}')