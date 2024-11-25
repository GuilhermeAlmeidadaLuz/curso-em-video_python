# Data: 04/11/2024

# Exercício Python 014 - Conversor de Temperaturas

# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF


#    Tc - 0       Tf - 32                 Tc         Tf - 32              Tc       Tf - 32            9 Tc
#  ---------- = ------------   ====>  ---------- = -----------  ====> --------- = ---------- ===> ----------- + 32 = Tf
#   100 - 0       212 - 32               100           180                5           9                5
print(f'\n{'='*10} Conversor de Temperaturas {'='*10}')

celsius = float(input('Digite a temperatura em graus celsius (ºC): '))
fahrenheit = ( (9 * celsius) / 5 ) + 32
print(f'\nA temperatura {celsius} ºC (graus Celsius) equivale a {fahrenheit} F (graus Fahrenheit)')
