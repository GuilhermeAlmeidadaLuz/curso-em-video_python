# Data: 01/11/2024

# Exercício Python 011 - Pintando Parede

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².


# obter dados:
height = float(input(f'Digite a altura da parede (m): '))
width = float(input('Digite a largura da parede (m): '))
liter_paint_area = 2

# calcular:
area = height * width # Área da parede
qtd_ink = area / liter_paint_area # Quantidade de tinta em litros

# resultado:
print(f'\nÁrea total da parede: {area:.2f} m²'
      f'\nQuantidade de tinta necessária: {qtd_ink:.2f} l')