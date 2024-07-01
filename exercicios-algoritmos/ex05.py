'''
5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
na tela a sua média na disciplina.
Ex:
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5'''

nota_um = float(input('Nota 1: '))
nota_dois = float(input('Nota 2: '))
media = (nota_um + nota_dois)/2
print(f'A média entre {nota_um} e {nota_dois} é igual a {media:.1f}')