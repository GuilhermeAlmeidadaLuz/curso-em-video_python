# Data: 25/10/2024

# Exercício Python 005 - Antecessor e Sucessor

# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input("Digite um número inteiro: "))
antecessor = num - 1
sucessor = num + 1
print(f'Antecessor: {antecessor}\n'
      f'{num}\n'
      f'Sucessor: {sucessor}\n')