def achar_soma(numero_inicial):
    soma = 0
    numero_inicial = str(numero_inicial)
    for item in numero_inicial:
        soma += int(item)
    return soma    

def mostrar_numero(numero):
    resposta = ''
    for item in numero:
        resposta += str(item)
    return resposta    

def achar_combinacoes(numero_inicial, numero_final,s):
    soma = achar_soma(numero_inicial)
    if numero_inicial == numero_final:
        if soma == s:
            print(numero_final)
    elif numero_inicial < numero_final:
        if soma == s:
            print(numero_inicial)  
        achar_combinacoes(numero_inicial + 9, numero_final, s)  
        


def main():
    n, s = input().split()
    n = int(n)
    s = int(s)
  
    numero_inicial = '1' 
    if s<10:
        for _ in range(n-1):
            numero_inicial += '0' 
        numero_final = str(s)
        for _ in range(n-1):
            numero_final+= '0'
    else:
        digitos = []
        i = 0
        while s>10:
            s-= 9
            digitos.append('9')
            i += 1
        digitos.append(str(s-1))
        for _ in range(n - 1 -len(digitos)):
            numero_inicial+='0'
        for i in range(len(digitos)):
            indice = len(digitos) - 1 - i
            numero_inicial+= str(digitos[indice])       
        for _ in range(n-3):
            numero_inicial+='0'  
        numero_final = str(9) + str(s - 9)    
        for _ in range(n-2):
            numero_final+= '0'
    numero_inicial = int(numero_inicial)          
    numero_final = int(numero_final)    
    achar_combinacoes(numero_inicial, numero_final,s)    
    




main()    