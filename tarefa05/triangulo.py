# lê uma string com três partes
a, b, c = input().split()

# converte strings em números
a = float(a)
b = float(b)
c = float(c)

# termine esse programa aqui...
if a + b > c and a + c > b and b + c > c:
    if a >= b and a >= c:
        if a*a == b*b + c*c:
            print("retângulo")
        if a*a > b*b + c*c:
            print("obtusângulo") 
        if a*a < b*b + c*c:
            print("acutângulo")       
    elif b >= a and b >= c:
        if b*b == a*a + c*c:
            print("retângulo")
        if b*b > a*a + c*c:
            print("obtusângulo") 
        if b*b < a*a + c*c:
            print("acutângulo")  
    elif c >= b and c >= a:
        if c*c == b*b + a*a:
            print("retângulo")
        if c*c > b*b + a*a:
            print("obtusângulo") 
        if c*c < b*b + a*a:
            print("acutângulo")  
else:
    print("não forma triângulo")            
