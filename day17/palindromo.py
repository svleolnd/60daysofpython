def eh_palindromo(texto):
    """
    verificar se um numero, texto ou palavra eh um palindromo
    :param texto: Palavra, texto ou numero a ser verificado
    :return: True se for palindromo, False caso contrario   
    """
    texto = str(texto).replace(" ", "").lower()
    
    if texto == texto[::-1]:
        return f"'{texto}' é um palíndromo"
    return f"'{texto}' não é um palíndromo"

print(eh_palindromo("arara"))
print(eh_palindromo("python"))
    