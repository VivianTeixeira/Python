'''
Escreva um programa que solicite ao usuário para digitar uma senha. 

* Se a senha digitada for igual a "python", exiba a mensagem "Acesso concedido!". 

* Caso contrário, exiba a mensagem "Senha incorreta, tente novamente.".
'''

senha = 'python'

while True:
    senha_digitada = (input('Digite a senha: '))
    if senha_digitada == senha:
        print('Acesso concedido!')
        break
    else:
        print('Senha incorreta, tente novamente!')

print('Fim do programa!')
