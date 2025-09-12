from collections import Counter

def contar_ocorrencias(lista):
    
    contagem = Counter(lista)
    
    for elemento, quantidade in contagem.items():
        print(f"{elemento}: {quantidade}")
        
    return "Contagem realizada com sucesso"

if __name__ == "__main__":
    lista_exemplo = ['banana', 'laranja', 'uva', 'laranja', 'uva', 'pera']
    
    print(contar_ocorrencias(lista_exemplo))