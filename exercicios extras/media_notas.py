'''
Média de Notas
Peça ao usuário para fornecer três notas de um estudante (em valores de 0 a 10). 
Calcule a média dessas notas e exiba o resultado formatado. Além disso, inclua uma 
mensagem que diga se o estudante foi aprovado ou reprovado, considerando que a média 
para aprovação é 6.0.

Lembre-se de usar variáveis para armazenar as notas e a média, 
e utilize estruturas condicionais para determinar se o estudante foi aprovado ou reprovado. 
Ao exibir a média, formate o resultado para mostrar até duas casas decimais.
'''

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'Nota final: {media:.2f}')
    print('ALUNO APROVADO!')
else:
    print(f'Nota final: {media:.2f}')
    print('ALUNO REPROVADO!')
    
    
'''
outro jeito também

# Solicita ao usuário três notas
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Verifica se o estudante foi aprovado ou reprovado
resultado = 'Aprovado' if media >= 6.0 else 'Reprovado'

# Exibe a média e o resultado formatados
print(f'A média das notas é: {media:.2f}')
print(f'O estudante está {resultado}.')

'''