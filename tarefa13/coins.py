def contar_notas(N, nota):
    notas = int(N//nota)
    resto = N % nota
    if notas > 0:
        print(f'{notas} nota(s) de R$ {"%.2f" % nota}')
    return(resto)
def contar_moedas(N, moeda):
    moedas = int(N//moeda)
    resto = N % moeda
    if moedas > 0:
        print(f'{moedas} moeda(s) de R$ {"%.2f" % moeda}')
    return(resto)    
def main():
    N = float(input())
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    if N > 2.00:
        print('NOTAS:')
    for item in notas:
        N = contar_notas(N,item)
    if N > 0.00:
        print('MOEDAS:')    
    for item in moedas: 
        N = contar_moedas(N,item)

main()    



