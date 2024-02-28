"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print()

if nome and idade:
    print(f'Seu nome é {nome}\n')
    print(f'Seu nome invertido é {nome[::-1]}\n')
    if ' ' in nome:
        print('Seu nome contém espaço\n')
    else:
        print('Seu nome não contém espaço\n')
    print(f'Seu nome tem {len(nome)} letras\n')
    print(f'A primeira letra do seu nome é "{nome[0]}"\n')
    print(f'A última letra do seu nome é "{nome[-1]}"\n')
    print(f'Obrigado por utilizar nosso sistema {nome}! S2\n', end=10*'ErRor')
else:
    print('Desculpe, você deixou campos vazios.')
