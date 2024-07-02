'''
7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
sua terça parte.
Ex:
Digite um número: 3.5
O dobro de 3.5 é 7.0
A terça parte de 3.5 é 1.16666
'''
num = int(input('Digite um número: '))
dobro = num * 2
terca_parte = num/3
print(f'O dobro de {num} é {dobro:.1f}\nA terça parte de {num} é {terca_parte:.1f}')