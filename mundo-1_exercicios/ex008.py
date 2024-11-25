# Data: 25/10/2024

# Exercício Python 008 - Conversor de Medidas

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# km - hm - dam - m - dm - cm - mm
# 0  , 0  ,  0  , 1   0    0    0

med_metros = float(input(f'Digit e a medida em metros: '))
kilômetros = med_metros / 1000 # 10^(-3) metros
hectômetros = med_metros / 100 # 10^(-2) metros
decâmetros = med_metros / 10 # 10^(-1) metros
decímetros = med_metros * 10 # 10^(1) metros
centímetros = med_metros * 100 # 10^(2) metros
milímetros = med_metros * 1000 # 10^(3) metros
print(f'[{med_metros}m] Corresponde a:\n'
      f'{kilômetros:}km\n'
      f'{hectômetros:}hm\n'
      f'{decâmetros:}dam\n'     
      f'{decímetros:}dm\n'
      f'{centímetros:}cm', end='\n'
      f'{milímetros:}mm')