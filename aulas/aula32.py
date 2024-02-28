"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
print("PAR OU IMPAR?")
numero = input('Digite um número inteiro: ')

try:
    num_int = int(numero)
    if num_int % 2 == 0:
        print('Par\n')
    else:
        print('Impar\n')
except:
    print('Não é um número inteiro!\n')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('QUE HORAS SÃO?')
hora = int(input('Hora (sem minutos): '))

if hora >= 0 and hora <= 11:
    print('Bom dia!')
elif hora >= 12 and hora <= 17:
    print('Boa tarde!')
elif hora >= 18 and hora <= 23:
    print('Boa noite!')
print()

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

primeiro_nome = input('Primeiro nome: ')
lendo = len(primeiro_nome)

if len(primeiro_nome) <= 4:
    print('Seu nome é curto!')
elif len(primeiro_nome) >= 5 and len(primeiro_nome) <= 6:
    print('Seu nome é normal!')
elif len(primeiro_nome) >= 6 :
    print('Seu nome é grande!')