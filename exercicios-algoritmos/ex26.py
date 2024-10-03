'''26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
na tela uma das mensagens abaixo:
 - O primeiro valor é o maior
 - O segundo valor é o maior
 - Não existe valor maior, os dois são iguais'''

while True:
    try:
        a = int(input("Digite o primeiro número inteiro: "))
        b = int(input("Digite o segundo número inteiro: "))
        break
    except ValueError:
        print("Por favor, insira apenas números inteiros.")

if a > b:
    print("O primeiro valor é o maior.")
elif b > a:
    print("O segundo valor é o maior.")
else:
    print("Não existe valor maior, os dois são iguais.")
