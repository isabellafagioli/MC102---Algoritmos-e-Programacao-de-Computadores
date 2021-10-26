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
 return lista2


def achar_sugestao(par_palavras,palavras_texto):
 par_palavras = par_palavras.split()
 possiveis_palavras = []
 for c in range(len(palavras_texto)-2):
        if palavras_texto[c] == par_palavras[0] and palavras_texto[c+1] == par_palavras[1]:
            possiveis_palavras.append(palavras_texto[c+2])
 possiveis_palavras = sorted(possiveis_palavras)
 possiveis_palavras = organizar_frequencia(possiveis_palavras)
 return par_palavras[0], par_palavras[1], possiveis_palavras[0]


def main():
 arquivo = input()
 with open(arquivo) as texto:
   palavras_texto = []  
   for linha in texto:
         linha = linha.strip()
         palavras = linha.split()
         for item in palavras:
             item = item.lower()
             item = item.strip()
             item = tirar_pontuação(item)            
             palavras_texto.append(item)
 while True:
        try:
          par_palavras = input()  
          sugestao = list(achar_sugestao(par_palavras, palavras_texto))
          sugestao = ' '.join(sugestao)
          print(sugestao)
        except EOFError:
            break 
main()

