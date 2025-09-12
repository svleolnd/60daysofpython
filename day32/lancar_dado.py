import random

def lancar_dado():

    return random.randint(1, 6)

if __name__ == "__main__":
    print(f"O resultado do dado foi: {lancar_dado()}")