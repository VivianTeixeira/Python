'''
Crie uma string contendo nomes de algumas frutas separadas por vírgulas. 

Solicite ao usuário que digite o nome de uma fruta e verifique se a fruta está na string. 

Se estiver, imprima uma mensagem indicando que a fruta está disponível. 

Caso contrário, imprima uma mensagem indicando que a fruta não está disponível.
'''

frutas_disponiveis = 'maçã, pêra, banana, limão, tomate'
fruta = input('Qual fruta você deseja? ')

if fruta.lower() in frutas_disponiveis.lower():
    print(f'Temos {fruta} disponivel!')
else:
    print(f'Não temos {fruta} disponivel!')