'''
15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
por hora trabalhada.
'''
valor_dia = 8 * 25.00

dias = int(input('Dias trabalhados esse mês: '))

print(f'Esse mês você irá receber R$ {valor_dia * dias:.2f}')