salario = float((input("Digite o valor do salário:")))

if salario <= 3000:
    print("Programador júnior")
elif salario > 3000 and salario <= 5000:
    print("Programador pleno")
elif salario > 5000 and salario <= 10000:
    print("Programador sênior")
else:
    print("Gerente de Projetos")    