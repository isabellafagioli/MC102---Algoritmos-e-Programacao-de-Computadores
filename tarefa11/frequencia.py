def entrada():
 arquivo = input()
 stop_words = set(input().split())
 palavras_texto = []
 todas_as_palavras = []
 with open(arquivo) as texto:
     for linha in texto:
         linha = linha.strip()
         palavras = linha.split()
         for item in palavras:
             item = item.lower()
             item = item.strip()
             item = tirar_pontuação(item)            
             if item not in stop_words:
               palavras_texto.append(item)

                
 return palavras_texto

def tirar_pontuação(palavra):
 pontuacao = '''!()[]{};:'"\,<>./?@#$%&*_'''
 sem_pontuacao = ""
 for char in palavra:
   if char not in pontuacao:
       sem_pontuacao = sem_pontuacao + char
 return sem_pontuacao      

def organizar_frequencia(lista):
 lista = sorted(lista)   
 P = []  
 lista2 = []
 for item in lista:
     if item not in lista2:
         lista2.append(item)
 c = 0        
 while c < len(lista2):
     valor = lista2[c]
     p = lista.count(valor)
     P.append(p)
     c+=1   
 j = 0
 n = len(lista2)
 for a in range(n - 1):
     for j in range(n-a-1):  
         if P[j] < P[j+1] : 
             P[j], P[j+1] = P[j+1], P[j] 
             lista2[j], lista2[j+1] = lista2[j+1], lista2[j]
 return lista2, P            

def achar_quartil(palavras_texto):
 palavras, P = organizar_frequencia(palavras_texto)
 palavras_remover = [] 
 for i in range(len(P)):
     if P[i] < 5:
         palavras_remover.append(palavras[i])
 for i in range(len(palavras)):
     for item in palavras:
       if item in palavras_remover:
          palavras.remove(item)  
 j = len(palavras)// 4 - 1
 c = 0
 i = 0
 for i in range(len(palavras)):
     elemento = P[i]
     if elemento >= P[j]:
         c+=1 
                       
 return c, palavras
       


def main():
 palavras_texto = entrada()
 lista_de_palavras = organizar_frequencia(palavras_texto)[0]
 quartil , palavras= achar_quartil(palavras_texto)
 print(lista_de_palavras[0], lista_de_palavras[1], lista_de_palavras[2])
 print(quartil)
 print(palavras[quartil],palavras[quartil+1], palavras[quartil+2])



main()    

    