def achar_hanoi(n):
    if n == 1:
        return 1
    else:
        return 2*achar_hanoi(n-1) + 1    



def main():
    n = int(input())
    movimentos = achar_hanoi(n)
    print(movimentos)
main()    