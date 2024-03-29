'''
Peça ao usuário para inserir um número inteiro positivo e faça uma contagem regressiva a partir desse número até 0, imprimindo cada número no console.
'''
print('CONTAGEM REGRESSIVA\n')

num = int(input('Digite um número: '))

while num >= 0:
    print(num)
    num -= 1

print('Fim')