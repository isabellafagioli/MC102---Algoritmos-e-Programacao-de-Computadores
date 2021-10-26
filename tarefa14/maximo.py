def achar_maximo(numeros, i, maximo):
    if i + 1 < len(numeros):
        if int(numeros[i + 1]) > maximo:
            maximo = int(numeros[i+1])
        i+=1    
        maximo = achar_maximo(numeros, i, maximo)  
    return maximo 

def main():
    numeros = input().split()
    i = 0
    maximo = int(numeros[i])
    maximo = achar_maximo(numeros, i, maximo)
    print(maximo)

main()
