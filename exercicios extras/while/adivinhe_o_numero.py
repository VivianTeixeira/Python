'''
Escreva um programa que solicita ao usuário que adivinhe um número entre 1 e 100. 

* O programa deve gerar um número aleatório nesse intervalo e permitir que o usuário faça várias tentativas até acertar o número. 

* Após cada tentativa, o programa deve informar se o número digitado é maior ou menor que o número gerado. 

* Quando o usuário acertar o número, o programa deve exibir quantas tentativas foram necessárias e encerrar.
'''
import random
numero_secreto = random.randint(1, 100)
print('Adivinhe o número!!!')
num_tentativa = 0

while numero_secreto >=0 and numero_secreto <=100:
    tentativa = int(input('Número: '))
    num_tentativa += 1
    if tentativa < numero_secreto:
        print('O número secreto é maior. Tente novamente!')
    elif tentativa > numero_secreto:
        print('O número secreto é menor. Tente novamente!')
    elif tentativa == numero_secreto:
        print(f'Tentativas: {num_tentativa}')
        break
    else:
        print('O número não esta entre 0 e 100. Tente novamente!')