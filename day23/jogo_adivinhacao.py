import random

def jogar_adivinhacao():
    """"
    Um jogo o usuário tenta advinhar um número secreto entre 0 e 10.
    """
    print("Bem vindos ao nosso jogo de adivinhação!")
    
    numero_secreto = random.randint(0, 10)
    
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Digite um número entre 0 e 10: "))
            tentativas += 1
        
            if palpite < numero_secreto:
                print('Muito abaixo do número secreto!')
            elif palpite > numero_secreto:
                print('Muito acima do número secreto!')
            else:
                print(f'Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!')
                break
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    jogar_adivinhacao()