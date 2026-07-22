""" Crie um programa que leia o salário de vários funcionários. O programa deve perguntar se o usuário quer continuar cadastrando. No final, mostre:

A) A soma total da folha de pagamento.
B) Quantos funcionários ganham acima da média salarial (calculada com todos os salários cadastrados).
C) O maior e o menor salário cadastrado. """

soma = 0
quant = 0
maior = 0
menor = float('inf')
salarios = []  # lista pra guardar todos os salários

while True:
    salario = float(input("Insira seu salário: R$"))
    soma += salario
    quant += 1
    salarios.append(salario)  # guarda o salário na lista

    if salario > maior:
        maior = salario
    elif salario < menor:
        menor = salario

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    while continuar not in "SsnN":
        continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break

# calcula a média SÓ depois que todos os salários foram cadastrados
media = soma / quant

# percorre a lista comparando cada salário com a média final
acima_salario = 0
for s in salarios:
    if s > media:
        acima_salario += 1

print(f"A soma total da folha de pagamento: {soma}")
print(f"{acima_salario} funcionários ganham acima da média.")
print(f"Maior salário: {maior}")
print(f"Menor salário: {menor}")