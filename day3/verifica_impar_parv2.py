entrada = input("Coloque o numero:")

try:
    numero = int(entrada)
    if numero % 2 == 0:
        print("Numero e par")
    else:
        print("Numero e impar")
except ValueError:
    print("Voce nao passou um numero inteiro")