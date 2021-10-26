def achar_menor_ausente(sequencia, i):
    if sequencia[i+1] == sequencia[i] + 1:
        return achar_menor_ausente(sequencia, i + 1)
    else:
        return sequencia[i] + 1    




def main():
    sequencia = input().split()
    sequencia2 = []
    for item in sequencia:
        sequencia2.append(int(item))
    sequencia = sequencia2    
    i = 0
    menor_ausente = achar_menor_ausente(sequencia, i)
    print(menor_ausente)


main()    