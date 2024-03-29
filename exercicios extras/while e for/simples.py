'''

Escreva um programa que solicite ao usuário digitar cinco números e, em seguida, imprima a média desses números.
Escreva um programa que solicite ao usuário digitar uma palavra e, em seguida, imprima cada letra da palavra em uma linha separada.
Escreva um programa que solicite ao usuário digitar um número e, em seguida, imprima a tabuada desse número até 10.
Escreva um programa que imprima os números de 10 a 1 em ordem decrescente.
Escreva um programa que imprima os números de 1 a 10, mas pule o número 7.
Escreva um programa que solicite ao usuário digitar uma frase e, em seguida, imprima cada palavra da frase em uma linha separada.
'''

print('Escreva um programa que imprima os números de 1 a 10.')
for numero in range(1, 11):
    print(numero)

print('\nEscreva um programa que imprima os números pares de 1 a 20.')
for pares in range(0, 21, 2):
    print(pares)

print('\nEscreva um programa que imprima os números ímpares de 1 a 20.')
for impar in range(1, 21, 2):
    print(impar)

print('\nEscreva um programa que calcule e imprima a soma dos números de 1 a 100.')
soma = 0
for i in range(1, 101):
    soma += i
print('A soma dos númerod de 1 a 100 é:', soma)