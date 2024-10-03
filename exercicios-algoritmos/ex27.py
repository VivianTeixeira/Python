while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        break  # Sai do loop se as notas forem válidas
    except ValueError:
        print("Por favor, insira apenas números válidos para as notas.")

media = (nota1 + nota2) / 2

if media < 5.0:
    situacao = "REPROVADO"
elif 5.0 <= media < 7.0:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "APROVADO"

print(f"Sua média é {media:.1f} e você está {situacao}.")
