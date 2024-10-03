try:
    # Leitura dos três segmentos de reta
    a = float(input("Digite o comprimento do primeiro segmento: "))
    b = float(input("Digite o comprimento do segundo segmento: "))
    c = float(input("Digite o comprimento do terceiro segmento: "))

    # Verificação se é possível formar um triângulo
    if a < b + c and b < a + c and c < a + b:
        print("Os segmentos formam um triângulo ", end="")

        # Determinação do tipo de triângulo
        if a == b == c:
            print("EQUILÁTERO.")
        elif a == b or b == c or a == c:
            print("ISÓSCELES.")
        else:
            print("ESCALENO.")
    else:
        print("Os segmentos NÃO formam um triângulo.")

except ValueError:
    print("Por favor, insira valores numéricos válidos.")
