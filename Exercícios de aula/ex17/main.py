n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
            break
    s += 1
print("Acabou")
print("A soma desses números são: {}".format(s))