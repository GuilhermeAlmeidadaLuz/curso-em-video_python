# Data: 31/10/2024

# Exercício Python 009 - Tabuada

# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print(f'{'=' * 10} Cálculo de Tabuada {'=' * 10}')
number = int(input('Digite um número inteiro: '))
print(f'\nTabuada de {number}\n'
      f'{'=' * 12}')
for i in range(0, 10):
    print(f'{number} x {(i + 1):2} = {(i + 1) * number}')
