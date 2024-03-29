''''
Solicite um número inteiro positivo ao usuário e calcule a soma dos dígitos desse número. Por exemplo, se o número inserido for 123, a soma dos dígitos será 1 + 2 + 3 = 6.
'''

print('SOMANDO DIGITOS\n')
num = input('Digite um número: ')
soma = 0
i = 0

while i < len(num):
    soma += int(num[i])
    i += 1

print(f'Soma: {soma}')