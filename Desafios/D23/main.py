#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE;
#QUANTAS VEZES A LETRA 'A' APARECE;
#EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

name = input('Enter your name:').strip

print(name.upper().count('A'))
print(name.upper().find('A'))
print(name.upper().rfind('A'))