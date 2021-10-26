from modulo import *      


def destacar_bordas(largura, altura, imagem):
    bordas = imagem
    matriz = []
    for linha in imagem:
        linha = tuple(linha)
        matriz.append(linha)
    for i in range(altura):
         for j in range(largura):
           if i > 0 and i < altura - 1 and j > 0 and j < largura - 1:
            if matriz[i][j] == 1:
             if matriz[i][j + 1] == 1 and matriz[i - 1][j] == 1 and matriz[i +1][j+1] == 1: 
               if matriz[i - 1][j] == 1 and matriz[i][j -1] == 1 and matriz[i-1][j-1] == 1: 
                 if matriz[i +1 ][j -1] == 1 and matriz[i - 1][j+1] == 1 and matriz[i + 1][j] == 1:
                  bordas[i][j] = 0  
               
                 
    return bordas


def main():

    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()
