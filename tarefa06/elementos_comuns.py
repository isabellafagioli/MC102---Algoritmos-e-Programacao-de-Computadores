lista_A  = input().split()

lista_B = input().split()

lista_C = []

i = 0
while i< len(lista_A):
    if lista_A[i] not in lista_C:
        if lista_A[i] in lista_B:
            lista_C.append(lista_A[i])
    i+=1

l = 0
while l < len(lista_C):
    print(lista_C[l], end=' ')
    l+=1