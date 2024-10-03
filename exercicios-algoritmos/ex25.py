try:
    a = float(input("Digite o comprimento do primeiro segmento de reta: "))
    b = float(input("Digite o comprimento do segundo segmento de reta: "))
    c = float(input("Digite o comprimento do terceiro segmento de reta: "))

    if a < b + c and b < a + c and c < a + b:
        print("Os segmentos podem formar um triângulo.")
    else:
        print("Os segmentos não podem formar um triângulo.")
except ValueError:
    print("Por favor, insira valores numéricos válidos para os comprimentos dos segmentos.")
