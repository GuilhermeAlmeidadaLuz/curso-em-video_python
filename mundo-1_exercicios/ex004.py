# Data: 23/10/2024

# Exercício Python 004 -  Dissecando uma Variável

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

entrada = input('Digite algo: ')
print('Qual tipo do que foi digitado? ', type(entrada))
print('O que foi digitado é numérico? ', entrada.isnumeric())
print('O que foi digitado é alfanúmerico? ', entrada.isalnum())
print('O que foi digitado é alfabético? ', entrada.isalpha())
print('O que foi digitado é totalmente maiúsculo? ', entrada.isupper())
print('O que foi digitado é totalmente minúsculo? ', entrada.islower())
print('O que foi digitado é decimal? ', entrada.isdecimal())
print('O que foi digitado é um Título? ', entrada.istitle())
print('O que foi digitado é composto só por espaços? ', entrada.isspace())
print('O que foi digitado é capitalizado: ', entrada.istitle())

