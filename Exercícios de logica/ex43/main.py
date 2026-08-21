

qtd_classe1 = 10
qtd_classe2 = 15
qtd_classe3 = 18

passageiros_classe1 = []
passageiros_classe2 = []
passageiros_classe3 = []
assentos_especias = []

for i in range(qtd_classe1):
    nome = input(f"Nome do passageiro {i+1} (primeira classe): ")
    necessidade = input("Necessidade especial (ou nenhuma: )").strip().upper()
    passageiros_classe1.append((nome, necessidade))

for i in range(qtd_classe2):
    nome = input(f"Nome do passageiro {i+1} (classe executiva): ")
    necessidade = input("Necessidade especial (ou nenhuma): ").strip().upper()
    passageiros_classe2.append((nome, necessidade))

for i in range(qtd_classe3):
    nome = input(f"Nome do passageiro: {i+1} (classe econômica): ")
    necessidade = input("Necessidade especial (ou nenhuma): ").strip().upper()
    passageiros_classe3.append((nome, necessidade))

assentos_especias = passageiros_classe1 + passageiros_classe2 + passageiros_classe3
necessitados = [p for p in assentos_especias if p[1] != "NENHUMA"]

print(f"Total de passageiros com necessidade {len(necessitados)}")
for nome, necessidade in necessitados:
    print(f"- {nome}: {necessidade}")

