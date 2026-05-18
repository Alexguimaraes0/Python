""" Faça um programa que leia a largura e a altra de uma
parede em metros, calcule a sua área e a quantidade de tinta
necessariá para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²"""

largura = float(input('Largura da parede (m): '))
altura = float(input('Altura da parede (m): '))
area = largura * altura
litros = area / 2

print('Área da parede: {:.1f} m²'.format(area))
print('Tinta necessária: {:.1f} litros'.format(litros))