def contar_pares_de_meias(cores):
    contagem_cores = {}  # Dicionário para contar quantas meias de cada cor temos

    # Contar quantas meias de cada cor temos
    for cor in cores:
        if cor in contagem_cores:
            contagem_cores[cor] += 1
        else:
            contagem_cores[cor] = 1

    # Contar quantos pares de meias podemos fazer
    total_pares = 0
    for quantidade in contagem_cores.values():
        total_pares += quantidade // 2

    return total_pares

# Exemplo de uso
meias = [1, 2, 1, 3, 2, 1, 2, 3, 1, 4, 4]  # Exemplo de matriz de cores de meias
print("Número total de pares de meias:", contar_pares_de_meias(meias))
