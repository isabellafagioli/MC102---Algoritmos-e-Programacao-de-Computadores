def codificar(largura, altura, imagem):
 i = 0
 codificacao = []
 while i < altura:   
   j = 0  
   while j < largura: 
     if i + 1 < altura:
      if imagem[i][j] == 0 and imagem[i + 1][j] == 0:
            codificacao.append(1)
            codificacao.append('00')
      if imagem[i][j] == 0 and imagem[i + 1][j] == 1:
            codificacao.append(1)
            codificacao.append('01')
      if imagem[i][j] == 1 and imagem[i + 1][j] == 0:
            codificacao.append(1)
            codificacao.append('10')
      if imagem[i][j] == 1 and imagem[i + 1][j] == 1:
            codificacao.append(1)
            codificacao.append('11')   
      j+=1                              
   i+=2      
 k = 1
 codificacao2 = []
 while k < len(codificacao):
  c = 1
  a = codificacao[k] 
  while k + 2 <len(codificacao) and codificacao[k] == codificacao[k +2]:
    c+=1
    k+=2
  codificacao2.append(c)
  codificacao2.append(a)
  k+=2  
 codificacao = codificacao2
 codificacao = str(codificacao2).strip("'[]'")
 codificacao = codificacao.replace(",",'')
 codificacao = codificacao.replace("'", '')
 return codificacao


def decodificar(largura, altura, codificacao):  
 m = 0
 imagem = []
 codificacao2 = []
 k = 0
 while k < len(codificacao):
   c = int(codificacao[k]) 
   if k + 2 <= len(codificacao):
     for _ in range(c):
        codificacao2.append(1)
        codificacao2.append(codificacao[k+1])
     k+=2  
 k = 0 
 codificacao = codificacao2     
 while m < altura:
    linha1 = []
    linha2 = []
    imagem.append(linha1)
    imagem.append(linha2)
    a = 0
    for a in range(largura):
        if k < len(codificacao):
         c = int(codificacao[k])   
         for _ in range(c):
                if codificacao[k + 1] == '00':
                    linha1.append(0)
                    linha2.append(0)
                if codificacao[k + 1] == '01':
                    linha1.append(0)
                    linha2.append(1)
                if codificacao[k + 1] == '10':
                    linha1.append(1)
                    linha2.append(0)
                if codificacao[k + 1] == '11':
                    linha1.append(1)
                    linha2.append(1)             
         k+=2 
    m+=2            
 return imagem


def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as imagem_codificada:
        infos_da_codificacao = []
        for linha in imagem_codificada:
            linha = linha.strip()
            linha_da_matriz = []
            linha_da_matriz.append(linha)
            infos_da_codificacao.append(linha_da_matriz)
    tamanho = infos_da_codificacao[1]
    tamanho = str(tamanho)
    tamanho = tamanho.split()
    largura = str(tamanho[0])
    largura = int(largura.strip("['"))
    altura = str(tamanho[1])
    altura = int(altura.strip("]'"))
    codificacao = str(infos_da_codificacao[2])
    codificacao = codificacao.split()
    codificacao[0] = codificacao[0].strip("['")
    codificacao[-1] = codificacao[-1].strip("]'")
    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    with open (nome_do_arquivo) as imagem_decodificada:
        imagem = []
        for linha in imagem_decodificada:
            linha = linha.strip()
            linha_da_matriz = []
            linha_da_matriz.append(linha)
            imagem.append(linha_da_matriz) 
    del imagem[0]     
    del imagem[0]
    imagem2 = []
    for linha in imagem:
        linha2 = []
        for elemento in linha:
            for numero in elemento:
                linha2.append(int(numero))
        imagem2.append(linha2)
          

    largura = len(linha2)      
    altura = len(imagem)   
    imagem = imagem2    
    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as imagem_codificada:
        imagem_codificada.write('P1C\n')
        imagem_codificada.write(str(largura))
        imagem_codificada.write(' ')
        imagem_codificada.write(str(altura))
        imagem_codificada.write('\n')
        imagem_codificada.write(str(codificacao))

    pass


def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as imagem_decodificada:
        imagem_decodificada.write('P1\n')
        imagem_decodificada.write(str(largura))
        imagem_decodificada.write(' ')
        imagem_decodificada.write(str(altura))
        for linha in imagem:
            imagem_decodificada.write('\n')
            linha2 = []
            for item in linha:
                item = str(item)
                linha2.append(item)
            linha2 = ''.join(linha2)    
            imagem_decodificada.write(linha2)
            
        

    pass
