def ordena_lista(lista, lista2): 
    """ Troca os valores de forma a deixar a lista em ordem crescente, com base em outra lista (lista2)"""
    j = 0
    n = len(lista2)
    for a in range(n):
        for j in range(0, n-a-1): 
            if lista2[j] > lista2[j+1] : 
                lista2[j], lista2[j+1] = lista2[j+1], lista2[j] 
                lista[j], lista[j+1] = lista[j+1], lista[j] 
            if lista2[j] == lista2[j+1]:
                if lista[j] > lista[j+1] :
                    lista[j], lista[j+1] = lista[j+1], lista[j] 
    return lista

def main():
 L = input().split()
 c = 0
 P = []
 L1 = []    
 for i in L:
     if i not in L1:
         L1.append(i)
         """ Cria uma lista L1 sem númeos repetidos"""
 while c < len(L1):
     valor = L1[c]
     p = L.count(valor)
     P.append(p)
     c+=1
     """ Cria uma lista P com base na quantidade de vezes que cada elemento aparece em L """
 L1 = ordena_lista(L1, P)
 """ Ordena L1 de acordo com as probababilidades da lista P """                           
 for b in range(len(L1)):
     print (L1[b], end = ' ')
     """ Imprime L1"""
main()     