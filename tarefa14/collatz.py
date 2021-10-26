def achar_conjectura(n, c):
    if n == 1:
        return c
    elif n%2 == 0:
        n = n//2
        c+=1
        return achar_conjectura(n, c)
    elif n%2 != 0:
        n = (n*3 + 1)//2
        c+=1
        return achar_conjectura(n, c)
        

def main():
    n = int(input())
    c = 0
    collatz = achar_conjectura(n, c)
    print(collatz)

main()    

