while True:
    try:
        largura = float(input("Digite a largura do terreno em metros: "))
        comprimento = float(input("Digite o comprimento do terreno em metros: "))
        break
    except ValueError:
        print("Por favor, insira valores numéricos válidos para a largura e o comprimento.")

area = largura * comprimento

if area < 100:
    classificacao = "TERRENO POPULAR"
elif 100 <= area <= 500:
    classificacao = "TERRENO MASTER"
else:
    classificacao = "TERRENO VIP"

print(f"A área do terreno é {area:.2f} m² e a classificação é: {classificacao}.")