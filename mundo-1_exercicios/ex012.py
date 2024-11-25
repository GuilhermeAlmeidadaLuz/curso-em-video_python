# Data: 01/11/2024

# Exercício Python 012 - Calculando Descontos

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


print(f'{'='*10} Cálculo de Desconto {'='*10}')
# Leitura dos dados:
cost = float(input('Preço do produto: R$ '))
# Cálculo do desconto e novo preço do produto:
discount_percent = 5/100
new_cost =  cost - (cost * discount_percent)
# Impressão do resultado:
print(f'Seu desconto pela promoção de 5% é de R$ {cost * discount_percent:.2f}', end='\n'
      f'Produto com desconto de {discount_percent * 100:.0f}% fica: R$ {new_cost:.2f}')