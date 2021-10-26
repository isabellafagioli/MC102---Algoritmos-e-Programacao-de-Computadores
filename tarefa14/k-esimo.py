def achar_kesimo(sequencia, k, n):
    menor = sequencia[0]
    for i in range(len(sequencia)):
        if sequencia[i] <= menor:
            menor = sequencia[i]
    sequencia.remove(menor)   
    if n == k:
        return menor
    else:
        return achar_kesimo(sequencia, k, n +1)           


def main():
    sequencia = input().split()
    sequencia = [int(x) for x in sequencia]
    k = input()
    k = int(k) 
    n = 1
    kesimo = achar_kesimo(sequencia, k, n)
    print(kesimo)
   

main()    