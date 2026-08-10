""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso. """

user = int(input("Digite um número de 0 a 20: "))

num_extenso = ("zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")

if user > 20 or user < 0:
    user = int(input("Tente novamente. Digite um número de 0 a 20"))

for pos , num in enumerate(num_extenso):
    if user == pos:
        print(f"Você digitou o Número {num}")