def calcular_potencia(a,b):
    if b == 1:
        return a
    else:
        return a*calcular_potencia(a, b-1)    


def main():
    a,b = input().split()
    a, b = int(a), int(b)
    resposta = calcular_potencia(a,b)
    print(resposta)
main()    