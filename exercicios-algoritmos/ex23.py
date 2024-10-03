nome = input('Digite o nome do cliente: ')
sexo = input('Digite o sexo do cliente (homem/mulher): ')
valor_compras = float(input('Digite o valor das compras: R$ '))

if sexo.lower() == 'homem':
    desconto = 0.05
elif sexo.lower() == 'mulher':
    desconto = 0.13
else:
    desconto = 0

valor_final = valor_compras * (1 - desconto)
valor_final_str = f'{valor_final:.2f}'.replace('.', ',')

print(f'{nome}, o valor final com desconto é R$ {valor_final_str}')
