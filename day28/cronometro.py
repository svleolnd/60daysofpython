import time

def cronometro(tempo):
    """_summary_
    """
    
    print('Iniciando o cronômetro...')
    
    for segundo in range(tempo + 1):
        print(f"Tempo: {segundo} segundos", end='\r')
        time.sleep(1)
        
        print("\nCronômetro finalizado!")
        
if __name__ == "__main__":
    tempo = 10
    cronometro(tempo)
    