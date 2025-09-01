def calcular_media_notas(notas):
    """
    Calculando media de notas a partir de uma lista de notas
    
    Args:
    notas(lista)
    return:
    float da media das notas
    """
    
    media = sum(notas) / len(notas)
    
    return round(media, 2)

print(calcular_media_notas([10,4,5,6,9]))
   