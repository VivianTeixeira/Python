print("-----Bem-vindo ao jogo-----\n")
print("***** QUAL É O MAIOR *****")
print("")

valor_um = int(input("Digite um valor: "))
valor_dois = int(input("Digite outro valor: "))
print("")

if valor_um > valor_dois:
    print(f"O 1º valor é maior ({valor_um} é maior que {valor_dois})\n")
elif valor_um < valor_dois:
    print(f"O 2º valor é maior ({valor_dois} é maior que {valor_um})\n")
else:
    print(f"Os valores são iguais ({valor_um} é igual a {valor_dois})\n")

print("Obrigada por participar do jogo!")