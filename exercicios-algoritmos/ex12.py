'''
12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
PREÇO PROMOCIONAL, com 5% de desconto.
'''
produto = float(input('Valor do produto: R$ '))
desconto = produto - (5/100 * produto)
print(f'Preço promocional R$ {desconto:.2f}')