def escrever_arquivo_texto(nome_arquivo, conteudo):
    """
    Escreve o conteudo em um arquivo txt
    
    Args:
    nome_arquivo (str): Nome do arquivo a ser criado ou sobrescrito
    conteudo (str): Conteudo a ser escrito no arquivo
    """
    
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    
    print(f"o Conteudo foi salvo no arquivo: {nome_arquivo}.")
    
def ler_arquivo(nome_arquivo):
    """
    Le o conteudo do arquivo .txt
    
    Args:
    nome_arquivo (str): Nome do arquivo a ser criado ou sobrescrito
    """
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        print(f"Conteudo do arquivo: {conteudo}")
    except FileNotFoundError:
        print("O arquivo nao foi encontrado tente novamente")

def main(nome_arquivo, conteudo):
    """ 
    Escreve o conteudo em um arquivo txt
    
    Args:
    nome_arquivo (str): Nome do arquivo a ser criado ou sobrescrito
    conteudo (str): Conteudo a ser escrito no arquivo
    """
    print("Bem vindos ao nosso programa de escrita e leitura")
    
    escrever_arquivo_texto(nome_arquivo, conteudo)
    
    print("Fazendo a leitura do arquivo...")
    ler_arquivo(nome_arquivo)
    
if __name__ == "__main__":
    arquivo = "exemplo.txt"
    texto = "modificando texto"
    
    main(arquivo, texto)