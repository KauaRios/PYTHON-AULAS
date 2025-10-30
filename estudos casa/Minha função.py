def minhafunc(x, y):
    # Garante que x seja menor que y, independentemente da ordem
    inicio = min(x, y)
    fim = max(x, y)
    
    impares = []
    
    
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            pass
        else:
            impares.append(num)
    
    return impares
