A = int(input("Número:"))
par_impar = ""
pos_neg = ""
print("Número escolhido:", A)

def par_impar():
    if((A % 2) == 0):
        par_impar = ("Par")
    
    else:
        par_impar = ("Impar")

    return par_impar

print("Paridade:",par_impar())

def pos_neg():
    if(A > 0):
        pos_neg = ("Positivo")

    else:
        pos_neg = ("Negativo")

    return pos_neg

print("Sinalização",pos_neg())