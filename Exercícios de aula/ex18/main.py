lanche = ("Hamburger", "Suco", "Pizza", "Pudim", "Batata Frita")

#for cont in range(0, len(lanche)):
 #   print(f"Eu vou comer {lanche[cont]} na posição {cont}")

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c}, na posição {pos + 1}')

print(f'Eu comi muito')