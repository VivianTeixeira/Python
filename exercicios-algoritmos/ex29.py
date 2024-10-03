'''29) Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
 - Até 3 anos de empresa: aumento de 3%
 - entre 3 e 10 anos: aumento de 12.5%
 - 10 anos ou mais: aumento de 20%'''

while True:
    try:
        # Leitura dos dados do usuário
        nome = input("Digite o nome do funcionário: ")
        salario = float(input("Digite o salário atual: R$ "))
        anos_trabalho = int(input("Digite o número de anos que trabalha na empresa: "))
        break  # Sai do loop se os valores forem válidos
    except ValueError:
        print("Por favor, insira valores válidos para o salário e anos de trabalho.")

# Determinação do aumento com base nos anos de trabalho
if anos_trabalho <= 3:
    aumento = 0.03  # 3% de aumento
elif 3 < anos_trabalho <= 10:
    aumento = 0.125  # 12.5% de aumento
else:
    aumento = 0.20  # 20% de aumento

# Cálculo do novo salário
novo_salario = salario * (1 + aumento)

# Exibição do resultado
print(f"{nome}, o seu novo salário é R$ {novo_salario:.2f}.")
