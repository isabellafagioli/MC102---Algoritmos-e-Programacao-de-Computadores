n = int(input())
if n > 1000:
    a = n//1000
    b = (n%1000)//100
    c = (n%100)//10
    d = n%10
    if a == d and b ==c:
        print("sim")
    else:
        print("não")    
if n > 100 and n < 1000:
    a = n//100
    b = (n%100)//10
    c = n%10
    if a == c:
        print("sim")   
    else:
        print("não")          
if n > 10 and n < 100:
    a = n//10
    b = n%10
    if a == b:
        print("sim")
    else:
        print("não")   
if n < 10:
    print("sim")        
