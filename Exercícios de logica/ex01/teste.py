A = int(input("Numero:"))
B = int(input("Numero:"))
C = int(input("Numero:"))

luffy = ""

print(A,B,C)

def bunda():

    if((A + B ) >= C):
        luffy = ("Maior")

    else:
        luffy = ("Menor")

    return luffy

print(bunda())
