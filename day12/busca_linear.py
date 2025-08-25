def busca_linear(lista, numero_procurado):
    """
    Procurar um numero dentro de uma lista utilizando busca linear
    
    :param lista: lista de numeros
    :param numero_procurado: numero a ser procurado
    """
    for i, numero in enumerate(lista):
        if numero == numero_procurado:
            return i
    return -1
 
lista = [1, 3, 5, 7, 9]
numero_procurado = 8
 
buscando_numero = busca_linear(lista, numero_procurado)
print(buscando_numero)

if buscando_numero != -1:
    print(f"Número {numero_procurado} encontrado na posição {buscando_numero}") 
else:
    print(f"Número {numero_procurado} não encontrado na lista")