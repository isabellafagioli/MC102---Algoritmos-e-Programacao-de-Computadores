def eh_primo(n):
    eh_primo = True
    d = 2
    if n != 1:
        for d in range(2, n):
            if n % d == 0:
               eh_primo = False
               break
        return eh_primo   

def quadrado(n):
    quadrado = n**2
    return quadrado

def somar(lista):
    soma = 0
    k = 0
    while k < len(lista):
       q = lista[k]
       soma = soma + q
       k+=1
    return soma

def filtra(funcao, lista ):
    i = 0
    lista2 = []
    while i < len(lista):
        lista[i] = int(lista[i])
        if funcao(lista[i]):
            lista2.append(lista[i])
        i+=1  
    return lista2

def mapeia(funcao2, lista2):  
    c = 0
    lista3 = []
    while c < len(lista2):
       p = lista2[c]
       quadrado = funcao2(p)
       lista3.append(quadrado)
       c+=1  
    return lista3

def reduz(funcao3, lista3):
       resultado = funcao3(lista3)
       return resultado   

def main():
    lista = input().split()
    primos = filtra(eh_primo, lista)
    quadrados_primos = mapeia(quadrado,primos)
    resposta = reduz(somar, quadrados_primos)
    print(resposta)

main()    