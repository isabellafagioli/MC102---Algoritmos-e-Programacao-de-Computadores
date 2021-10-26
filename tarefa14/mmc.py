def achar_mdc(a,b):
    if b>=a:
        a,b = b,a
    if b!= 0:
        a = a - b
        return achar_mdc(a,b)
    elif b == 0:
        return a    
     
def main():
    a, b = input().split()
    a, b = int(a), int(b)
    mdc = achar_mdc(a,b)
    mmc = (a*b)//mdc
    print(mmc)
main()    