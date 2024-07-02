'''
9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
'''

dinheiro = float(input('Quanto de dinheiro você tem na carteira? R$ '))
conversao = dinheiro * 3.45
print(f'Você pode comprar U${conversao:.2f}')