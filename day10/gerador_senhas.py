import random
import string


def gerador_senhas(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    
    while len(senha) < comprimento:
        senha += random.choice(caracteres)
        
    print(f"Sua senha ficou assim: {senha}")

gerador_senhas(30)