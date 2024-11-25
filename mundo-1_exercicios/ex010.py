# Data: 31/10/2024

# Exercício Python 010 - Conversor de Moedas

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# US$ 1,00 = R$ 3,27 (2017)

print(f'{'=' * 10} Conversor de Moedas {'=' * 10}')
moeda_br = float(input('Digite a quantia que possui em caixa: R$ '))
cotacao_2017 = 3.27

currency_usa = moeda_br / cotacao_2017
print(f'Seus R$ {moeda_br:.2f} reais equivalem a: US$ {currency_usa:.2f} - na cotação de 2017')
