'''
Crie um programa que solicite ao usuário que digite um número. 

Em seguida, tente converter essa entrada para um número inteiro. 

Se a conversão for bem-sucedida, exiba o número na tela. 

Se ocorrer um erro durante a conversão (por exemplo, se o usuário 
digitar um texto que não pode ser convertido em número), 
capture essa exceção usando try e except e exiba uma mensagem de erro amigável.
'''

numero = input('Digite um número: ')
try:
    numero_int = int(numero)
    print(f'INT: {numero_int}')
except:
    print('Você não digitou um número!!')