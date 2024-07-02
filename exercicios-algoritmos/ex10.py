'''
10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
'''

print('Bora calcular?')
largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = (largura * altura) / 2
tinta = area / 2

print(f'Área para pintar: {area}m²')
print(f'Quantidade de tinta: {tinta:.1f}L')