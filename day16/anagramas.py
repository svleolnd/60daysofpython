def anagrama(palavra1, palavra2):
    """
    Verificar se uma palavra é um anagrama ou nao
    :param palavra1: Primeira palavra
    :param palavra2: Segunda palavra
    :return: True se for anagrama, False caso contrario
    """
    
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    if sorted(palavra1) == sorted(palavra2):
        return f'Essas palavras são anagramas.'
    return f'Essas palavras não são anagramas.'

print(anagrama("Roma", "Amor"))
print(anagrama("Python", "Java"))
print(anagrama("Listen", "Silent"))