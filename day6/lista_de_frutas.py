#frutas = ['banana', 'maca', 'uva' , 'pera', 'manga']

#for fruta in frutas:
#    print(fruta)
    
frutas = []

while True:
    fruta = input("Digite o nome da fruta: ")
    if fruta == "sair":
        break
    frutas.append(fruta)

print(frutas)