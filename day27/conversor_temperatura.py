def celsius_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

def main(temperatura, tipo_conversao):
    if tipo_conversao == 'celsius':
        print(celsius_fahrenheit(temperatura))
    elif tipo_conversao == 'fahrenheit':
        print(fahrenheit_celsius(temperatura))
    else:
        return print('Tipo de conversao invalido')
    
if __name__ == "__main__":
    main(20, "celsius")
    main(20, "fahrenheit")