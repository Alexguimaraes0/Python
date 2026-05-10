""" Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse 
usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20). """

""" 
while = enquanto
 """

salary_user = 8000.20

salary_min = 1293.20

quantity = 0

if salary_user <= salary_min:
    print("equal salary")

else:
    while salary_min < salary_user:
        salary_user = salary_user - salary_min
        quantity = quantity + 1
        if(salary_user <= salary_min):
            limit = round(salary_user,2)
            print(limit)
            print(quantity)
            break   




