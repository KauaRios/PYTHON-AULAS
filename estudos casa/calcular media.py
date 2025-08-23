def calcular_media(numeros):
    #calcula a media de uma lista de numeros.#

    if not numeros:
        return 0
    
    total=sum(numeros)
    quantidade= len (numeros)
    media=total/quantidade
    return media

#exemplo de uso funçao
numeros=[10,20,30,40,50]
media=calcular_media(numeros)
print(f"a media dos numeros é : {media}")