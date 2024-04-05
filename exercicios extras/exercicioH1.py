'''
- Variavel 's' que contém 'aba'
- Repetir o 'aba' para conter 10 cacteres
- No final mostrar na tela quantos 'a' tem na string
'''
s = "aba"
palavra_formatada = ''

for repetir in range(12 // len (s)):
    palavra_formatada += s
    if len(palavra_formatada) > 10:
        palavra_formatada = palavra_formatada[:-2]

print(len(palavra_formatada))
print(palavra_formatada)

c = palavra_formatada.count('a')
print('Número de "a"s na string: ', c)