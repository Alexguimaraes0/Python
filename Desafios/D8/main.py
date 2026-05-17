

largura = float(input('Largura da parede (m): '))
altura = float(input('Altura da parede (m): '))
area = largura * altura
litros = area / 2

print('Área da parede: {:.2f} m²'.format(area))
print('Tinta necessária: {:.2f} litros'.format(litros))

