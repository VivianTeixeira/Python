print('CALCULADORA')

num_um = int(input('Digite um número: '))
operador = input('+, -, *, /: ')
num_dois = int(input('Digite outro número: '))

c = 0

while True:
    if operador == '+':
        resultado = num_um + num_dois
    elif operador == '-':
        resultado = num_um - num_dois
    elif operador == '*':
        resultado = num_um * num_dois
    elif operador == '/':
        resultado = num_um / num_dois
    print(f'{num_um} {operador} {num_dois} = {resultado:.2f}')
    break
    