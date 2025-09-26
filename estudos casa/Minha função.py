def minhafunc(x, y):
    # Garante que x seja menor que y, independentemente da ordem
    inicio = min(x, y)
    fim = max(x, y)
    
    impares = []
    pares = []
    
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return impares, pares
