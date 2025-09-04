def tabuada():
    """
    Essa funcao recebe um numero e retorna a tabuada desse numero
    """
    
    try:
        # solicitar o numero para o usuario
        numero = int(input("Digite um numero para gerar a tabuada: "))
        
        print(f"\nTabuada de {numero}:")
        
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
        
    except ValueError:
        print("Por favor, digite um numero valido.")

if __name__ == "__main__":
    tabuada()