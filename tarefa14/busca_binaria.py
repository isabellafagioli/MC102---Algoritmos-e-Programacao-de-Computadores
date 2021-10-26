def buscar_i(sequencia, i, lim_inf, lim_sup):
    if  lim_inf <= lim_sup:
        novo_lim = (lim_inf + lim_sup) // 2
        if sequencia[novo_lim] == i:
            return novo_lim
        elif sequencia[novo_lim] < i:
            return buscar_i(sequencia, i, novo_lim +1, lim_sup)
        else:
            return buscar_i(sequencia, i, lim_inf, novo_lim - 1)
    elif lim_inf>=lim_sup and lim_inf != i:
        return -1  

def main():
    sequencia2 = []
    sequencia = input().split()
    for item in sequencia:
        item = int(item)
        sequencia2.append(item)
    sequencia = sequencia2    
    i = int(input())
    n = 0
    lim_sup = len(sequencia) - 1
    lim_inf = 0
    n = buscar_i(sequencia, i, lim_inf, lim_sup)
    print(n)

main()    