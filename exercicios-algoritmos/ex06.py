'''
6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
sucessor.
Ex:
Digite um número: 9
O antecessor de 9 é 8
O sucessor de 9 é 10
'''
num = int(input('Digite um número: '))
antecessor = num - 1
sucessor = num + 1
print(f'O antecessor de {num} é {antecessor}\nO sucessor de {num} é {sucessor}')