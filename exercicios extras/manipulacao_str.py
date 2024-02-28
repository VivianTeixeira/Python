# Exercício:
# Peça ao usuário para digitar seu sobrenome.
# Peça ao usuário para digitar sua idade.
# Se o sobrenome e a idade forem digitados:
#     Exiba:
#         Seu sobrenome é {sobrenome}
#         Seu sobrenome invertido é {sobrenome invertido}
#         Seu sobrenome contém (ou não) espaços
#         Seu sobrenome tem {n} letras
#         A primeira letra do seu sobrenome é {letra}
#         A última letra do seu sobrenome é {letra}
#         Você tem {idade} anos
# Se nada for digitado em sobrenome ou idade:
#     Exiba "Desculpe, você deixou campos vazios."

sobrenome = input('Digite teu sobrenome: ')
idade = input('Digite sua idade: ')

if sobrenome and idade.isdigit(): #isdigit da True se todos os caracteres for numero
    print(f'Seu sobrenome: {sobrenome}')
    print(f'Seu sobrenome invertido: {sobrenome[::-1]}')
    if ' ' in sobrenome:
        print(f'Seu sobrenome contém espaço')
    else:
        print(f'Seu sobrenome não contém espaço')
    print(f'Seu sobrenome tem {len(sobrenome)} letras')
    print(f'A primeira letra do seu sobrenome: {sobrenome[0]}')
    print(f'A ultima letra do seu sobrenome: {sobrenome[-1]}')
    print(f'Você tem {idade} anos')
else:
    print('Desculpa, você deixou campos vazios ou digitou a idade errado!')