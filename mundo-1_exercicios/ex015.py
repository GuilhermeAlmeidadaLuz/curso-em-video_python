# Data: 04/11/2024

# Exercício Python 015 - Aluguel de Carros

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


print(f'\n{'='*10} Cálculo de Aluguel de Carros {'='*10}')
# Obtendo entrada:
qtd_percorrida = float(input('Informe a quantidade de Km percorridos: '))
diasAlugado = int(input('Informe a quantidade de dias que o carro foi alugado: '))

# Cálculo de Preço:
custo_carro_dia = 60
custo_km_rodados = 0.15
pço_pagar = (diasAlugado * custo_carro_dia) + (qtd_percorrida * custo_km_rodados)

# Exibição de resultado:
print(f'\nO preço a pagar pelo aluguel do carro é: R$ {pço_pagar:.2f}')