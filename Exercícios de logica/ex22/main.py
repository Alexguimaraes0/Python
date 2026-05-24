""" Faça um algoritmo que efetue o cálculo do salário líquido de um professor.
 As informações fornecidas serão: valor da hora aula, número de aulas lecionadas no mês e percentual de desconto do INSS.
 Imprima na tela o salário líquido final. """

valor_h = 22.61
num_aula = 22
desc_inss = 0.14
 
sal = valor_h * num_aula

print(f'Salário bruto: R$ {sal:.2f}')

print('=' * 10)

desconto = sal * desc_inss
salario_liquido = sal - desconto

print(f'Desconto INSS (14%): R$ {desconto:.2f}')
print(f'Salário líquido: R$ {salario_liquido:.2f}')