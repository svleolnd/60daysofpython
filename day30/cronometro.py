import time

def cronometro():

    print("Cronometro de 10 segundos")
    
    tempo = 10
    
    while tempo > 0:
        print(f"Tempo restante: {tempo} segundos", end="\r", flush=True)
        time.sleep(1)
        tempo -= 1
    
    print("\nCronometro finalizado!")
    
if __name__ == "__main__":
    cronometro()