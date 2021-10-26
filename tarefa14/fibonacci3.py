def f(n, fib):
    if n in fib:
        return fib[n]
    if n >= 0 and n <=2:
        fib[n] = n
        return n   
    else:
        fib[n] = f(n - 1, fib) + f(n - 2, fib) + f(n - 3, fib)
        return f(n-1, fib) + f(n - 2, fib) + f(n - 3, fib)

def main():
    n = int(input())
    fib = {}
    fibonacci = f(n, fib)
    print(fibonacci)

main()    