'''
Calculando Média Ponderada:

Crie três variáveis, nota1, nota2 e nota3, 
e atribua valores numéricos representando notas de um estudante. 

Em seguida, calcule e imprima a média ponderada dessas notas, 
assumindo que as pesos são 2, 3 e 5, respectivamente
'''

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))

peso1 = 2
peso2 = 3
peso3 = 5

calculo = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f'Sua média ponderada: {calculo:.1f}')