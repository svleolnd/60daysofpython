def transpor_matriz(matriz):
    """
    Gerar uma matriz transposta de 3x3
    Substitui colunas horizontais por verticais
    
    Args:
    Matriz lista de 3 numeros na horizontal e na vertical
    Return: matriz transposta
    Raises: ValueError se a matriz não for 3x3
    """
    
    # verificador se a matriz e 3x3
    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
        raise ValueError("A matriz nao possui o tamanho 3x3")
    
    # gera a matriz transposta
    transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]
    
    return transposta

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(transpor_matriz(matriz))
