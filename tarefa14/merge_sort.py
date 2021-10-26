def intercalar (lista_verde, lista_preta):
    lista_organizada = []
    i = 0
    j = 0
    while i < len(lista_verde) and j < len(lista_preta):
        if lista_verde[i] > lista_preta[j]:
         lista_organizada.append(lista_preta[j])
         j+=1
        else:
         lista_organizada.append(lista_verde[i])  
         i+=1    
    if i == len(lista_verde):
        lista_organizada += lista_preta[j:]
    elif j == len(lista_preta):
        lista_organizada += lista_verde[i:]    

    return lista_organizada      


def merge_sort(lista):
    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        meio = len(lista) // 2
        lista_verde = lista[:meio]
        lista_preta = lista[meio:]
        lista_verde = merge_sort(lista_verde)
        lista_preta = merge_sort(lista_preta)
        lista = intercalar (lista_verde, lista_preta)
        return lista   




def main():
    lista = input().split()
    lista = [int(x) for x in lista]
    lista = merge_sort(lista)
    lista = str(lista).replace(",", " ")
    lista = lista.replace('[', '')
    lista = lista.replace(']', '')
    print(lista)



main()    