def calcular_diferenca(lista_dificuldade, N):
    diferenca = sum(lista_dificuldade) * -1
    diferencas = []
    for i in range(N):
        # tira a tarefa de gugu e passa para rangel
        diferenca = diferenca + (2 *lista_dificuldade[i])
        #tira o módulo do número
        if diferenca < 0:
            diferenca2 = diferenca * (-1)
        else:
            diferenca2 = diferenca    
        diferencas.append(diferenca2)
    diferencas = sorted(diferencas)
    menor_diferenca = diferencas[0]    
    return menor_diferenca 
             


def main():
    lista_diferenca = []
    while True:
        try:
            N = int(input())
            lista_dificuldade = input().split() 
            lista_dificuldade = [int(i) for i in lista_dificuldade]        
            diferenca = calcular_diferenca(lista_dificuldade, N)
            lista_diferenca.append(diferenca)
        except EOFError:
            break 
    for item in lista_diferenca:
        print(item)
main()
