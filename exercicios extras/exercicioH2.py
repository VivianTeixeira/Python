def contar_pares_de_meias(n, ar):
    contagem_cores = {}  # Inicializa um dicionário vazio para contar as meias de cada cor
    
    # Contar quantas meias de cada cor temos
    for cor in ar:
        if cor in contagem_cores:
            contagem_cores[cor] += 1
        else:
            contagem_cores[cor] = 1

    # Contar quantos pares de meias podemos fazer
    total_pares = 0
    for quantidade in contagem_cores.values():
        total_pares += quantidade // 2

    return total_pares

n = 9  # Número de cores diferentes
ar = [1, 2, 3, 1, 2, 3, 4, 4, 8]  # Lista de cores das meias
print("Número total de pares de meias:", contar_pares_de_meias(n, ar))