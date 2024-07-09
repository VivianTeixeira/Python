'''
14) A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
'''
custo_dia = 90
custo_km = 0.2
km_percorrido = float(input('Km percorrido: '))
dias = int(input('Dias alugados: '))
total = (custo_dia * dias) + (custo_km * km_percorrido)
print(f'Total a pagar: R$ {total:.2f}')