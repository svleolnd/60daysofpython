def conversor_moeda(valor, taxa_cambio, tipo_conversao):
    """
    Essa funcao converte dolar em reais e visse e versa
    
    Args:
        Valor: (float): Valor a ser convertido (monetario)
        taxa_cambio: A taxa de cambio atual
        tipo_conversao: dolar para real e real para dolar
        
    Return:
        float: O Valor convertido, arredondado para 2 casas decimais
    Raises:
        ValueError: Se o tipo de conversao for errado
    """
    
    if tipo_conversao == 'dolar_real':
        return round(valor * taxa_cambio, 2)
    elif tipo_conversao == 'dolar_real':
        return round(valor / taxa_cambio, 2)
    else:
        return ValueError("Tipo de conversao invalida")

print(conversor_moeda(12, 6.10, 'dolar_real'))