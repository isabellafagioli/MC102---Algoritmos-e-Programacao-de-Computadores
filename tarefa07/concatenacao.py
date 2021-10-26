def main():
 A = input().split()
 B = input().split()
 """ Recebe as listas A e B"""
 C = []
 i = 0
 while i < len(A):
     c = str(A[i]) + str(B[i])
     i+=1 
     C.append(c)
 """ "Soma" (nesse caso junta dois pedaçoes de palavras) cada elemento de A com o elemento de B correspondente"""
 l = 0
 while l < len(C):
     print(C[l], end=' ')
     l+=1
 """ Imprime cada elemento da lista da junção de A e B"""
main()     