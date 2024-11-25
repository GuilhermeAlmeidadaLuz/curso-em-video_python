# Exercício Python 002 #

#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas

nome = input('Digite seu nome: ')
print()
print('É um prazer te conhecer, {}!'.format(nome))
print()
print('É um prazer te conhecer, %s!' % (nome))
print()
print(f'É um prazer te conhecer, {nome}!')