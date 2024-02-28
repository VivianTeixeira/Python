'''
Verificando Idade para Votação:

Peça ao usuário que forneça sua idade como entrada.
Armazene essa idade em uma variável e, em seguida, 
use uma variável booleana para verificar se a pessoa 
é maior de idade (idade igual ou superior a 18 anos). 

Imprima uma mensagem indicando se ela pode votar ou não.
'''
print('Será que você tem idade para votar?')
idade = int(input('Qual sua idade? '))

if idade >= 18:
    print('Você já tem idade para votar')
else:
    print('Você ainda não pode votar!! Somente com 18 anos.')