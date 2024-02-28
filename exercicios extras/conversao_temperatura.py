'''
Conversão de Temperatura:

Solicite ao usuário que insira uma temperatura em graus Celsius. 
Converta essa temperatura para Fahrenheit usando a fórmula 

- F = C * 9/5 + 32 e imprima o resultado.
'''

print('Conversor de temperatura! Bora ver como esta a temperatura em Fahrenheit')
celsius = int(input('Quantos graus está? '))
confirmacao = input(f'Então esta {celsius}°C?')

if confirmacao == 'sim' or confirmacao == 'Sim':
    print(f'{celsius}°C = {celsius*9/5 + 32}°F')
else:
    print('Desculpe o erro')
    