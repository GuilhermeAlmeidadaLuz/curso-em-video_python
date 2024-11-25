# Data: 25/10/2024

# Exercício Python 006 - Dobro, Triplo, Raiz Quadrada

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz_quad = num ** (1/2)
print(f'Dobro de {num} é: {dobro}\n'
      f'Triplo de {num} é: {triplo}\n'
      f'Raiz Quadrada de {num} é: {raiz_quad:.2f}')