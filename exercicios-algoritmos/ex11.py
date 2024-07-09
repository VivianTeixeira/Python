'''
11) Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
segundo grau e mostre o valor de Delta.
'''
a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))
delta = b**2 - 4 * a * c
print(f'Valor de Delta: {delta}')