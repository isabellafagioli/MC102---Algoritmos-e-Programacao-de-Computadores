def calcular_fatorial(n):
    if n == 0 or n == 1:
        fatorial = 1
    else:
        fatorial = n * calcular_fatorial(n - 1)    
    return fatorial    


def main():
    n = int(input())
    fatorial = calcular_fatorial(n)
    print(fatorial)

main()    