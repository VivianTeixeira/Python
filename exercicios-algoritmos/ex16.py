'''
16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.
'''
# Solicitar os dados de entrada
cigarros_por_dia = int(input('Quantidade de cigarros fumados por dia: '))
anos_fumados = int(input('Quantidade de anos que você já fumou: '))

# Calcular o total de cigarros fumados
total_cigarros = cigarros_por_dia * anos_fumados * 365

# Calcular o tempo de vida perdido em minutos
tempo_perdido_minutos = total_cigarros * 10

# Converter o tempo perdido para dias
tempo_perdido_dias = tempo_perdido_minutos / 1440

# Exibir o resultado
print(f'Você perdeu aproximadamente {tempo_perdido_dias:.2f} dias de vida devido ao hábito de fumar.')
