import json
from typing import Any

# none indica que a funcao nao retorna nada
def salvar_dados(arquivo: str, dados: Any) -> None:
    """ 
    Salva os dados fornecidos em um arquivo json
    
    :param: arquivo: Caminho para o arquivo json
    :param dados: Os dados que serao armazenados no arquivo
    
    """
    
    with open(arquivo, 'w', encoding="utf-8") as f:
    # ensure_ascii = False mantém os acentos, Ç e etc
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_dados(arquivo: str) -> Any:
    """ 
    Le os dados do arquivo json
    :param arquivo: Caminho para o arquivo json
    :return: dados carregados e lidos do arquivo json
    """
    
    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("O arquivo nao foi encontrado. caminho do arquivo {arquivo}")
        return{}

dados_exemplos = {'Nome': 'Leonardo', 'cidade':'Taubate', 'cargo': 'data analyst'}

nome_arquivo = 'nome_leonardo.json'

salvar_dados(nome_arquivo, dados_exemplos)

dados_carregados = carregar_dados(nome_arquivo)

print("Dados carregados:", dados_carregados)