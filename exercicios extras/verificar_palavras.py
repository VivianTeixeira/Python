'''
Peça ao usuário para digitar uma frase e, em seguida, peça que ele digite uma palavra.
Verifique se a palavra está presente na frase e imprima uma mensagem indicando o resultado.
'''

frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra: ')

if palavra.lower() in frase.lower():
    print(f'A palavra "{palavra}" está na frase!!!')
else:
    print(f'A palavra "{palavra}" não foi encontrada na frase!!!')