'''
13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento.
'''
salario = float(input('Salário: R$ '))
novo_salario = salario + (15/100 * salario)
print(f'Salário antigo R$ {salario:.2f} \nSalário novo R$ {novo_salario:.2f}')