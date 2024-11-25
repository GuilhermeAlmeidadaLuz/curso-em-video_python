# Data: 01/11/2024

# Exercício Python 013 - Reajuste Salarial

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


print(f'{'='*10} Cálculo de Reajuste Salarial {'='*10}')
# Leitura de dados:
earnings = float(input(f'Salário: R$ '))
# Cálculo de aumento:
increase = 15/100 # 0.15 - 15%
new_earnings = earnings + (earnings * increase)
# Exibição do resultado:
print(f'Salário com aumento de {increase * 100:.0f}%: R$ {new_earnings:.2f}', end='\n'
      f'Você teve seu salário aumentado em R$ {earnings * increase:.2f}')