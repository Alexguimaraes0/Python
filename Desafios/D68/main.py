""" Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense. """

times = "Athletico-PR", "Atlético-MG", "Bahia" ,"Botafogo", "Chapecoense", "Corinthians", "Coritiba", "Cruzeiro", "Flamengo", "Fluminense", "Grêmio", "Internacional", "Mirassol", "Palmeiras", "Red Bull Bragantino", "Remo", "Santos", "São Paulo", "Vasco da Gama", "Vitória"

print("-=" * 30)
print(f"Lista de times Brasileirão {times}")
print("-=" * 30)
print(f"Os 5 Primeiros são {times[:5]}")
print("-=" * 30)
print(f"Os 4 Ultimos são {times[16:]}")
print("-=" * 30)
print(f"Times em ordem alfábetica {sorted(times)}")
print("-=" * 30)
print(f"O Flamengo está na {times.index("Flamengo") + 1}º lugar")
