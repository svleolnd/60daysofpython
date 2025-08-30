def contar_palvras(texto):
    """
    contar palavras em uma string
     :param texto: str de entrada
     :return: Numero de palavras
    """
    palavras = texto.split()
    
    return len(palavras)

print(contar_palvras("Oi, tudo bem?"))