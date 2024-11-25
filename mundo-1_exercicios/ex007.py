# Data: 25/10/2024

# Exercício Python 007 -  Média Aritmética

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print(f'='*10,
      f' Cálculo de Média ',
      f'='*10)
nota_1 = float(input('Digite a 1ª nota: '))
nota_2 = float(input('Digite a 2ª nota: '))
media = (nota_1 + nota_2) / 2
print(f'A sua média é: {media:6.2f}')

# ---------------------------
# print(f'='*10,
#       f' Cálculo de Média ',
#       f'='*10)
# qtd_n = int(input('Digite a quantidade de notas: '))
# sum = 0
# for i in range(0,qtd_n):
#       nota_1 = float(input('Digite a 1ª nota: '))
#       sum += nota_1
#       media = (sum) / (i + 1)
#       print(f'A sua média é: {media:6.2f}')